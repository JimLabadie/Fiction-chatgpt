#!/usr/bin/env python3
"""Build evidence-first repository catalogs from the checked-out Git tree.

The generated tables deliberately separate objective inventory facts from
mechanical review aids. Filename-family and content-signal columns are leads
for human review; they are never canon, equivalence, or authority decisions.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
import subprocess
import sys
import unicodedata
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "Systemwide" / "Audit"
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".csv", ".old", ".html", ".htm"}

def git_rows() -> list[tuple[str, str]]:
    raw = subprocess.check_output(["git", "ls-files", "-s", "-z"], cwd=ROOT)
    rows: list[tuple[str, str]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        meta, path = record.split(b"\t", 1)
        _mode, blob, _stage = meta.decode().split()
        decoded_path = path.decode("utf-8", "surrogateescape")
        # Audit products are excluded so the catalog is a stable inventory of
        # project sources and curated outputs rather than a self-hashing loop.
        if decoded_path.startswith("Systemwide/Audit/"):
            continue
        rows.append((decoded_path, blob))
    return sorted(rows)


def decode_text(data: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-16", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", "replace")


def xml_text(data: bytes) -> str:
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return ""
    pieces: list[str] = []
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] in {"t", "v"} and node.text:
            pieces.append(node.text)
    return " ".join(pieces)


def extract_zip(path: Path | io.BytesIO, suffix: str) -> tuple[str, int, list[tuple[str, int, int, str, str]]]:
    text_parts: list[str] = []
    members: list[tuple[str, int, int, str, str]] = []
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        for info in infos:
            member_suffix = Path(info.filename).suffix.lower()
            kind = "binary"
            if not info.is_dir() and (member_suffix in TEXT_EXTENSIONS or member_suffix in {".xml", ".rels"}):
                kind = "text"
            member_data = b"" if info.is_dir() else archive.read(info)
            members.append((
                info.filename, info.file_size, info.compress_size,
                hashlib.sha256(member_data).hexdigest(), kind,
            ))

        if suffix == ".docx":
            for name in ("word/document.xml", "docProps/core.xml"):
                try:
                    text_parts.append(xml_text(archive.read(name)))
                except KeyError:
                    pass
        elif suffix == ".xlsx":
            for info in infos:
                if info.filename in {"xl/workbook.xml", "xl/sharedStrings.xml"} or re.fullmatch(
                    r"xl/worksheets/sheet\d+\.xml", info.filename
                ):
                    text_parts.append(xml_text(archive.read(info)))
        else:
            for info in infos:
                member_suffix = Path(info.filename).suffix.lower()
                if info.is_dir():
                    continue
                if member_suffix in TEXT_EXTENSIONS:
                    text_parts.append(decode_text(archive.read(info)))
                elif member_suffix == ".docx":
                    nested_text, _count, _members = extract_zip(
                        io.BytesIO(archive.read(info)), ".docx"
                    )
                    text_parts.append(nested_text)
                elif member_suffix == ".xlsx":
                    nested_text, _count, _members = extract_zip(
                        io.BytesIO(archive.read(info)), ".xlsx"
                    )
                    text_parts.append(nested_text)
    return "\n".join(text_parts), len(members), members


def extract(path: Path) -> tuple[str, str, int, list[tuple[str, int, int, str, str]]]:
    suffix = path.suffix.lower()
    if suffix in {".docx", ".xlsx", ".skill", ".zip"}:
        try:
            text, count, members = extract_zip(path, suffix)
            return text, suffix.lstrip("+").lstrip("."), count, members
        except zipfile.BadZipFile:
            return "", "invalid-zip-container", 0, []
    if suffix == ".pdf":
        try:
            run = subprocess.run(
                ["pdftotext", str(path), "-"], check=True, capture_output=True
            )
            return decode_text(run.stdout), "pdf", 0, []
        except (FileNotFoundError, subprocess.CalledProcessError):
            return "", "pdf-unextracted", 0, []
    data = path.read_bytes()
    if suffix in TEXT_EXTENSIONS or not suffix:
        return decode_text(data), "text", 0, []
    return "", suffix.lstrip(".") or "unknown", 0, []


def normalize_family(path: str) -> str:
    name = unicodedata.normalize("NFKC", Path(path).stem).casefold()
    name = re.sub(r"^\[copy\](?:\[copy\])?", "", name)
    name = re.sub(r"^(?:copy of|copy|old[. _-]+|claude report[ _-]+)", "", name)
    name = re.sub(r"\s*\(\d+\)\s*$", "", name)
    name = re.sub(r"(?:[ _-]+(?:copy|old|revised|updated|final(?: canon)?|final use this))+$", "", name)
    name = re.sub(r"[ _-]+20\d{2}-\d{2}-\d{2}$", "", name)
    name = re.sub(r"\bthe\b", " ", name)
    name = re.sub(r"[^a-z0-9]+", " ", name).strip()
    return name


def source_zone(path: str) -> str:
    if path.startswith("Systemwide/Source/Original-Documents/"):
        return "source-original"
    if path.startswith("Systemwide/Source/Obsolete-Documents/"):
        return "source-obsolete"
    if path.startswith("Systemwide/Source/Readable-Sources/"):
        return "source-readable-conversion"
    if path.startswith("Systemwide/Source/conversations/"):
        return "source-conversation"
    if path.startswith("Systemwide/Source/"):
        return "source-metadata"
    if path.startswith("system bible/"):
        return "curated-output"
    return "other"


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main() -> int:
    if subprocess.run(["git", "diff", "--quiet"], cwd=ROOT).returncode != 0:
        print("Refusing to build from a dirty tree.", file=sys.stderr)
        return 2

    AUDIT.mkdir(parents=True, exist_ok=True)
    baseline = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    (AUDIT / "repository-baseline.txt").write_text(baseline + "\n", encoding="utf-8")
    records: list[dict[str, object]] = []
    package_members: list[list[object]] = []
    for relative, blob in git_rows():
        path = ROOT / relative
        data = path.read_bytes()
        text, kind, member_count, members = extract(path)
        normalized_text = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text)).strip()
        record = {
            "path": relative,
            "zone": source_zone(relative),
            "extension": path.suffix.lower().lstrip(".") or "[none]",
            "bytes": len(data),
            "git_blob_sha": blob,
            "sha256": hashlib.sha256(data).hexdigest(),
            "container_kind": kind,
            "container_members": member_count,
            "normalized_text_sha256": hashlib.sha256(normalized_text.encode("utf-8")).hexdigest() if normalized_text else "",
            "filename_family_candidate": normalize_family(relative) or "[empty-normalized-name]",
        }
        records.append(record)
        if path.suffix.lower() in {".skill", ".zip"}:
            for member_name, member_bytes, compressed_bytes, member_sha256, member_kind in members:
                package_members.append([
                    relative, member_name, member_bytes, compressed_bytes,
                    member_sha256, member_kind,
                ])

    blobs: dict[str, list[dict[str, object]]] = defaultdict(list)
    normalized_texts: dict[str, list[dict[str, object]]] = defaultdict(list)
    families: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        blobs[str(record["git_blob_sha"])].append(record)
        if record["normalized_text_sha256"]:
            normalized_texts[str(record["normalized_text_sha256"])].append(record)
        families[str(record["filename_family_candidate"])].append(record)

    duplicate_id: dict[str, str] = {}
    duplicate_rows: list[list[object]] = []
    index = 0
    for blob, members in sorted(blobs.items()):
        if len(members) < 2:
            continue
        index += 1
        group = f"D{index:03d}"
        for member in members:
            duplicate_id[str(member["path"])] = group
            duplicate_rows.append([group, blob, member["bytes"], member["path"]])

    inventory_header = [
        "path", "zone", "extension", "bytes", "git_blob_sha", "sha256",
        "exact_duplicate_group", "container_kind", "container_members",
        "filename_family_candidate",
    ]
    inventory_rows = []
    for record in records:
        inventory_rows.append([
            record[key] if key != "exact_duplicate_group" else duplicate_id.get(str(record["path"]), "")
            for key in inventory_header
        ])

    family_rows: list[list[object]] = []
    family_index = 0
    for normalized, members in sorted(families.items()):
        if len(members) < 2 or not normalized:
            continue
        family_index += 1
        family = f"F{family_index:03d}"
        exact_blobs = len({str(member["git_blob_sha"]) for member in members})
        for member in members:
            family_rows.append([
                family, normalized, len(members), exact_blobs,
                "mechanical-review-lead-not-equivalence", member["path"],
            ])

    write_tsv(AUDIT / "repository-file-inventory.tsv", inventory_header, inventory_rows)
    write_tsv(
        AUDIT / "exact-duplicate-groups.tsv",
        ["group", "git_blob_sha", "bytes", "path"],
        duplicate_rows,
    )
    text_duplicate_rows: list[list[object]] = []
    text_index = 0
    for digest, members in sorted(normalized_texts.items()):
        if len(members) < 2:
            continue
        text_index += 1
        group = f"T{text_index:03d}"
        distinct_blobs = len({str(member["git_blob_sha"]) for member in members})
        for member in members:
            text_duplicate_rows.append([
                group, digest, len(members), distinct_blobs,
                "normalized-extracted-text-match-not-authority-equivalence", member["path"],
            ])
    write_tsv(
        AUDIT / "normalized-text-match-groups.tsv",
        ["group", "normalized_text_sha256", "path_count", "distinct_blob_count", "status", "path"],
        text_duplicate_rows,
    )
    write_tsv(
        AUDIT / "filename-family-candidates.tsv",
        ["family", "normalized_name", "path_count", "distinct_blob_count", "status", "path"],
        family_rows,
    )
    write_tsv(
        AUDIT / "package-member-inventory.tsv",
        ["package_path", "member_path", "uncompressed_bytes", "compressed_bytes", "sha256", "member_kind"],
        package_members,
    )

    print(f"files={len(records)}")
    print(f"baseline={baseline}")
    print(f"source_files={sum(1 for record in records if str(record['zone']).startswith('source-'))}")
    print(f"exact_duplicate_groups={sum(1 for members in blobs.values() if len(members) > 1)}")
    print(f"exact_duplicate_extra_paths={sum(len(members) - 1 for members in blobs.values() if len(members) > 1)}")
    print(f"filename_family_candidates={sum(1 for members in families.values() if len(members) > 1)}")
    print(f"normalized_text_match_groups={sum(1 for members in normalized_texts.values() if len(members) > 1)}")
    print(f"package_members={len(package_members)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

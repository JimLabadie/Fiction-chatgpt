#!/usr/bin/env python3
"""Validate durable story-lifecycle invariants.

This checker deliberately verifies only facts that can be established from repository
bytes.  It does not claim that brainstorming was semantically complete, that a model
noticed a lifecycle trigger, or that a fresh chat applied the records correctly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


REQUIRED_DOCUMENTS = (
    "README.md",
    "series-bible.md",
    "character-bible.md",
    "world-and-setting.md",
    "voice-and-style.md",
    "series-outline.md",
    "timeline-and-continuity.md",
    "current-story-state.md",
    "series-development.md",
)
CHAPTER_NAME = re.compile(r"^(?P<number>\d{3}[A-Za-z]?)-.+\.md$")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def markdown_files(path: Path) -> list[Path]:
    if not path.is_dir():
        return []
    return sorted(item for item in path.glob("*.md") if item.name != ".gitkeep")


def validate_story(story: Path) -> list[Finding]:
    findings: list[Finding] = []

    for name in REQUIRED_DOCUMENTS:
        target = story / name
        if not target.is_file():
            findings.append(Finding("error", "missing-starter-document", str(target), f"Missing required starter document: {name}"))

    chapters = story / "chapters"
    candidate = chapters / "candidate"
    approved = chapters / "approved"
    for target, code in ((candidate, "missing-candidate-directory"), (approved, "missing-approved-directory")):
        if not target.is_dir():
            findings.append(Finding("error", code, str(target), "Required chapter lifecycle directory is missing"))

    plural_candidate = chapters / "candidates"
    if plural_candidate.exists():
        findings.append(Finding("error", "noncanonical-candidate-directory", str(plural_candidate), "Use chapters/candidate; the plural directory is not part of the maintained schema"))

    candidate_files = {item.name: item for item in markdown_files(candidate)}
    all_approved_files = {item.name: item for item in markdown_files(approved)}
    approved_files = {name: path for name, path in all_approved_files.items() if CHAPTER_NAME.match(name)}

    for name, path in sorted(all_approved_files.items()):
        if name not in approved_files:
            findings.append(Finding("error", "nonchapter-artifact-in-approved", str(path), "The approved lifecycle directory contains a Markdown artifact that does not follow the chapter filename pattern"))

    for name in sorted(candidate_files.keys() & approved_files.keys()):
        left = candidate_files[name]
        right = approved_files[name]
        if digest(left) == digest(right):
            findings.append(Finding("error", "promoted-candidate-retained", str(left), f"Candidate is byte-identical to approved/{name}; promoted candidates must be removed"))
        else:
            findings.append(Finding("info", "approved-revision-in-progress", str(left), f"Candidate differs from approved/{name}; treat it as a proposed revision and verify its status"))

    readme = story / "README.md"
    readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    for name in REQUIRED_DOCUMENTS[1:]:
        if name not in readme_text:
            findings.append(Finding("error", "story-record-not-linked", str(readme), f"README navigation does not link or name required story record: {name}"))

    outline = story / "series-outline.md"
    outline_text = outline.read_text(encoding="utf-8") if outline.is_file() else ""
    if approved_files and "no chapters approved" in outline_text.lower():
        findings.append(Finding("error", "approval-state-conflict", str(outline), "Series outline says no chapters are approved while chapter artifacts exist in chapters/approved"))

    approved_by_number: dict[str, list[Path]] = {}
    for name, path in approved_files.items():
        match = CHAPTER_NAME.match(name)
        assert match is not None
        approved_by_number.setdefault(match.group("number").lower(), []).append(path)
    for number, paths in sorted(approved_by_number.items()):
        if len(paths) > 1:
            findings.append(Finding("error", "multiple-approved-artifacts-for-number", str(approved), f"Chapter number {number} has multiple approved artifacts: {', '.join(path.name for path in paths)}"))

    for name, path in approved_files.items():
        relative = f"chapters/approved/{name}"
        if relative not in outline_text:
            findings.append(Finding("error", "approved-chapter-not-registered", str(path), f"Series outline does not reference {relative}"))

    if approved_files:
        state = story / "current-story-state.md"
        state_text = state.read_text(encoding="utf-8").strip() if state.is_file() else ""
        if not state_text:
            findings.append(Finding("error", "missing-current-handoff", str(state), "Approved prose exists but the current-story-state record is empty or missing"))
        elif not any(term in state_text.lower() for term in ("handoff", "current", "next")):
            findings.append(Finding("error", "unrecognizable-current-handoff", str(state), "Current-story-state does not expose an identifiable current/handoff/next section"))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stories", nargs="+", type=Path, help="Story directories to validate")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    report = []
    exit_code = 0
    for story in args.stories:
        findings = validate_story(story)
        if any(item.severity == "error" for item in findings):
            exit_code = 1
        report.append({"story": str(story), "findings": [asdict(item) for item in findings]})

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for item in report:
            print(f"{item['story']}: {len(item['findings'])} finding(s)")
            for finding in item["findings"]:
                print(f"  {finding['severity'].upper()} {finding['code']}: {finding['path']} — {finding['message']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

import tempfile
import unittest
from pathlib import Path

from validate_story_lifecycle import REQUIRED_DOCUMENTS, validate_story


def make_story(root: Path) -> Path:
    story = root / "Test Story"
    story.mkdir()
    for name in REQUIRED_DOCUMENTS:
        content = "# Test\n"
        if name == "README.md":
            content += "\n".join(REQUIRED_DOCUMENTS[1:]) + "\n"
        if name == "series-outline.md":
            content += "chapters/approved/001-opening.md\n"
        if name == "current-story-state.md":
            content += "Current handoff: after chapter one.\n"
        (story / name).write_text(content, encoding="utf-8")
    (story / "chapters" / "candidate").mkdir(parents=True)
    (story / "chapters" / "approved").mkdir()
    (story / "chapters" / "approved" / "001-opening.md").write_text("# Opening\n", encoding="utf-8")
    return story


class StoryLifecycleValidationTests(unittest.TestCase):
    def test_complete_story_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(validate_story(make_story(Path(temp))), [])

    def test_retained_promoted_candidate_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            story = make_story(Path(temp))
            text = (story / "chapters" / "approved" / "001-opening.md").read_text(encoding="utf-8")
            (story / "chapters" / "candidate" / "001-opening.md").write_text(text, encoding="utf-8")
            codes = {finding.code for finding in validate_story(story)}
            self.assertIn("promoted-candidate-retained", codes)

    def test_missing_handoff_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            story = make_story(Path(temp))
            (story / "current-story-state.md").write_text("", encoding="utf-8")
            codes = {finding.code for finding in validate_story(story)}
            self.assertIn("missing-current-handoff", codes)

    def test_conflicting_approval_state_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            story = make_story(Path(temp))
            outline = story / "series-outline.md"
            outline.write_text(outline.read_text(encoding="utf-8") + "No chapters approved.\n", encoding="utf-8")
            codes = {finding.code for finding in validate_story(story)}
            self.assertIn("approval-state-conflict", codes)

    def test_missing_navigation_link_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            story = make_story(Path(temp))
            (story / "README.md").write_text("# Test\n", encoding="utf-8")
            codes = {finding.code for finding in validate_story(story)}
            self.assertIn("story-record-not-linked", codes)


if __name__ == "__main__":
    unittest.main()

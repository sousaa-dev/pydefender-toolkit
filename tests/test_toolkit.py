import hashlib
import tempfile
import unittest
from pathlib import Path
from pydefender import fingerprint, summarize, inventory


class ToolkitTests(unittest.TestCase):
    def test_fingerprint(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "sample"
            path.write_bytes(b"hello")
            self.assertEqual(fingerprint(path), hashlib.sha256(b"hello").hexdigest())

    def test_summary(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "sample.jsonl"
            path.write_text('{"level":"INFO"}\ninvalid\n', encoding="utf-8")
            self.assertEqual(summarize(path), {"levels": {"info": 1}, "invalid_lines": 1})

    def test_inventory(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root)
            (path / "sample").write_bytes(b"abc")
            self.assertEqual(inventory(path)[0]["size_bytes"], 3)

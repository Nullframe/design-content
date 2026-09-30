#!/usr/bin/env python3
"""Checks every published archive listed in packs/*/pack.json, downloaded anonymously.

For each archive: its SHA-256 and size; its MANIFEST.json (every file there with its SHA-256, and the pack's SHA-256
over the `<sha256>  <path>` lines, sorted by path); every font file listed in the pack's NOTICES.md with a licence
file that is in the archive and holds a licence text.

Usage: python3 scripts/verify_packs.py [--file ARCHIVE]  (--file: check a local archive against pack.json instead)
"""
import hashlib
import json
import os
import re
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT = re.compile(r"\.(ttf|otf|ttc|woff2?)$", re.I)
LICENCE_TEXT = re.compile(r"SIL OPEN FONT LICENSE Version 1\.1|Apache License|UBUNTU FONT LICENCE", re.I)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url, to):
    # No Authorization header: a user without GitHub access must be able to fetch it.
    req = urllib.request.Request(url, headers={"User-Agent": "design-content-verify"})
    with urllib.request.urlopen(req, timeout=300) as res, open(to, "wb") as out:
        while chunk := res.read(1 << 20):
            out.write(chunk)


def check_archive(pack_dir, entry, archive, errors):
    say = lambda msg: errors.append(f"{entry['archive']}: {msg}")
    if sha256(archive) != entry["archiveSha256"]:
        say(f"archive sha256 {sha256(archive)} != {entry['archiveSha256']}")
    if os.path.getsize(archive) != entry["size"]:
        say(f"size {os.path.getsize(archive)} != {entry['size']}")
    with tempfile.TemporaryDirectory() as tmp:
        with tarfile.open(archive) as tar:
            tar.extractall(tmp, filter="data")
        tops = os.listdir(tmp)
        if len(tops) != 1:
            say(f"expected one top folder, found {tops}")
            return
        top = Path(tmp, tops[0])
        manifest = json.loads((top / "MANIFEST.json").read_text())
        files = manifest["files"]
        lines = "".join(f"{files[rel]['sha256']}  {rel}\n" for rel in sorted(files))
        if hashlib.sha256(lines.encode()).hexdigest() != entry["sha256"] or manifest.get("sha256") != entry["sha256"]:
            say("pack sha256 (MANIFEST.json) differs from pack.json")
        for rel, meta in files.items():
            p = top / rel
            if not p.exists() or sha256(p) != meta["sha256"]:
                say(f"{rel} missing or differs from MANIFEST.json")
        on_disk = {str(p.relative_to(top)) for p in top.rglob("*") if p.is_file() and p.name != "MANIFEST.json"}
        extra = on_disk - set(files)
        if extra:
            say(f"files not in MANIFEST.json: {sorted(extra)}")
        notices = (pack_dir / "NOTICES.md").read_text()
        for rel in sorted(on_disk):
            if not FONT.search(rel):
                continue
            row = next((l for l in notices.splitlines() if f"`{rel}`" in l), None)
            if not row:
                say(f"{rel} is not in {pack_dir.name}/NOTICES.md")
                continue
            lic = re.findall(r"`([^`]+)`", row)[-1]
            lp = top / lic
            if not lp.is_file() or not LICENCE_TEXT.search(lp.read_text(errors="replace")):
                say(f"{rel}: licence file {lic} missing from the archive or holds no licence text")


def main():
    local = sys.argv[sys.argv.index("--file") + 1] if "--file" in sys.argv else None
    errors, checked = [], 0
    for pack_json in sorted(ROOT.glob("packs/*/pack.json")):
        pack = json.loads(pack_json.read_text())
        for entry in pack["archives"]:
            if local and Path(local).name != entry["archive"]:
                continue
            with tempfile.TemporaryDirectory() as tmp:
                archive = local or os.path.join(tmp, entry["archive"])
                if not local:
                    print(f"GET {entry['url']}", flush=True)
                    try:
                        download(entry["url"], archive)
                    except Exception as e:  # noqa: BLE001
                        errors.append(f"{entry['archive']}: download failed: {e}")
                        continue
                check_archive(pack_json.parent, entry, archive, errors)
                checked += 1
    for e in errors:
        print(f"FAIL {e}")
    print(f"{checked} archive(s) checked, {len(errors)} problem(s)")
    sys.exit(1 if errors or not checked else 0)


if __name__ == "__main__":
    main()

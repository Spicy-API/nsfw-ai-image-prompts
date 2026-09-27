#!/usr/bin/env python3
"""Validate prompt data: model settings, adult-only wording, banned terms, and README freshness."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

BANNED = re.compile(
    r"\b(teen\w*|school\s?girl|school uniform|student|loli\w*|shota|child\w*|kid|minor|underage|"
    r"young[- ]looking|petite|little girl|chibi|celebrity|drunk|asleep and|unconscious|forced|"
    r"non-?consensual|incest|step-?(sister|mom|brother|dad)|undress\w*)\b",
    re.IGNORECASE,
)
ADULT_MARKER = re.compile(r"\b(adult|in (her|his|their) (early |late )?(20s|30s|40s)|woman in her|man in his)\b", re.IGNORECASE)


def main() -> int:
    doc = json.loads((DATA / "models.json").read_text())
    models, loras = doc["models"], doc["loras"]
    data = json.loads((DATA / "image-prompts.json").read_text())
    errors: list[str] = []
    ids = [p["id"] for p in data["prompts"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"duplicate ids: {sorted(dupes)}")
    cats = {c["key"] for c in data["categories"]}
    for p in data["prompts"]:
        pid, m = p["id"], models.get(p["model"])
        if p["cat"] not in cats:
            errors.append(f"{pid}: unknown category {p['cat']}")
        if m is None:
            errors.append(f"{pid}: unknown model {p['model']}")
            continue
        if "size" in p:
            if "max_side" not in m or max(int(v) for v in p["size"].split("x")) > m["max_side"]:
                errors.append(f"{pid}: size {p['size']} not valid for {m['name']}")
        else:
            if p["res"] not in m.get("prices", {}):
                errors.append(f"{pid}: resolution {p['res']} not offered by {m['name']}")
            if p["ar"] not in m.get("aspect_ratios", []):
                errors.append(f"{pid}: aspect ratio {p['ar']} not offered by {m['name']}")
        if p.get("lora"):
            if p["model"] != "qwen21lora":
                errors.append(f"{pid}: LoRA set on a model without LoRA support")
            for name in p["lora"].split("+"):
                if name not in loras:
                    errors.append(f"{pid}: unknown LoRA {name}")
        if m.get("edit") and not p.get("input"):
            errors.append(f"{pid}: editing prompt needs an input description")
        text = " ".join([p["prompt"], p["title"], p.get("input", "")])
        if BANNED.search(text):
            errors.append(f"{pid}: banned term '{BANNED.search(text).group(0)}'")
        if not m.get("edit") and not ADULT_MARKER.search(p["prompt"]):
            errors.append(f"{pid}: prompt does not state an adult subject")
    readmes = [r for r in ROOT.glob("README*.md") if ".template" not in r.name]
    before = {r.name: r.read_text() for r in readmes}
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_readme.py")], check=True, capture_output=True)
    for r in ROOT.glob("README*.md"):
        if ".template" not in r.name and before.get(r.name) != r.read_text():
            errors.append(f"{r.name} was stale; it has been regenerated, commit the result")
    for e in errors:
        print("ERROR", e)
    print(f"checked {len(data['prompts'])} image prompts: {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

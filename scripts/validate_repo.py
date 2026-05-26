#!/usr/bin/env python3
"""Validate repository structure and the bundled example diagram."""

from __future__ import annotations

import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "html-swimlane-diagram"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    SKILL / "SKILL.md",
    SKILL / "LICENSE.txt",
    SKILL / "agents" / "openai.yaml",
    SKILL / "assets" / "swimlane-template.html",
    SKILL / "references" / "lane_dimension_examples.md",
    SKILL / "references" / "process_extraction.md",
    SKILL / "references" / "routing_algorithm.md",
    SKILL / "references" / "swimlane_rules.md",
    SKILL / "scripts" / "lint_svg_links.py",
    ROOT / "examples" / "mall-marketing-workflow.md",
    ROOT / "examples" / "mall-marketing-swimlane.html",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path.relative_to(ROOT)}")
        return 1

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    for required in ("name: html-swimlane-diagram", "description:"):
        if required not in skill_text:
            print(f"SKILL.md is missing required metadata: {required}")
            return 1

    lint = subprocess.run(
        [
            sys.executable,
            str(SKILL / "scripts" / "lint_svg_links.py"),
            str(ROOT / "examples" / "mall-marketing-swimlane.html"),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(lint.stdout, end="")
    if lint.returncode != 0:
        return lint.returncode

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

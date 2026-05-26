# HTML Swimlane Diagram Skill

Generate editable HTML/SVG swimlane diagrams with fixed lanes, decision branches, orthogonal connectors, sticky headers, and connector linting.

This repository packages a Codex skill named `html-swimlane-diagram`.

## What It Does

- Creates one self-contained `.html` file per diagram.
- Uses inline SVG, so the output can be edited directly.
- Supports role/organization lanes, system/module lanes, or another single homogeneous lane dimension.
- Uses approval diamonds with `Y/N` branches.
- Validates connector paths with a bundled Python linter.

## Repository Layout

```text
.
├── skills/
│   └── html-swimlane-diagram/
│       ├── SKILL.md
│       ├── LICENSE.txt
│       ├── agents/openai.yaml
│       ├── assets/swimlane-template.html
│       ├── references/
│       └── scripts/lint_svg_links.py
├── examples/
│   ├── mall-marketing-workflow.md
│   └── mall-marketing-swimlane.html
└── scripts/validate_repo.py
```

## Install

Install the skill directory into Codex from this repository:

```bash
$skill-installer install https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram
```

Restart Codex after installation if the skill does not appear immediately.

## Usage

In Codex, ask:

```text
Use $html-swimlane-diagram to generate a role-based swimlane diagram for a mall admin marketing campaign.
```

The skill will produce a single HTML file. For underspecified workflows, it should research likely roles and process steps first, then label the result as a researched draft.

## Validate

Validate the example output:

```bash
python3 skills/html-swimlane-diagram/scripts/lint_svg_links.py examples/mall-marketing-swimlane.html
```

Validate the repository structure and example:

```bash
python3 scripts/validate_repo.py
```

## Development

Keep the skill itself lean:

- Put core instructions in `skills/html-swimlane-diagram/SKILL.md`.
- Put detailed guidance in `references/`.
- Put deterministic checks or generators in `scripts/`.
- Put reusable output templates in `assets/`.
- Keep repository docs such as this README outside the skill directory.

## License

MIT. See `LICENSE` and `skills/html-swimlane-diagram/LICENSE.txt`.

# HTML Swimlane Diagram · Editable HTML Swimlane Diagram Skill

An agent skill for Codex, Claude Code, Cursor, and similar coding-agent environments. It converts business workflows, approval processes, system flows, rough notes, or Mermaid-style process material into a **single-file HTML/SVG swimlane diagram**.

The goal is not to create a static screenshot. The skill produces an editable `.html` file that can be opened in a browser, inspected, modified, and validated.

## What You Get

- Fixed-lane diagrams for role/organization lanes, system/module lanes, or another single homogeneous dimension
- Phase bands with a left-side phase rail and sticky lane header
- Decision diamonds with explicit `Y/N` branches
- Local rework loops for rejection, exception handling, and resubmission
- Orthogonal SVG connectors with horizontal/vertical routing
- A bundled Python linter for diagonal, crossing, and overlapping connector paths
- Single-file HTML output with inline CSS/SVG, no build step or server required

## Fits / Doesn't Fit

Fits:

- Admin workflows for ecommerce, ERP, CRM, OA, support, and internal tools
- Approval flows, procurement flows, inventory flows, campaign flows, ticket flows
- Role-based diagrams that clarify ownership and handoffs
- System/module diagrams that clarify boundaries and data movement
- Product portfolios, requirement reviews, SOP documentation, and interview artifacts

Doesn't fit:

- Large-scale BPMN modeling and simulation
- Multi-user real-time diagram editing platforms
- Freeform posters or highly decorative infographics
- Workflows that must export native Visio, Draw.io, or Figma source files

## Install

### Option 1: Skill Installer

```bash
$skill-installer install https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram
```

Restart Codex if the skill does not appear immediately.

### Option 2: Paste This To An AI Agent

```text
Install the html-swimlane-diagram skill for me:
1. Make sure the local Codex skills directory exists.
2. Install the skill from https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram.
3. Verify the installed skill contains SKILL.md, assets/, references/, and scripts/.
4. Tell me the result.
```

## How To Trigger It

```text
Use $html-swimlane-diagram to generate a role-based swimlane diagram for a mall admin marketing campaign.
```

More trigger examples:

- `Use $html-swimlane-diagram to turn this procurement approval flow into a swimlane diagram.`
- `Generate a role-based swimlane diagram for the ticket lifecycle from submission to closure.`
- `Convert this Mermaid sequence diagram into an editable HTML swimlane diagram.`
- `Draw a system-module swimlane diagram for order, inventory, payment, and notification flow.`

## Workflow

The skill follows a structured workflow:

1. Understand the input: goals, phases, actions, approvals, branches, and end states
2. Choose one lane dimension: roles/organizations, systems/modules, or another homogeneous dimension
3. Research missing defaults when the user provides only a vague domain request
4. Place every node before drawing connectors
5. Route arrows with horizontal/vertical SVG paths and compact rework loops
6. Run the connector linter
7. Deliver one editable `.html` file

## Repository Layout

```text
html-swimlane-diagram/
├── README.md
├── README.en.md
├── LICENSE
├── CONTRIBUTING.md
├── examples/
│   ├── mall-marketing-workflow.md
│   └── mall-marketing-swimlane.html
├── scripts/
│   └── validate_repo.py
└── skills/
    └── html-swimlane-diagram/
        ├── SKILL.md
        ├── LICENSE.txt
        ├── agents/openai.yaml
        ├── assets/swimlane-template.html
        ├── references/
        └── scripts/lint_svg_links.py
```

## Example

This repository includes a mall admin marketing campaign example:

- Input brief: [examples/mall-marketing-workflow.md](examples/mall-marketing-workflow.md)
- Generated diagram: [examples/mall-marketing-swimlane.html](examples/mall-marketing-swimlane.html)

Open the HTML file directly in a browser.

## Validate

Validate the example connector paths:

```bash
python3 skills/html-swimlane-diagram/scripts/lint_svg_links.py examples/mall-marketing-swimlane.html
```

Validate the repository structure and example:

```bash
python3 scripts/validate_repo.py
```

GitHub Actions runs the same repository validation on push and pull request.

## Design Principles

- Choose exactly one lane dimension per diagram.
- Do not mix people/departments and systems/modules as peer lanes.
- Put approval nodes in the reviewer, manager, compliance, or owning-system lane.
- Place business nodes before connector routing.
- Keep rework loops local and readable.
- Every generated diagram should be readable, editable, and validated.

## License

MIT. See [LICENSE](LICENSE) and [skills/html-swimlane-diagram/LICENSE.txt](skills/html-swimlane-diagram/LICENSE.txt).

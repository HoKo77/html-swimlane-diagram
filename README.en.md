# HTML Swimlane Diagram Skills

![Skill](https://img.shields.io/badge/Skill-Codex-315596)
![Output](https://img.shields.io/badge/Output-HTML%20%2F%20SVG-416bb3)
![License](https://img.shields.io/badge/License-MIT-green)

```text
HTML Swimlane Diagram
├─ Editable single-file HTML/SVG
├─ Role or system swimlanes
├─ Y/N decision branches
├─ Orthogonal arrows and rework loops
└─ Bundled connector linter
```

An agent skill package for Codex-style environments. It converts business workflows, approval processes, system flows, Mermaid snippets, or rough notes into an **editable single-file HTML/SVG swimlane diagram**.

The point is not just to draw a picture. The skill gives the agent a repeatable process for workflow extraction, lane normalization, node placement, arrow routing, and connector validation.

## Skills

| Skill | Purpose | Output | Risk Level |
| --- | --- | --- | --- |
| `html-swimlane-diagram` | Generate or refine swimlane diagrams for business workflows, approval flows, system flows, SOPs, and product docs | One `.html` file with inline SVG/CSS | Low: local file generation, no external service dependency |

## Agent Quick Reference

Shortest useful prompt:

```text
Use $html-swimlane-diagram to generate a role-based swimlane diagram for a mall admin marketing campaign.
```

Recommended input fields:

- Workflow topic: ecommerce campaign, procurement approval, inventory transfer, ticket handling
- Lane preference: role/organization lanes or system/module lanes
- Key steps: initiate, configure, review, launch, monitor, retrospective
- Decisions: approved, rejected, abnormal, rework required
- Output request: generate one editable HTML file

If you only provide a vague domain, the skill should research common workflow defaults first and label the result as a draft.

## What You Get

- **Fixed lanes**: one lane dimension per diagram
- **Phase bands**: left-side phase rail and sticky lane header
- **Decision nodes**: approval, validation, and exception handling as diamonds with `Y/N`
- **Rework loops**: local rejection and resubmission paths
- **Orthogonal arrows**: SVG paths using horizontal/vertical routing
- **Quality checks**: bundled linter for diagonal, crossing, and overlapping links
- **Single-file output**: inline CSS/SVG, no build step or server required

## Install

### Skill Installer

```bash
$skill-installer install https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram
```

Restart Codex if the skill does not appear immediately.

### Manual / Agent-Assisted Install

Paste this to an agent with shell access:

```text
Install the html-swimlane-diagram skill for me:
1. Make sure the local Codex skills directory exists.
2. Install the skill from https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram.
3. Verify the installed skill contains SKILL.md, agents/, assets/, references/, and scripts/.
4. Run the example validation script and tell me the result.
```

## Example Prompts

```text
Use $html-swimlane-diagram to generate a role-based swimlane diagram for a mall admin marketing campaign.
```

```text
Use $html-swimlane-diagram to turn this procurement approval process into a role swimlane diagram:
requester submits purchase request -> procurement collects quotes -> manager reviews -> finance reviews -> order is placed -> goods are received -> reconciliation and payment.
```

```text
Use $html-swimlane-diagram to generate a system-module swimlane diagram for order, inventory, payment, and notification flow.
```

## How It Works

```text
workflow input
  ↓
understand and research
  ↓
choose lane dimension
  ↓
place nodes
  ↓
route orthogonal links
  ↓
run SVG link linter
  ↓
deliver single-file HTML
```

Core rules:

- Choose exactly one lane dimension per diagram.
- In role lanes, approval nodes belong to reviewers, not submitters.
- In system lanes, decision nodes belong to the system that owns the rule or data.
- Place every node before drawing arrows.
- Prefer compact local loops for rejection and exception paths.

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

## Included Example

- Input brief: [examples/mall-marketing-workflow.md](examples/mall-marketing-workflow.md)
- Generated diagram: [examples/mall-marketing-swimlane.html](examples/mall-marketing-swimlane.html)

Open `examples/mall-marketing-swimlane.html` directly in a browser.

## Validation

Validate the example connector paths:

```bash
python3 skills/html-swimlane-diagram/scripts/lint_svg_links.py examples/mall-marketing-swimlane.html
```

Validate the repository structure and example output:

```bash
python3 scripts/validate_repo.py
```

GitHub Actions runs validation on push and pull request.

## Scope

Fits:

- Admin workflows, approval flows, ticket flows, procurement flows, inventory flows, campaign flows
- Product docs, requirement reviews, SOPs, portfolio artifacts
- Cases where editable HTML is more useful than a one-off screenshot

Doesn't fit:

- Large-scale BPMN modeling and simulation
- Multi-user real-time diagramming platforms
- Workflows that must export native Visio, Draw.io, or Figma source files

## License

MIT. See [LICENSE](LICENSE) and [skills/html-swimlane-diagram/LICENSE.txt](skills/html-swimlane-diagram/LICENSE.txt).

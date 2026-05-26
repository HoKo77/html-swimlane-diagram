---
name: html-swimlane-diagram
description: Use this skill when creating, converting, or refining homogeneous swimlane diagrams as a single editable HTML file with inline SVG, especially from Markdown workflows, Mermaid sequence diagrams, business process notes, procurement/inventory processes, system workflows, or approval flows. Choose one lane dimension per diagram, such as all roles/organizations or all systems/modules; never mix role lanes and system lanes. When the user does not provide lanes or process steps, use browser/search research first to identify credible workflow patterns before drafting the diagram.
---

# HTML Swimlane Diagram

## Purpose

Generate one editable HTML/SVG swimlane diagram. Keep this skill stable by using a small pipeline in `SKILL.md` and loading detailed references only when needed.

Pattern mix, based on ADK skill design patterns:

- **Generator**: create the HTML diagram from a reusable template.
- **Inversion**: ask the user to confirm roles or flow only when the source is missing or ambiguous.
- **Reviewer**: run connector checks and visual review before delivery.
- **Pipeline**: preserve the order: understand -> place nodes -> route links -> review -> deliver.

## Core Defaults

- Output only a single `.html` file.
- Start from `assets/swimlane-template.html`.
- Choose one lane dimension before drawing: role/organization lanes, system/module lanes, or another single homogeneous dimension that fits the source.
- Do not mix lane dimensions in one diagram. If a candidate lane list contains both roles/departments/organizations and systems/modules/platforms, convert it to one dimension before placing nodes.
- Confirm provided swimlane lanes before drawing.
- If swimlane lanes are missing or vague, research them with browser/search tools before drafting.
- Confirm provided process steps before drawing.
- If process steps are missing or vague, research them with browser/search tools before drafting.
- Place all nodes before drawing connectors.
- Use approval diamonds with `Y/N` branches.
- In role/organization lane mode, put approval nodes in supervisor/reviewer lanes, not the submitter lane.
- In system/module lane mode, put validation/approval automation in the system that owns the decision, and mention the human approver in node text when relevant.
- Route connectors orthogonally; avoid crossings, overlaps, and node collisions.

## Workflow

1. **Understand And Research**
   - Extract candidate lanes, lane dimension, phases, actions, approvals, branches, rework loops, and end states.
   - Decide the lane dimension from the user's framing and source material:
     - Use role/organization lanes when accountability, handoffs, approvals, responsibilities, or cross-department collaboration are the main point.
     - Use system/module lanes when integration, automation, data flow, API handoff, or platform ownership is the main point.
     - Use another homogeneous dimension only when the source clearly requires it.
   - Treat systems used by people as node context in a role/organization diagram. Treat people operating systems as node context in a system/module diagram.
   - If the source mixes dimensions, normalize it before drawing and make the assumption visible in the delivery note or diagram title/subtitle.
   - If the user supplied roles and an end-to-end process, use those directly.
   - If roles or process are missing, vague, or only named by domain (for example "ERP询价", "采购审批", "库存调拨"), do not invent the structure from memory. Use browser/search tools to research credible public references first.
   - Prefer official product docs, ERP/vendor documentation, procurement SOPs, standards, or high-quality business process references. Avoid relying on a single low-quality SEO article.
   - From the research, extract a compact "调研草案": lane dimension, candidate lanes, ordered phases, key actions, decision points, rework paths, and end states.
   - Mention that the flow is based on researched defaults if the user did not provide source-specific roles or process.
   - Ask for confirmation only when the researched defaults materially affect ownership, compliance, or approval authority; otherwise proceed with a first draft and make the assumptions visible in the diagram text or delivery note.

2. **Place Nodes**
   - Lay out the full node set by lane, phase, and process order before drawing any link.
   - Prefer a top-to-bottom main path.
   - Keep `N` rework/resubmit nodes close to the decision they return to.

3. **Route Links**
   - Calculate links after node placement.
   - Use only horizontal/vertical SVG segments.
   - Prefer compact `重新提交` loops for rejected approvals.
   - If routing becomes messy, move nodes first; do not compensate with large crossing paths.

4. **Review**
   - Run `python3 scripts/lint_svg_links.py output.html`.
   - Open the HTML and visually check missing steps, branch labels, node collisions, crossed links, and sticky header behavior.
   - Iterate until the HTML is readable and passes connector checks.

5. **Deliver**
   - Deliver the HTML file only.
   - Do not generate PDF, PNG, screenshots, Markdown wrappers, or document wrappers in this skill.

## Load References Only When Needed

- `references/process_extraction.md`: use when the source is Markdown, Mermaid, rough notes, or the roles/process are unclear. It includes the required research-first behavior for underspecified workflows.
- `references/swimlane_rules.md`: use when adjusting role ownership, approval branches, visual layout, or fixing user-reported diagram style issues.
- `references/routing_algorithm.md`: use only for complex diagrams or when connectors cross, overlap, pass through nodes, or fail the linter.
- `references/lane_dimension_examples.md`: use when deciding between role/organization lanes, system/module lanes, or another homogeneous lane dimension.

## Validation Script

Use the connector linter before delivery:

```bash
python3 scripts/lint_svg_links.py output.html
```

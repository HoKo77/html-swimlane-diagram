# Swimlane Diagram Rules

Use this reference when refining visual style, role ownership, approval branches, or user-reported diagram issues. Treat these as defaults and troubleshooting rules, not as a reason to overcomplicate simple diagrams.

## Layout

- Use `assets/swimlane-template.html` as the default visual baseline.
- Use fixed-width lanes. Do not auto-resize each lane independently.
- Use a sticky role header for tall diagrams.
- Prefer full-screen presentation. Only show scrollbars when the fixed canvas exceeds the viewport.
- Keep phase labels in a narrow left band when phases are important.
- Use consistent node sizes; only widen a node when text cannot fit professionally.
- Avoid nested card-style containers. The diagram surface should be direct and readable.
- Finish node placement before drawing connectors. Do not use connector convenience to decide the process structure.
- If routing is messy, fix node placement first, then reroute.

## Layout Patterns

- Use a top-to-bottom main spine for the normal successful process.
- Put the `Y` path below a decision whenever possible.
- Put `N` correction/rework nodes near the decision that rejected the flow.
- Keep rework loops local: correction node -> corrected submission/review -> same decision.
- Prefer the compact `重新提交` loop style: rework node immediately left of the decision, `N` exits the diamond side, and `重新提交` returns through a short local path to the diamond top or left point.
- Do not place a correction target far above or across several lanes if it forces long return lines.
- Avoid dense bands where several nodes and decisions share the same y-range across many lanes.
- Add a blank routing row between major decision groups when a return loop exists.
- If a branch line needs to cross more than two lanes, first consider moving the target node closer or adding an intermediate process node.

## Node Types

- Start/end: rounded pill.
- Work/action: rectangle.
- Approval/review/judgment: diamond.
- Use diamonds for decisions that have `Y` and `N` exits.
- Do not duplicate an approval as multiple diamonds unless the process has distinct decisions.
- In role/organization lane mode, approval/review diamonds must be placed in a supervisor, manager, reviewer, finance manager, risk-control, audit, or compliance lane.
- In role/organization lane mode, a specialist lane can submit or revise a request, but should not approve its own request.
- In system/module lane mode, decision diamonds belong to the system/module that evaluates, routes, stores, or enforces the decision.

## Role Rules

Apply these only when the chosen lane dimension is role/organization. For system/module swimlanes, use system ownership and data/control handoff rules instead.

- Enforce maker/checker separation in the diagram.
- Use paired submitter/checker roles where the source or researched workflow implies a maker/checker control.
- Use a neutral reviewer lane only when the source does not specify a domain-specific checker.
- If an approval node is found but no checker role exists, add a draft checker lane and mark it for user confirmation.
- Keep domain-specific approvals separate when they mean different accountability, such as campaign approval versus payment approval.

## Lane Dimension Rules

- Choose exactly one lane dimension before layout: role/organization, system/module, or another source-driven dimension.
- Do not place systems and roles as peer lanes in the same diagram.
- If a business workflow mentions a system, keep the system inside the action text when using role/organization lanes.
- If a system workflow mentions an operator or approver, keep the human role inside the action text when using system/module lanes.
- Use `lane_dimension_examples.md` as dimension guidance, not as fixed lane templates.

## Connector Rules

- Every connector must have a visible arrowhead.
- Arrowheads should touch the target node edge.
- Connectors must be orthogonal. Every path segment must be horizontal or vertical.
- Never create a connector segment where both x and y change between adjacent points.
- Connectors must not cross other connectors.
- Connectors must not overlap/share the same corridor with other connectors except at an intentional merge point immediately before a shared target.
- Connectors must not pass through node interiors or run under node text.
- Avoid direct diagonal segments such as `M265 304 L335 529`, `M570 1094 L265 1119`, or `M775 1614 L485 1740`.
- Prefer `H`/`V` commands or explicit right-angle `L` paths:
  - valid: `M265 304 H320 V529 H335`
  - valid: `M570 1094 H520 V1119 H265`
  - invalid: `M570 1094 L265 1119`
- Rectangles should normally have one incoming and one outgoing connector.
- Branching belongs to diamonds.
- Connect from and to edge centers:
  - rectangle right/left/top/bottom center
  - diamond top/right/bottom/left point
- Avoid using rectangle corners as connection points.

## Branch Routing

- `Y` from a diamond usually leaves from the bottom point and continues the main path.
- `N` should route to a correction/rework node and return to the same decision when resubmission is required.
- Keep rejection/return loops outside the main forward path. Use outer corridors rather than crossing through the middle of the current step group.
- If `Y` and `N` branches from a diamond would cross, change the node placement or branch direction before drawing.
- For approval decisions, prefer this pattern: submitter node -> checker diamond -> `Y` down to next main step; `N` sideward to correction node; correction loops back into the input/review step without crossing the `Y` path.
- Preferred compact resubmit style:
  - Place correction/rework node adjacent to the decision, usually on the left.
  - Route `N` horizontally from the decision left point to the correction node right edge.
  - Route `重新提交` from the correction node right/top edge back to the decision top or left point.
  - Keep the return path short and local; do not wrap around unrelated nodes.
  - Put the `重新提交` label on the return segment, not inside a node.
- Place `Y` and `N` labels close to their branch segments without covering lines or nodes.

## Cross-Lane Routing

- Rightward movement can be same-level: source side center -> horizontal segment -> target edge center.
- Leftward movement should usually go down first, then left, then enter target edge center.
- If lines become visually close or overlap, add offset corridors between rows.
- Reserve separate routing corridors for separate branches; do not stack multiple links on the same horizontal or vertical line.
- For direct vertical links, increase vertical distance enough that labels and arrowheads do not crowd the nodes.

## Crossing Avoidance

- Treat a crossed connector as a layout bug.
- Use an algorithmic routing pass after all nodes are placed.
- Model node rectangles as obstacles with padding, then route connectors through free horizontal/vertical corridors.
- First try to eliminate crossings by placing the next main-path node below the decision and placing correction/rework nodes to the side.
- Route rework paths around the outside boundary of the local group, then return to the decision from an unused edge.
- Avoid long horizontal connector runs across more than two lanes through a dense node band; break them into outside corridors or reposition nodes.
- If a clean route is not possible with current coordinates, move nodes. Do not accept crossed lines as a compromise.

## Validation

- Run `scripts/lint_svg_links.py` on generated HTML before visual review.
- Treat any diagonal, crossing, or overlapping `.link` segment as a generation bug, not as an acceptable style variant.
- If the linter reports a diagonal, rewrite that connector with a right-angle route.
- If the linter reports a crossing or overlap, move the connector to a separate corridor or reposition nodes.

## Procurement/Inventory Flow Semantics

- Requisition, replenishment, new-item, or promotion demand can trigger inquiry/quotation.
- Procurement specialist creates inquiry/quotation documents; procurement manager approval should be explicit.
- Supplier admission and order approval should be modeled as separate decisions if both exist.
- Reconciliation is not payment. Reconciliation verifies supplier bills, receiving records, invoices, deductions, and payable amount.
- Payment should occur after reconciliation and any required payment approval.
- Reconciliation differences may be handled collaboratively when the workflow needs traceability; if the target artifact is simplified, model it as a difference-handling loop back to reconciliation.

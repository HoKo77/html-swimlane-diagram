# Process Extraction Guide

Use this guide when the source process is Markdown, Mermaid, rough notes, incomplete, or role ownership is ambiguous. For clear sources, use the core workflow in `SKILL.md` without loading every detail here.

## Research-First Rule For Underspecified Requests

If the user does not specify roles, process steps, approvals, or branch handling, research the domain before drafting the swimlane diagram. Do not fill the gaps only from general memory.

Use browser/search tools to find credible references for the requested process domain. Prioritize:

1. Official ERP/vendor documentation or help centers.
2. Company SOPs, procurement/inventory/accounting process references, or implementation guides.
3. Standards, audit/control guidance, or high-quality industry explanations.

Avoid basing the diagram on a single low-quality SEO article. If sources disagree, choose a conservative common workflow and label it as a researched draft.

For each researched workflow, extract:

- Candidate lanes and their lane dimension.
- Ordered phases.
- Actions owned by each lane.
- Approval, validation, comparison, and audit points.
- `Y/N` branch outcomes.
- Rework loops and resubmission points.
- Final state or downstream process.

Before drawing, create a compact research summary for yourself. When delivering the file, briefly state that roles/process were based on researched defaults if the user did not provide their own.

## Inputs

Possible inputs include Markdown notes, Mermaid sequence diagrams, existing HTML diagrams, screenshots, interview portfolio documents, or rough business process descriptions.

## Extraction Checklist

1. Identify the lane dimension before identifying lanes. Common dimensions include roles/organizations, systems/modules, locations, teams, or environments.
2. Keep all lanes in one dimension. Do not mix people/departments with systems/platforms in the same lane set.
3. If the source contains mixed participants, decide what the diagram is explaining:
   - If it explains accountability, approvals, manual work, or business handoffs, use role/organization lanes and put systems inside action labels.
   - If it explains integration, automation, data movement, or platform boundaries, use system/module lanes and put human roles inside action labels.
4. Identify all lanes after the dimension is chosen. Preserve source lanes when they already share the same dimension.
5. Identify phases. Phases should group the flow without hiding steps.
6. Convert each message or bullet into an action owned by one lane.
7. Mark approvals, audits, validations, and comparisons as decisions if they can pass/fail.
8. Add `Y/N` branches for each decision.
9. Add correction/rework loops for rejected approvals.
10. Distinguish exception handling from the main path.
11. Preserve every source step unless it is a duplicate wording of the same action.
12. Before drawing, produce a compact ordered outline and compare it against the source.

## Lane Dimension Examples

When lane dimension is unclear, load `lane_dimension_examples.md`. Use those examples as pattern guidance, not as fixed lane templates.

## Role Governance

Use this section only when the chosen lane dimension is role/organization.

- Apply maker/checker separation.
- Specialists/operators own preparation, configuration, submission, adjustment, and execution tasks.
- Supervisors/managers/reviewers own approval, review, audit, risk-control, finance approval, and rejection decisions.
- Do not place an approval diamond in the same lane as the specialist who submitted the item unless the source explicitly says it is self-approval.
- If a submission role exists but the approval role is missing, infer a draft checker lane from the same responsibility area and ask for confirmation.
- If the responsibility area is unclear, use a neutral reviewer lane label and mark it for user confirmation.
- If several approvals are domain-specific, keep them separate by responsibility area instead of merging them into one generic approval lane.

## Confirmation Gates

Use two confirmation gates for underspecified work:

1. **Lane confirmation**
   - If lanes are provided by the user or source document and share one dimension, use them directly and mention them briefly.
   - If lanes are mixed across dimensions, normalize them into one dimension before drawing and mention the normalization.
   - If role/organization lanes are not provided, research likely domain roles first, then label them as a researched draft lane list.
   - If approval exists without a supervisor/checker lane, propose one and ask the user to confirm it.
   - If important role ownership is unclear, generate a draft diagram only when useful, then ask the user to confirm or revise the lanes.

2. **Process confirmation**
   - If the source provides an end-to-end process, preserve it.
   - If the source is incomplete, research the missing workflow pattern first, then label the flow as draft.
   - Ask the user to confirm the ordered flow before treating the HTML as final.

Do not block unnecessarily when the user wants momentum. A good default is: create a first draft, then request confirmation of the role list and process outline.

## Mermaid Sequence To Swimlane Mapping

- Participant -> lane.
- Message sender with business responsibility -> action owner.
- Message receiver may become the owner only when the receiver performs the action.
- `alt/else` -> decision diamond with branch labels.
- `loop` -> return connector to the relevant prior decision or task.
- `opt` -> optional branch; label it clearly or include it as a side path.

## Review Questions

- Is any approval missing its rejected path?
- Does each rectangle have a single clear next step?
- Are reconciliation and payment separated?
- Are manager/supervisor review nodes visible where the source mentions them?
- Can a viewer follow the flow without reading the original document?

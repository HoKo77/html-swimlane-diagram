# Lane Dimension Example Library

Use these examples to choose a lane dimension. They are patterns, not prompt templates. Do not copy a lane list unless the user's source actually contains the same actors or systems.

## How To Use

1. Identify what the diagram is meant to explain.
2. Pick one dimension that best explains it.
3. Convert every lane into that dimension.
4. Put other participant types inside node text, not in lane headers.

## Role Or Organization Lanes

Use this when the workflow is about responsibility, approval, accountability, business handoff, or cross-team execution.

Pattern:

- Lanes are people, roles, teams, departments, vendors, or customers.
- Systems appear inside action text.
- Approval diamonds belong to reviewer, manager, compliance, finance, or other checker lanes.

Example lane shape:

- Requesting party
- Operator or specialist
- Reviewer or manager
- External counterparty
- Finance, compliance, warehouse, or another downstream business role

Example node wording:

- Create request in ERP
- Submit RFQ through procurement system
- Review quote comparison
- Supplier returns quote in portal

Example derived from the local inventory/procurement diagram pattern:

- That diagram keeps every lane as a business actor, such as operation, procurement, supplier, warehouse, quality, inventory, and finance roles.
- It does not place ERP, portals, or approval engines as peer lanes.
- Use this as a responsibility-lane pattern only; do not copy its exact lane names unless the user's process has those same actors.

## System Or Module Lanes

Use this when the workflow is about integration, automation, data movement, API boundaries, event routing, or platform ownership.

Pattern:

- Lanes are systems, modules, services, platforms, or databases.
- Human roles appear inside action text.
- Decision diamonds belong to the system or module that evaluates, routes, stores, or enforces the decision.

Example lane shape:

- Source business system
- Workflow or approval engine
- External portal or supplier system
- Master data service
- Notification service
- Reporting or audit store

Example node wording:

- Buyer submits request
- Approval engine routes manager task
- Supplier portal captures quote
- ERP writes selected vendor and price

## Other Homogeneous Dimensions

Use another dimension only when the source clearly centers on that dimension.

Examples:

- Environment lanes: development, staging, production.
- Location lanes: store, regional warehouse, central warehouse.
- Data-state lanes: draft, submitted, approved, posted, archived.

Keep the same rule: do not mix dimensions in lane headers.

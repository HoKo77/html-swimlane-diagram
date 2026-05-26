# Connector Routing Algorithm

Use this approach only for complex diagrams or when connectors cross, overlap, pass through nodes, or fail `scripts/lint_svg_links.py`. For simple diagrams, static orthogonal paths are enough if they pass review.

## Principle

Route connectors only after every node is placed. Treat nodes as fixed obstacles, then calculate orthogonal paths that avoid node interiors and avoid other connectors.

## Data Model

Represent the diagram as structured data before rendering:

```js
const nodes = [
  { id: "submit", lane: 0, x: 90, y: 160, w: 150, h: 58, type: "task" },
  { id: "approve", lane: 2, cx: 560, cy: 260, rx: 58, ry: 52, type: "decision" }
];

const edges = [
  { from: "submit", to: "approve", fromSide: "right", toSide: "left" },
  { from: "approve", to: "fix", label: "N", fromSide: "left", toSide: "right", kind: "reject" },
  { from: "fix", to: "approve", label: "重新提交", fromSide: "right", toSide: "top", kind: "resubmit" }
];
```

Render nodes first. Render links from calculated paths second.

## Routing Steps

0. **Check layout before routing**
   - Main successful path should flow downward.
   - Rework/correction nodes should sit close to the decision that rejected the flow.
   - For resubmission loops, place the correction node adjacent to the decision, preferably immediately left of it.
   - If the graph already requires long cross-lane return lines, change node placement before routing.
   - Add blank routing rows between decision groups when needed.

1. **Build obstacles**
   - Convert each node to a padded rectangle.
   - Use at least 16-24 px padding so arrowheads and labels do not touch nodes.
   - Treat decision diamonds as their bounding boxes for obstacle checks.

2. **Create candidate corridors**
   - Candidate x values: lane boundaries, lane centers, node left/right edges plus padding, outer margins.
   - Candidate y values: row gaps, node top/bottom edges plus padding, phase separators, outer margins.
   - Add extra y corridors above or below dense groups for reject/rework loops.
   - Mark corridors as occupied after selecting a path; later edges should avoid reusing occupied segments unless intentionally merging into the same target.

3. **Generate candidate orthogonal paths**
   - Direct vertical: `M x1 y1 V y2` when same x and no obstacle.
   - Direct horizontal: `M x1 y1 H x2` when same y and no obstacle.
   - One-bend route: `M x1 y1 H midX V y2 H x2` or `M x1 y1 V midY H x2 V y2`.
   - Multi-bend outside route for reject/rework loops: leave source, go to an outer corridor, cross lanes there, then enter target.
   - Compact resubmit route: correction node side/top -> short local vertical/horizontal segment -> decision top/left.
   - Generate several alternatives, not just the shortest path.

4. **Score candidate paths**
   - Reject any path that intersects a padded node box.
   - Reject any path that crosses an existing connector.
   - Penalize shared connector corridors or overlaps.
   - Penalize long horizontal runs through dense node bands.
   - Penalize paths that pass between a node and the node immediately below it on the main spine.
   - Penalize paths that cross lane boundaries more than necessary.
   - Strongly prefer compact `重新提交` routes over large bracket-shaped loops.
   - Prefer fewer bends, shorter length, and branch conventions (`Y` downward, `N` to correction/rework).

5. **Choose path**
   - Pick the lowest-score valid path.
   - If no valid path exists, move nodes or add spacing. Do not accept a crossing route.

6. **Validate**
   - Run `scripts/lint_svg_links.py output.html`.
   - Inspect visually for connector-node collisions that the simple linter cannot see.

## HTML Implementation Pattern

Keep the generated HTML self-contained. It may include inline JavaScript that stores `nodes` and `edges`, computes paths in the browser, then inserts `<path class="link">` elements into the SVG.

Prefer this pattern for complex diagrams:

```js
const routedEdges = routeEdges(nodes, edges);
for (const edge of routedEdges) {
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("class", "link");
  path.setAttribute("d", edge.d);
  svg.appendChild(path);
}
```

For simple diagrams, precomputed static SVG paths are acceptable only if they pass the linter and visual QA.

## Hard Rules

- Do not route before all nodes exist.
- Do not draw a connector through a node.
- Do not accept crossed connectors.
- Do not stack separate connectors on the same line segment.
- Do not fix routing by changing business logic. Fix node placement or routing corridors.
- If the route looks like a large bracket around unrelated nodes, revisit the process layout first.
- For rejected approvals that return to the same decision, prefer a compact `重新提交` loop unless the user explicitly wants a wider process loop.

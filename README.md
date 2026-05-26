# HTML Swimlane Diagram · 可编辑 HTML 泳道图 Skill

> English version: [README.en.md](README.en.md)

一个适配 Codex / Claude Code / Cursor 等 Agent 环境的泳道图技能，用于把业务流程、审批流、系统流程或粗略笔记转换成**单文件 HTML/SVG 泳道图**。

它的目标不是生成一张不可编辑的截图，而是生成一个可以直接打开、复制、修改、检查连线质量的 `.html` 文件。

## 效果

- 固定泳道布局：角色/组织、系统/模块或其他单一维度，避免混乱泳道
- 阶段分区：左侧阶段栏 + 顶部 sticky 泳道表头，适合长流程
- 决策分支：审批/判断节点使用菱形，并保留 `Y/N` 分支
- 返工闭环：拒绝、异常、补充材料等分支使用局部回路
- 正交箭头：连接线只走水平/垂直路径，避免斜线和随意穿插
- 可验证输出：内置 Python linter 检查 SVG 连线交叉、重叠和斜线
- 单文件交付：输出 HTML 内联 CSS/SVG，无需构建、无需服务器

## 适合 / 不适合

适合：

- 商城后台、ERP、CRM、OA 等后台业务流程
- 审批流、采购流、库存流、营销活动流、工单流
- 需要明确“谁负责什么”的角色泳道图
- 需要说明系统边界、模块交互、数据流转的系统泳道图
- 面试作品集、产品方案、需求评审、SOP 梳理

不适合：

- 超大规模 BPMN 建模和仿真
- 需要多人实时协作编辑的专业流程图平台
- 高度自由的美术海报或复杂信息图
- 必须导出 Visio、Draw.io、Figma 源文件的场景

## 安装

### 方式一：通过 Skill Installer

```bash
$skill-installer install https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram
```

安装后如果没有立即出现，请重启 Codex。

### 方式二：让 AI Agent 帮你安装

把下面这段发给有 shell 权限的 Codex / Claude Code / Cursor：

```text
请帮我安装 html-swimlane-diagram skill：
1. 确保本地 Codex skills 目录存在。
2. 从 https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram 安装 skill。
3. 验证安装目录里包含 SKILL.md、assets/、references/、scripts/。
4. 告诉我安装结果。
```

## 如何触发

安装后，可以这样说：

```text
使用 $html-swimlane-diagram 帮我生成一个商城后台营销活动的泳道图
```

更多触发示例：

- `用 $html-swimlane-diagram 把这个采购审批流程画成泳道图`
- `生成一个角色泳道图，展示工单从提交到关闭的流程`
- `把这段 Mermaid sequence diagram 转成可编辑 HTML 泳道图`
- `画一个系统模块泳道图，展示订单、库存、支付、通知之间的流转`

## 工作流

这个 skill 会按固定流程执行：

1. 理解输入：识别流程目标、阶段、动作、审批、分支和终态
2. 选择泳道维度：角色/组织、系统/模块，或其他同质维度
3. 补齐缺口：当用户没有给完整流程时，先查资料形成调研草案
4. 放置节点：先排完所有节点，再处理连线
5. 路由箭头：使用水平/垂直路径，处理 `Y/N` 和返工回路
6. 运行校验：用脚本检查连线斜线、交叉和重叠
7. 交付 HTML：只输出一个可编辑 `.html` 文件

## 目录结构

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
        ├── agents/
        │   └── openai.yaml
        ├── assets/
        │   └── swimlane-template.html
        ├── references/
        │   ├── lane_dimension_examples.md
        │   ├── process_extraction.md
        │   ├── routing_algorithm.md
        │   └── swimlane_rules.md
        └── scripts/
            └── lint_svg_links.py
```

## 示例

本仓库提供了一个商城后台营销活动示例：

- 输入说明：[examples/mall-marketing-workflow.md](examples/mall-marketing-workflow.md)
- 生成结果：[examples/mall-marketing-swimlane.html](examples/mall-marketing-swimlane.html)

你可以直接用浏览器打开 HTML 文件。

## 质量检查

检查示例泳道图连线：

```bash
python3 skills/html-swimlane-diagram/scripts/lint_svg_links.py examples/mall-marketing-swimlane.html
```

检查仓库结构和示例输出：

```bash
python3 scripts/validate_repo.py
```

GitHub Actions 会在 push 和 pull request 时自动执行同样的仓库校验。

## 设计原则

- 一个图只选一种泳道维度，不混用角色和系统
- 审批节点放在审核/主管/系统决策方泳道，不放在提交人泳道
- 先确定业务节点，再画连线
- 返工路径尽量局部闭环，不绕过半张图
- 生成的图必须可读、可编辑、可校验

## License

MIT. See [LICENSE](LICENSE) and [skills/html-swimlane-diagram/LICENSE.txt](skills/html-swimlane-diagram/LICENSE.txt).

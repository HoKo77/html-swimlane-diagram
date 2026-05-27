# HTML Swimlane Diagram Skills

![Skill](https://img.shields.io/badge/Skill-Codex-315596)
![Output](https://img.shields.io/badge/Output-HTML%20%2F%20SVG-416bb3)
![License](https://img.shields.io/badge/License-MIT-green)

```text
HTML Swimlane Diagram
├─ 可编辑单文件 HTML/SVG
├─ 角色 / 系统泳道
├─ Y/N 决策分支
├─ 正交箭头与返工回路
└─ 内置连线校验脚本
```

> English version: [README.en.md](README.en.md)

面向 Codex 等 Agent 环境的泳道图技能包。它把业务流程、审批流、系统流程、Mermaid 片段或粗略笔记转换成**可编辑的单文件 HTML/SVG 泳道图**。

这个项目的重点是：让 Agent 不只是“画一张图”，而是按稳定规则完成流程抽取、泳道归一、节点排布、箭头路由和连线校验。

## Skills

| Skill | 用途 | 输出 | 风险等级 |
| --- | --- | --- | --- |
| `html-swimlane-diagram` | 生成或优化泳道图，适合业务流程、审批流、系统流程、SOP、产品方案 | 单个 `.html` 文件，内联 SVG/CSS | Low：本地文件生成，无外部服务依赖 |

## Agent Quick Reference

给 Agent 的最短使用方式：

```text
使用 $html-swimlane-diagram 帮我生成一个商城后台营销活动的泳道图
```

推荐输入里包含：

- 流程主题：例如商城营销活动、采购审批、库存调拨、工单处理
- 泳道偏好：角色/组织泳道，或系统/模块泳道
- 关键节点：发起、配置、审核、发布、监控、复盘
- 决策点：是否通过、是否异常、是否需要返工
- 输出要求：生成一个可编辑 HTML 文件

如果你没有完整流程，也可以只给领域主题。skill 会先调研常见流程，再生成标注为草案的第一版。

## What You Get

- **固定泳道**：只选一种泳道维度，避免把人、部门、系统混成同级泳道
- **阶段分区**：左侧阶段栏 + 顶部 sticky 泳道表头，长流程也能读
- **决策节点**：审批、判断、异常处理使用菱形，并保留 `Y/N`
- **返工闭环**：拒绝、异常、补充材料等分支就近回到对应节点
- **正交箭头**：SVG 连线只走水平/垂直路径
- **质量校验**：内置 linter 检查斜线、交叉和重叠
- **单文件交付**：HTML 内联 CSS/SVG，无需构建、无需服务器

## Install

### Skill Installer

```bash
$skill-installer install https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram
```

安装后如果没有立即出现，请重启 Codex。

### Manual / Agent-Assisted Install

把下面这段发给有 shell 权限的 Agent：

```text
请帮我安装 html-swimlane-diagram skill：
1. 确保本地 Codex skills 目录存在。
2. 从 https://github.com/<your-github-username>/html-swimlane-diagram/tree/main/skills/html-swimlane-diagram 安装 skill。
3. 验证安装目录里包含 SKILL.md、agents/、assets/、references/、scripts/。
4. 运行示例校验脚本，告诉我安装结果。
```

## Example Prompts

```text
使用 $html-swimlane-diagram 帮我生成一个商城后台营销活动的泳道图
```

```text
用 $html-swimlane-diagram 把这个采购审批流程画成角色泳道图：
需求部门提交采购申请 -> 采购询价 -> 主管审核 -> 财务审核 -> 下单 -> 收货 -> 对账付款
```

```text
用 $html-swimlane-diagram 生成一个系统模块泳道图，展示订单、库存、支付、通知之间的流转。
```

## How It Works

```text
输入流程
  ↓
理解与调研
  ↓
选择泳道维度
  ↓
放置节点
  ↓
路由正交连线
  ↓
运行 SVG link linter
  ↓
交付单文件 HTML
```

关键规则：

- 一个图只选一种泳道维度
- 角色泳道中，审批节点放在审核方，不放在提交方
- 系统泳道中，判断节点放在拥有规则或数据的系统
- 先完整放置节点，再绘制箭头
- 拒绝和异常分支优先使用局部返工回路

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

## Included Example

- 输入说明：[examples/mall-marketing-workflow.md](examples/mall-marketing-workflow.md)
- 生成结果：[examples/mall-marketing-swimlane.html](examples/mall-marketing-swimlane.html)

浏览器直接打开 `examples/mall-marketing-swimlane.html` 即可查看。

## Validation

检查示例泳道图连线：

```bash
python3 skills/html-swimlane-diagram/scripts/lint_svg_links.py examples/mall-marketing-swimlane.html
```

检查仓库结构和示例输出：

```bash
python3 scripts/validate_repo.py
```

GitHub Actions 会在 push 和 pull request 时自动执行校验。

## Scope

适合：

- 后台业务流程、审批流、工单流、采购流、库存流、营销活动流
- 产品方案、需求评审、SOP、面试作品集
- 需要可编辑 HTML 文件，而不是一次性截图的场景

不适合：

- 超大规模 BPMN 建模和仿真
- 多人实时协作流程图平台
- 必须导出 Visio、Draw.io、Figma 源文件的场景

## License

MIT. See [LICENSE](LICENSE) and [skills/html-swimlane-diagram/LICENSE.txt](skills/html-swimlane-diagram/LICENSE.txt).

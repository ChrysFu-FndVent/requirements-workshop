<a id="readme-top"></a>

<div align="center">

# Requirements Workshop

**Turn ambiguous requests into user-confirmed delivery boundaries before Codex starts building.**

<img src="assets/readme/requirements-workshop-banner.svg" alt="Requirements Workshop: clarify, confirm, then build" width="100%" />

[![CI](https://img.shields.io/github/actions/workflow/status/ChrysFu-FndVent/requirements-workshop/ci.yml?branch=main&style=flat)](https://github.com/ChrysFu-FndVent/requirements-workshop/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/ChrysFu-FndVent/requirements-workshop?style=flat)](https://github.com/ChrysFu-FndVent/requirements-workshop/releases)
[![License](https://img.shields.io/github/license/ChrysFu-FndVent/requirements-workshop?style=flat)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/ChrysFu-FndVent/requirements-workshop?style=flat)](https://github.com/ChrysFu-FndVent/requirements-workshop/search?l=Python)
[![Stars](https://img.shields.io/github/stars/ChrysFu-FndVent/requirements-workshop?style=flat)](https://github.com/ChrysFu-FndVent/requirements-workshop/stargazers)

</div>

<div align="right"><a href="#简体中文">简体中文</a> | <a href="#english">English</a></div>

---

<a id="简体中文"></a>

## 简体中文

<details>
<summary>目录</summary>

- [为什么需要它](#为什么需要它)
- [工作方式](#工作方式)
- [使用前后](#使用前后)
- [安装](#安装)
- [调用与回答](#调用与回答)
- [完整对话样例](#完整对话样例)
- [可选 PRD](#可选-prd)
- [组合工作流](#组合工作流)
- [验证与衡量](#验证与衡量)
- [兼容性](#兼容性)
- [许可证](#许可证)

</details>

### 为什么需要它

`Requirements Workshop` 是一个 Codex Skill 插件。它在规划或实现开始前，通过多轮短问题确认用户、目标、范围、约束、数据、权限、集成和验收标准。

它解决的不是“不会写需求文档”，而是更常见的问题：**模糊请求中的产品决定被实现细节悄悄替代**。Skill 保留对话上下文与已确认的决策记录，降低将长篇需求盘点压缩为一次性表单时遗漏细节的风险。

> 让 Codex 在动手前，把模糊需求变成经过用户确认的实施边界。

适合以下场景：

- 从模糊想法定义一个新产品、应用或 Skill；
- 修改已有功能，但不希望范围扩散到无关模块；
- 接入外部平台，需要确认账号、权限、刷新、失败和合规边界；
- 在实现前获得明确的排除项和可测试验收标准。

### 工作方式

```text
模糊请求
  -> 预计 3-5 轮聚焦问题
  -> 用户用 1B、2D、3A 快速回答
  -> Confirmed so far 持续记录决定
  -> 汇总范围、排除项、验收标准和风险
  -> 用户补充或最终确认
  -> 回到原先授权的规划或实现任务
```

每轮只询问 1-4 个高价值问题，并显示 `第 x 轮/共 y 轮：主题`。预计轮数发生变化时，Codex 会先解释原因。到达预计轮数不代表自动开工；必须先出现：

```text
基本需求已确认完毕。请确认是否还有需要补充的需求？
```

### 使用前后

| 直接从模糊请求编码 | 使用 Requirements Workshop |
|---|---|
| 输入、用户和权限由实现者猜测 | 用户逐项确认输入、角色与授权边界 |
| “完成”通常只有功能描述 | 形成可测试的验收标准 |
| 新想法容易混入首版 | 明确首版、未来范围和排除项 |
| 失败处理在开发中临时决定 | 在实现前确认失败、刷新与数据保留策略 |
| 返工原因难以追溯 | `Confirmed so far` 保留决策来源 |

查看可复现的[同一个模糊请求：直接编码 vs Requirements Workshop](docs/direct-coding-vs-workshop.md)。该对比用于展示决策时机，不宣称未经测量的效率提升。

### 安装

仓库自带 Codex marketplace 清单。克隆后执行：

```sh
git clone https://github.com/ChrysFu-FndVent/requirements-workshop.git
cd requirements-workshop
codex plugin marketplace add "$PWD"
codex plugin add requirements-workshop@requirements-workshop-marketplace
```

安装后开启一个新的 Codex 任务，使插件 Skill 被加载。

### 调用与回答

显式调用：

```text
$requirements-workshop:requirements-workshop 帮我梳理一个 AI 求职工作台的需求。
```

自然语言调用：

```text
使用 requirement-workshop 帮我梳理一个 YouTube 视频抓取 skill 的需求
```

问题使用题号和 `A/B/C...` 选项，最后一个选项始终允许自定义补充。回复时无需复制问题：

```text
1B，2D，3A
1E：我希望按频道分别设置刷新频率。
4：首版应在十分钟内完成首次检索。
```

### 完整对话样例

| 场景 | 初始模糊请求 | 最终确认重点 |
|---|---|---|
| [新应用](examples/new-app.md) | “做一个 AI 求职工作台” | 用户、职位来源、数据存储、AI 确认点、首版排除项 |
| [已有功能改造](examples/existing-feature.md) | “给知识库增加共享功能” | 邀请对象、权限、验证、撤销、存量内容迁移 |
| [外部平台集成](examples/external-integration.md) | “抓取 YouTube 视频加入知识库” | 登录前后能力、刷新、去重、失败处理、合规边界 |

三份样例都包含完整四轮问答、`Confirmed so far`、最终确认和使用前后的返工边界差异。

### 可选 PRD

Skill 默认不生成 PRD。只有用户在需求确认后明确要求“生成 PRD”时，才创建 `PRD-[产品名].md`，包含摘要、联系人、背景、目标、市场细分、价值主张、解决方案和发布计划。未确认事实标为 `TBD`，不会重新开启泛泛的需求访谈。

### 组合工作流

Requirements Workshop 可以作为应用生成 Agent 的前置需求入口：先确认页面、数据、权限、集成与验收边界，再将最终确认交给生成、测试和重试流程。

查看 [Requirements Workshop -> text-to-app-agent 工作链](docs/text-to-app-agent-workflow.md)。伴随仓库目前为私有仓库，因此其 GitHub 地址只对已授权用户可见；本仓库没有将它伪装成公开依赖。

### 验证与衡量

本地验证：

```sh
python3 -m unittest discover -s tests -p "test_*.py" -v
```

仓库测试不依赖本机 Skill 安装路径。CI 在 Python 3.11 和 3.12 上验证 Skill 协议、发布元数据、marketplace 路径、许可证和文档证据。项目的[指标手册](docs/metrics.md)定义了安装或克隆量、样例访问、新需求类型和 Stars/独立访问转化的来源与口径；新的需求场景可通过仓库 Issue 表单提交。

### 兼容性

本发布包依赖 Codex 的插件清单、Skill 发现能力和普通对话流，因此不能原样安装到其他 Agent。核心 `SKILL.md` 是可移植的 Markdown 流程，可适配具有类似 Skill 机制的 Agent，但必须改写目标平台的安装、触发和上下文访问方式。

Codex 插件清单当前没有已文档化的全局快捷键或自定义 `/` 命令字段，所以本插件使用 Skill 标识和自然语言触发。

### 许可证

Copyright (c) 2026 Cherys。项目采用 [MIT License](LICENSE)。

<p align="right"><a href="#readme-top">返回顶部</a></p>

---

<a id="english"></a>

## English

<details>
<summary>Table of Contents</summary>

- [Why it exists](#why-it-exists)
- [How it works](#how-it-works)
- [Before and after](#before-and-after)
- [Installation](#installation)
- [Invocation and replies](#invocation-and-replies)
- [Complete dialogue examples](#complete-dialogue-examples)
- [Optional PRD](#optional-prd)
- [Combined workflow](#combined-workflow)
- [Validation and measurement](#validation-and-measurement)
- [Compatibility](#compatibility)
- [License](#license)

</details>

### Why it exists

`Requirements Workshop` is a Codex Skill plugin. Before planning or implementation begins, it uses short multi-turn question batches to confirm users, outcomes, scope, constraints, data, permissions, integrations, and acceptance criteria.

It addresses a more common failure than “not having a requirements document”: **product decisions hidden inside implementation assumptions**. The Skill preserves conversation context and confirmed decisions, reducing detail loss when a long discovery process is compressed into a one-shot form.

> Before Codex starts building, turn an ambiguous request into a user-confirmed delivery boundary.

Use it to:

- define a new product, application, or Skill from a broad idea;
- change an existing feature without expanding into unrelated modules;
- define account, permission, refresh, failure, and compliance boundaries for an integration;
- obtain explicit exclusions and testable acceptance criteria before implementation.

### How it works

```text
Ambiguous request
  -> 3-5 estimated focused rounds
  -> compact replies such as 1B, 2D, 3A
  -> Confirmed so far decision record
  -> scope, exclusions, acceptance criteria, and risk summary
  -> additions or final user confirmation
  -> the originally authorized planning or implementation task
```

Each round asks one to four high-value questions and uses `第 x 轮/共 y 轮：topic`. Codex explains any change to the estimated total. Reaching the estimated round count does not authorize work; the flow first asks:

```text
基本需求已确认完毕。请确认是否还有需要补充的需求？
```

### Before and after

| Coding directly from a vague request | Using Requirements Workshop |
|---|---|
| Inputs, users, and permissions are implementation assumptions | Users confirm inputs, roles, and authorization boundaries |
| “Done” is usually a feature description | Acceptance criteria are testable |
| New ideas can silently enter the first release | First release, future scope, and exclusions are separated |
| Failure handling is decided during development | Failure, refresh, and retention behavior is confirmed first |
| Rework decisions are hard to trace | `Confirmed so far` preserves decision provenance |

See [Direct coding vs. Requirements Workshop](docs/direct-coding-vs-workshop.md) for a reproducible same-request comparison. It demonstrates decision timing and does not claim an unmeasured productivity gain.

### Installation

The repository includes a Codex marketplace manifest. Clone and install it with:

```sh
git clone https://github.com/ChrysFu-FndVent/requirements-workshop.git
cd requirements-workshop
codex plugin marketplace add "$PWD"
codex plugin add requirements-workshop@requirements-workshop-marketplace
```

Start a new Codex task after installation so the Skill is loaded.

### Invocation and replies

Explicit invocation:

```text
$requirements-workshop:requirements-workshop Help me define an AI job-search workbench.
```

Natural-language invocation:

```text
使用 requirement-workshop 帮我梳理一个 YouTube 视频抓取 skill 的需求
```

Questions use numbers and `A/B/C...` choices, always ending with a custom option. Replies can stay compact:

```text
1B，2D，3A
1E：Use a separate refresh schedule for each channel.
4：The first search should complete within ten minutes.
```

### Complete dialogue examples

| Scenario | Initial vague request | Confirmed decisions |
|---|---|---|
| [New application](examples/new-app.md) | “Build an AI job-search workbench” | Users, job sources, storage, AI consent, first-release exclusions |
| [Existing feature change](examples/existing-feature.md) | “Add sharing to the knowledge base” | Invitees, roles, verification, revocation, existing-content migration |
| [External integration](examples/external-integration.md) | “Add YouTube videos to the knowledge base” | Connected/disconnected access, refresh, deduplication, failures, compliance |

Each example contains four complete rounds, `Confirmed so far`, final confirmation, and a before/after rework boundary.

### Optional PRD

The Skill does not generate a PRD by default. Only when the user explicitly asks after confirmation does it create `PRD-[product-name].md` with Summary, Contacts, Background, Objective, Market Segment(s), Value Proposition(s), Solution, and Release. Unknown facts remain `TBD`, and generic discovery is not restarted.

### Combined workflow

Requirements Workshop can serve as the requirements entry point for an application-generation Agent: confirm pages, data, permissions, integrations, and acceptance boundaries before handing the final contract to generation, testing, and retry stages.

See the [Requirements Workshop -> text-to-app-agent workflow](docs/text-to-app-agent-workflow.md). The companion repository is currently private, so its GitHub URL is visible only to authorized users; this repository does not present it as a public dependency.

### Validation and measurement

Local validation:

```sh
python3 -m unittest discover -s tests -p "test_*.py" -v
```

The repository test command does not depend on a machine-specific Skill installation path. CI validates the Skill contract, release metadata, marketplace path, license, and evidence documents on Python 3.11 and 3.12. The [measurement plan](docs/metrics.md) defines sources and interpretation for installs or clones, example engagement, new requirement categories, and Stars/unique-visitor conversion. New scenarios can be submitted through the repository issue form.

### Compatibility

This distribution relies on Codex plugin manifests, Skill discovery, and normal conversation flow, so it cannot be installed unchanged in another Agent. The core `SKILL.md` is a portable Markdown workflow that can be adapted for Agents with a similar Skill mechanism, but the target platform's installation, activation, and context access must be rewritten.

Codex plugin manifests currently expose no documented field for global keybindings or custom `/` commands, so this plugin uses its Skill identifier and natural-language activation.

### License

Copyright (c) 2026 Cherys. Released under the [MIT License](LICENSE).

<p align="right"><a href="#readme-top">Back to top</a></p>

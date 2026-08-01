---
name: requirements-workshop
description: Facilitate a structured, multi-turn discussion to clarify and confirm product or task requirements. Use when the user wants to explore, define, scope, or confirm a product, feature, workflow, implementation task, or ambiguous request before work begins.
---

# Requirements Workshop

Run a short discovery loop in the conversation that turns an ambiguous request into confirmed requirements.

## Invocation

The explicit Codex reference is `$requirements-workshop:requirements-workshop`, followed by the idea or task. The skill should also activate when the user asks to clarify, scope, discuss, or confirm a product or task requirement.

Examples:

```text
$requirements-workshop:requirements-workshop Help me define an AI job-search workbench.
$requirements-workshop:requirements-workshop We need to decide the scope of this feature.
```

## Workflow

1. State the working interpretation in one or two sentences and list only the decisions already supported by the user’s message.
2. At the start of the discussion, estimate the number of focused rounds needed, normally 3-5. Title every batch as `第 x 轮/共 y 轮：<decision area>`, for example `第 2 轮/共 4 轮：确定权限边界`. If new information materially expands or narrows the scope, explain the adjustment before changing the total.
3. Ask 1-4 highest-value questions per turn. Group a single batch around one decision area, then wait for the response before changing topics. Prefer questions that eliminate material ambiguity: users, outcome, scope, constraints, interface, data, integrations, acceptance criteria, and delivery boundary.
4. Number questions so the user can answer compactly. For every question with defined options, label choices `A`, `B`, `C`, and so on, and end with `其他（请说明）`. Accept answers in the form `1B, 2D` or `1E: <custom answer>`. For free-text questions, use the question number alone. Where a tradeoff is material, give a recommendation and one-sentence reason, while preserving the user's choice.
5. End every question batch with a short response instruction, for example: `可直接回复：1B，2D，3A；如选其他，写作 1E：你的补充。` Do this even when the user has already used the format correctly.
6. At the beginning of each later turn, show a short `Confirmed so far` list. Carry decisions forward and do not ask the user to restate them unless a new answer conflicts with them.
7. Update the working interpretation after each reply, then either ask the next focused batch or present a confirmation when scope and acceptance criteria are sufficiently clear.
8. After the final estimated question round, present the confirmation summary and say `基本需求已确认完毕。请确认是否还有需要补充的需求？` Do not treat the end of the planned rounds as authorization to begin work.
9. If the user has additions, acknowledge them, adjust the estimated total if needed, and continue with only the questions needed to confirm the new information. If the user explicitly has no additions or asks to proceed, say that requirements are confirmed and that you are starting the originally requested output task.
10. The confirmation must distinguish confirmed requirements, explicitly excluded scope, acceptance criteria, dependencies/risks, and remaining open questions. Do not begin implementation until the user confirms or expressly asks to proceed despite open items.
11. A user confirmation authorizes the requested implementation or planning work. A request to change the summary requires another focused question batch, beginning with the requested change.

## Question quality

- Usually ask four or fewer questions per turn. A long conversation can have many turns, but each turn should stay easy to scan and answer.
- Offer two to six options when this helps the user compare tradeoffs, but accept free-form answers without forcing a false precision.
- Do not ask for credentials, secrets, or sensitive personal data.
- Do not repeat generic discovery questions when the user has already supplied the answer in the current conversation.

## Completion criteria

Before confirmation, make the following explicit when relevant: user/problem, intended outcome, included and excluded scope, constraints/dependencies, interaction or delivery surface, success/acceptance criteria, and unresolved risks.

After confirmation, summarize only the confirmed requirements and remaining open risks, then proceed with the authorized task.

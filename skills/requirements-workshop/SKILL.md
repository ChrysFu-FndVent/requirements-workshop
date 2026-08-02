---
name: requirements-workshop
description: Facilitate a structured, multi-turn discussion to clarify and confirm product or task requirements. Use when the user wants to explore, define, scope, or confirm a product, feature, workflow, implementation task, or ambiguous request before work begins. After confirmed product or feature requirements, hand the decision record to create-prd to produce a PRD, then use that PRD as the primary source for downstream work.
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
9. If the user has additions, acknowledge them, adjust the estimated total if needed, and continue with only the questions needed to confirm the new information. If the user explicitly has no additions or asks to proceed, say that requirements are confirmed and begin the appropriate confirmed output path.
10. For a product or feature request, invoke `create-prd` after confirmation. Pass it the confirmed decision record and final summary as its input; do not repeat discovery questions that the workshop has already answered. Generate the `create-prd` 8-section Markdown document as `PRD-[product-name].md`. Preserve unknown facts as `TBD` rather than inventing them, especially contacts, market evidence, metrics, and delivery estimates.
11. For a non-product task, continue with the originally requested implementation or planning output instead of forcing a PRD.
12. The confirmation must distinguish confirmed requirements, explicitly excluded scope, acceptance criteria, dependencies/risks, and remaining open questions. Do not begin implementation until the user confirms or expressly asks to proceed despite open items.
13. A user confirmation authorizes the requested implementation or planning work. A request to change the summary requires another focused question batch, beginning with the requested change.

## PRD handoff

When invoking `create-prd`, provide a compact handoff containing: product or feature name, summary, user/problem, objectives and measurable outcomes, target segments, value propositions, in-scope and excluded capabilities, UX or workflow decisions, relevant technology/integrations, assumptions, dependencies/risks, and first-release versus future-release scope.

Use the `create-prd` section order: Summary, Contacts, Background, Objective, Market Segment(s), Value Proposition(s), Solution, and Release. Mark details that were not confirmed during discovery as `TBD`; do not manufacture stakeholder names, customer research, competitive claims, dates, or metrics. The PRD is the product-requirements output of this combined workflow, not permission to begin implementation unless the user has also requested it.

## Downstream source order

For downstream planning, design, implementation, review, or other product work, read the generated PRD first and treat it as the primary requirements source. When the PRD lacks a decision rationale, option tradeoff, exception, or implementation-relevant detail, review the complete `requirements-workshop` discussion in the current Codex task before asking the user again.

Apply this precedence: a later explicit user instruction overrides the PRD; the PRD overrides earlier workshop summaries; the full workshop record supplies supporting detail and rationale. If the record resolves the issue, proceed without reopening discovery. If neither the PRD nor the available workshop record resolves it, ask one focused follow-up question and update the PRD after confirmation.

Only claim to have reviewed the full workshop record when it is available in the current task context. In a new task where the prior conversation is unavailable, request the original discussion record or its accessible link; do not infer missing details from the PRD.

## Question quality

- Usually ask four or fewer questions per turn. A long conversation can have many turns, but each turn should stay easy to scan and answer.
- Offer two to six options when this helps the user compare tradeoffs, but accept free-form answers without forcing a false precision.
- Do not ask for credentials, secrets, or sensitive personal data.
- Do not repeat generic discovery questions when the user has already supplied the answer in the current conversation.

## Completion criteria

Before confirmation, make the following explicit when relevant: user/problem, intended outcome, included and excluded scope, constraints/dependencies, interaction or delivery surface, success/acceptance criteria, and unresolved risks.

After confirmation, summarize only the confirmed requirements and remaining open risks, then proceed with the authorized task.

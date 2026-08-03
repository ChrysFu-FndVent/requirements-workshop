---
name: requirements-workshop
description: Facilitate a structured, multi-turn discussion to clarify and confirm product or task requirements. Use when the user wants to explore, define, scope, or confirm a product, feature, workflow, implementation task, or ambiguous request before work begins. Generate a PRD only when the user explicitly requests one after requirements are confirmed.
---

# Requirements Workshop

Run a short discovery loop in the conversation that turns an ambiguous request into confirmed requirements.

## Invocation

Use `$requirements-workshop:requirements-workshop`, followed by the idea or task. Also activate when the user asks to clarify, scope, discuss, or confirm a product or task requirement.

Examples:

```text
$requirements-workshop:requirements-workshop Help me define an AI job-search workbench.
$requirements-workshop:requirements-workshop We need to decide the scope of this feature.
```

## Workflow

1. State the working interpretation in one or two sentences and list only the decisions already supported by the user's message.
2. Estimate the number of focused rounds needed, normally 3-5. Title every batch as `第 x 轮/共 y 轮：<decision area>`. Explain any material change before adjusting the total.
3. Ask 1-4 highest-value questions per turn. Group each batch around one decision area, then wait for the response. Prioritize user, outcome, scope, constraints, interface, data, integrations, acceptance criteria, and delivery boundary.
4. Number questions. For defined options, label choices `A`, `B`, `C`, and so on, ending with `其他（请说明）`. Accept `1B, 2D`, `1E: <custom answer>`, or a numbered free-text response. Give a recommendation and a one-sentence reason when a material tradeoff exists, while preserving the user's choice.
5. End every batch with a compact reply instruction such as `可直接回复：1B，2D，3A；如选其他，写作 1E：你的补充。`
6. Begin every later turn with a short `Confirmed so far` list. Carry decisions forward and do not ask the user to restate them unless a new answer conflicts with them.
7. Update the working interpretation after each reply, then ask the next focused batch or present the confirmation summary.
8. After the final estimated round, present the summary and say `基本需求已确认完毕。请确认是否还有需要补充的需求？` Do not treat the end of the estimated rounds as authorization to begin work.
9. If the user adds requirements, adjust the estimate if needed and ask only the questions required to confirm the additions. If the user has no additions or asks to proceed, state that requirements are confirmed and start the originally requested planning or implementation output.
10. Generate a PRD only when the user explicitly requests one after confirmation. Create `PRD-[product-name].md` with Summary, Contacts, Background, Objective, Market Segment(s), Value Proposition(s), Solution, and Release. Use confirmed information, mark missing facts as `TBD`, and do not restart discovery.
11. Without an explicit PRD request, carry the confirmed requirements directly into the user's authorized task.
12. Distinguish confirmed requirements, excluded scope, acceptance criteria, dependencies or risks, and remaining open questions. Do not begin implementation until the user confirms or expressly asks to proceed despite open items.

## Question quality

- Ask four or fewer questions per turn unless the user requests a comprehensive batch.
- Offer two to six options when comparison helps, while always accepting free-form answers.
- Do not ask for credentials, secrets, or sensitive personal data.
- Do not repeat questions already answered in the current conversation.

## Completion criteria

Before confirmation, make explicit when relevant: user and problem, intended outcome, included and excluded scope, constraints and dependencies, interaction or delivery surface, acceptance criteria, and unresolved risks.

After confirmation, summarize only confirmed requirements and remaining open risks, then proceed with the authorized task. Generate a PRD only when explicitly requested.

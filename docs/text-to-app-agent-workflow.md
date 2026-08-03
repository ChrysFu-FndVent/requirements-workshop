# Requirements Workshop to text-to-app-agent

This document defines a real handoff contract between this public requirements plugin and the companion `text-to-app-agent` workflow.

> The companion repository is currently private. Its GitHub URL is accessible only to authorized users: https://github.com/ChrysFu-FndVent/text-to-app-agent

## Workflow

```text
Ambiguous app request
  -> Requirements Workshop
  -> confirmed user, page, data, permission, integration, and acceptance boundaries
  -> explicit user approval
  -> text-to-app-agent planning and generation
  -> tests and retry loop
```

## Handoff contract

Before starting the app-generation workflow, carry forward:

- target users and the job they need to complete;
- first-release pages and explicitly excluded pages;
- entities, ownership, retention, and sensitive-data constraints;
- roles, permissions, authentication, and external account behavior;
- integrations, failure modes, refresh rules, and rate limits;
- acceptance criteria and unresolved risks;
- the user's final confirmation.

Do not pass exploratory options as confirmed requirements. If the app-generation workflow discovers a material contradiction or missing boundary, return to one focused Requirements Workshop round, update the confirmation summary, and ask for approval again.

## Example invocation

```text
$requirements-workshop:requirements-workshop 帮我明确这个应用的页面、数据、权限和验收边界；确认后再交给 app 生成流程。
```

The [new application example](../examples/new-app.md) demonstrates the upstream conversation. The generated application workflow should treat its final confirmation as the delivery contract.

# Example: Change an existing feature

This example clarifies a sharing feature for an existing knowledge-base product without redesigning the rest of the application.

## Initial request

**User**

> 使用 requirement-workshop 帮我梳理“给现有知识库增加共享功能”的需求。

## 第 1 轮/共 4 轮：共享对象与目标

**Codex**

1. 谁可以发起共享？
   A. 任何成员
   B. 内容创建者
   C. 工作区管理员
   D. B 和 C
   E. 其他（请说明）
2. 首版共享给谁？
   A. 同一工作区成员
   B. 受邀邮箱
   C. 拥有链接的任何人
   D. A、B、C
   E. 其他（请说明）
3. 最重要的使用场景是什么？
   A. 只读审阅
   B. 协作编辑
   C. 评论反馈
   D. 对外发布
   E. 其他（请说明）

可直接回复：1D，2B，3C；如选其他，写作 1E：你的补充。

**User**

> 1D，2B，3C

## 第 2 轮/共 4 轮：权限模型

**Codex**

Confirmed so far:

- 发起者：内容创建者或管理员
- 接收者：受邀邮箱
- 场景：评论反馈

1. 首版权限级别有哪些？
   A. 查看
   B. 查看和评论
   C. 查看、评论和编辑
   D. 自定义权限
   E. 其他（请说明）
2. 邀请是否需要登录？
   A. 必须注册并登录
   B. 邮箱验证码即可
   C. 无需验证
   D. 由发起者选择
   E. 其他（请说明）
3. 谁可以撤销访问？
   A. 发起者
   B. 管理员
   C. A 和 B
   D. 任何编辑者
   E. 其他（请说明）

可直接回复：1B，2B，3C；如选其他，写作 1E：你的补充。

**User**

> 1B，2B，3C

## 第 3 轮/共 4 轮：界面与通知

**Codex**

Confirmed so far:

- 权限：查看或评论
- 验证：邮箱验证码
- 撤销：发起者与管理员

1. 共享入口放在哪里？
   A. 文档页顶部工具栏
   B. 侧边栏菜单
   C. 工作区设置
   D. 多处入口
   E. 其他（请说明）
2. 接收者收到什么通知？
   A. 邀请邮件
   B. 站内通知
   C. A 和 B
   D. 不通知
   E. 其他（请说明）
3. 评论通知如何发送？
   A. 每条邮件
   B. 站内实时通知
   C. 每日摘要
   D. B 和可选每日摘要
   E. 其他（请说明）

可直接回复：1A，2C，3D；如选其他，写作 1E：你的补充。

**User**

> 1A，2C，3D

## 第 4 轮/共 4 轮：兼容与验收

**Codex**

Confirmed so far:

- 入口：文档页顶部
- 邀请：邮件与站内通知
- 评论：实时站内通知，可选每日摘要

1. 现有内容默认状态是什么？
   A. 全部私有
   B. 沿用现有权限
   C. 管理员统一设置
   D. 自动对工作区公开
   E. 其他（请说明）
2. 首版验收标准是什么？
   A. 2 分钟内完成邀请
   B. 未授权用户无法访问
   C. 撤销后立即失效
   D. A、B、C 全部满足
   E. 其他（请说明）
3. 哪项明确排除？
   A. 公开匿名链接
   B. 协作编辑
   C. 批量共享
   D. A、B、C
   E. 其他（请说明）

可直接回复：1A，2D，3D；如选其他，写作 1E：你的补充。

**User**

> 1A，2D，3D

## Confirmation

**Codex**

基本需求已确认完毕。

- Confirmed requirements: creator/admin invitations by email, view/comment permissions, email-code verification, toolbar entry, email and in-app invitation notifications, revocation by creator/admin.
- Excluded scope: anonymous public links, collaborative editing, and bulk sharing.
- Acceptance criteria: invite within two minutes, reject unauthorized access, and revoke immediately.
- Migration: all existing content remains private.
- Open questions: none blocking.

请确认是否还有需要补充的需求？

**User**

> 没有，开始修改现有功能。

## Before/after boundary

| From the initial request | After the workshop |
|---|---|
| “共享功能” might trigger public links, editor roles, and a broad permissions migration. | The change is limited to verified invitees with view/comment access; existing content remains private and revocation is testable. |

**English summary:** The workshop isolates the new feature from unrelated permission migration and collaborative editing work.

# Example: Define a new application

This complete example starts from a broad request and ends with a confirmed delivery boundary. The dialogue is intentionally compact; a real workshop may adjust the estimated round count when answers expand the scope.

## Initial request

**User**

> 使用 requirement-workshop 帮我梳理一个 AI 求职工作台的需求。

## 第 1 轮/共 4 轮：用户与核心结果

**Codex**

1. 首版主要服务谁？
   A. 应届毕业生
   B. 有工作经验的求职者
   C. 招聘顾问
   D. 企业招聘团队
   E. 其他（请说明）
2. 用户最重要的结果是什么？
   A. 找到匹配岗位
   B. 生成定制简历
   C. 管理投递流程
   D. A、B、C 都需要
   E. 其他（请说明）
3. 首次使用从哪里开始？
   A. 上传简历
   B. 填写目标岗位
   C. 导入职位链接
   D. 连接招聘网站账号
   E. 其他（请说明）

可直接回复：1B，2D，3A；如选其他，写作 1E：你的补充。

**User**

> 1B，2D，3A

## 第 2 轮/共 4 轮：首版范围

**Codex**

Confirmed so far:

- 用户：有工作经验的求职者
- 核心结果：岗位匹配、定制简历和投递管理
- 首次入口：上传简历

1. 首版职位从哪里获得？
   A. 用户粘贴职位链接
   B. 关键词检索公开职位
   C. 连接招聘平台
   D. A 和 B
   E. 其他（请说明）
2. 定制简历需要输出什么？
   A. 修改建议
   B. 可编辑的新版本
   C. 差异对比与新版本
   D. 只生成求职信
   E. 其他（请说明）
3. 投递管理包含哪些状态？
   A. 待投递、已投递、面试、结束
   B. 用户自定义状态
   C. 看板和提醒
   D. A 和 C
   E. 其他（请说明）

可直接回复：1D，2C，3D；如选其他，写作 1E：你的补充。

**User**

> 1D，2C，3D

## 第 3 轮/共 4 轮：数据与交互边界

**Codex**

Confirmed so far:

- 职位来源：链接导入与公开检索
- 简历输出：差异对比及可编辑版本
- 投递管理：固定状态看板与提醒

1. 简历和职位数据保存在哪里？
   A. 仅本机
   B. 登录后的云端工作区
   C. 用户每次自行选择
   D. 不保存
   E. 其他（请说明）
2. 首版主要界面是什么？
   A. 桌面网页
   B. 移动网页
   C. 原生移动应用
   D. 浏览器扩展
   E. 其他（请说明）
3. AI 修改简历前是否需要确认？
   A. 每条建议确认
   B. 整份预览后确认
   C. 自动覆盖
   D. 只建议、不生成
   E. 其他（请说明）

可直接回复：1B，2A，3B；如选其他，写作 1E：你的补充。

**User**

> 1B，2A，3B

## 第 4 轮/共 4 轮：验收与排除项

**Codex**

Confirmed so far:

- 数据：登录后保存在云端工作区
- 终端：桌面网页
- AI 变更：整份预览后由用户确认

1. 首版成功标准是什么？
   A. 10 分钟内完成首次职位匹配
   B. 15 分钟内生成并确认定制简历
   C. 完成一次投递并进入看板
   D. A、B、C 全部满足
   E. 其他（请说明）
2. 哪些能力明确不进入首版？
   A. 自动代投
   B. 招聘平台私有账号连接
   C. 移动应用
   D. A、B、C
   E. 其他（请说明）

可直接回复：1D，2D；如选其他，写作 1E：你的补充。

**User**

> 1D，2D

## Confirmation

**Codex**

基本需求已确认完毕。

- Confirmed requirements: desktop web app for experienced job seekers; resume upload; public job search and link import; job matching; previewable resume customization; application board and reminders; authenticated cloud workspace.
- Excluded scope: automatic applications, private recruiting-platform account connections, and mobile apps.
- Acceptance criteria: first match within 10 minutes, confirmed tailored resume within 15 minutes, and one tracked application.
- Dependencies and risks: public job-source reliability, personal-data handling, and quality of resume diffs.
- Open questions: none blocking.

请确认是否还有需要补充的需求？

**User**

> 没有，开始输出实施计划。

## Before/after boundary

| From the initial request | After the workshop |
|---|---|
| “AI 求职工作台” could imply an employer ATS, auto-apply bot, mobile app, or scraping platform. | The first release is a desktop applicant workspace with explicit inputs, consent points, acceptance criteria, and excluded integrations. |

**English summary:** The workshop prevents the implementation from drifting into auto-apply, private platform integrations, or mobile delivery before the user has authorized those scopes.

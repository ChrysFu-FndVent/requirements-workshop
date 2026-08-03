# Example: Define an external integration

This example clarifies a YouTube-to-knowledge-base integration, including public/private access, refresh behavior, and failure handling.

## Initial request

**User**

> 使用 requirement-workshop 帮我梳理一个抓取 YouTube 视频并加入知识库的功能。

## 第 1 轮/共 4 轮：输入与核心输出

**Codex**

1. 首版接受哪些输入？
   A. 单个视频链接
   B. 播放列表
   C. 频道
   D. 关键词搜索
   E. A、B、C、D
   F. 其他（请说明）
2. 需要抓取哪些内容？
   A. 标题和描述
   B. 字幕
   C. 章节与时间戳
   D. 缩略图和元数据
   E. A、B、C、D
   F. 其他（请说明）
3. 主要结果是什么？
   A. 对话摘要
   B. Markdown 笔记
   C. 可搜索知识库
   D. 下载视频文件
   E. 其他（请说明）

可直接回复：1E，2E，3C；如选其他，写作 1F：你的补充。

**User**

> 1E，2E，3C

## 第 2 轮/共 4 轮：账号与内容边界

**Codex**

Confirmed so far:

- 输入：视频、播放列表、频道和关键词
- 内容：元数据、字幕、章节、时间戳与缩略图
- 输出：可搜索知识库

1. 未连接 YouTube 账号时允许什么？
   A. 仅公开内容
   B. 禁止使用
   C. 允许用户粘贴任何链接
   D. 使用共享服务账号
   E. 其他（请说明）
2. 连接账号后增加什么？
   A. 私有播放列表和已授权内容
   B. 账号订阅内容
   C. 观看历史
   D. A 和 B
   E. 其他（请说明）
3. 是否保存账号凭据？
   A. 使用平台 OAuth，不保存密码
   B. 保存 Cookie
   C. 要求 API Key
   D. 用户每次重新登录
   E. 其他（请说明）

可直接回复：1A，2D，3A；如选其他，写作 1E：你的补充。

**User**

> 1A，2D，3A

## 第 3 轮/共 4 轮：刷新与订阅

**Codex**

Confirmed so far:

- 未登录：只检索公开内容
- 已登录：可访问获授权的私有播放列表和订阅内容
- 认证：平台 OAuth，不保存密码

1. 默认刷新方式是什么？
   A. 仅手动刷新
   B. 固定间隔自动刷新
   C. 用户为每个来源设定计划
   D. 检测频道更新
   E. 其他（请说明）
2. 删除或下架视频后怎么办？
   A. 立即删除知识库内容
   B. 标记来源不可用，保留已提取文本
   C. 静默保留
   D. 由管理员统一决定
   E. 其他（请说明）
3. 重复视频如何处理？
   A. 按视频 ID 去重并更新
   B. 每次创建副本
   C. 询问用户
   D. 按播放列表分别保存
   E. 其他（请说明）

可直接回复：1C，2B，3A；如选其他，写作 1E：你的补充。

**User**

> 1C，2B，3A

## 第 4 轮/共 4 轮：失败处理与验收

**Codex**

Confirmed so far:

- 刷新：用户按来源设定计划
- 下架：保留文本并标记来源不可用
- 重复：按视频 ID 更新

1. 没有字幕时怎么办？
   A. 仅保存元数据
   B. 尝试语音转录
   C. 直接失败
   D. 询问用户是否转录
   E. 其他（请说明）
2. 首版验收标准是什么？
   A. 公开视频可在 5 分钟内检索
   B. 搜索结果可跳到原时间戳
   C. 登录状态不会扩大未授权访问
   D. A、B、C 全部满足
   E. 其他（请说明）
3. 哪项明确排除？
   A. 下载或重新分发视频文件
   B. 绕过地区、年龄或付费限制
   C. 自动发布内容
   D. A、B、C
   E. 其他（请说明）

可直接回复：1D，2D，3D；如选其他，写作 1E：你的补充。

**User**

> 1D，2D，3D

## Confirmation

**Codex**

基本需求已确认完毕。

- Confirmed requirements: four input modes; searchable metadata, captions, chapters, timestamps, and thumbnails; public-only access when disconnected; OAuth-based authorized access; per-source refresh schedules; ID-based updates; optional transcription prompt.
- Excluded scope: video download or redistribution, access-control bypass, and automatic publishing.
- Acceptance criteria: public videos searchable within five minutes, timestamp deep links, and no expansion of unauthorized access.
- Dependencies and risks: YouTube API quotas, caption availability, OAuth consent, and source removals.
- Open questions: none blocking.

请确认是否还有需要补充的需求？

**User**

> 没有，开始输出技术方案。

## Before/after boundary

| From the initial request | After the workshop |
|---|---|
| “抓取 YouTube 视频” could mean downloading media, bypassing access controls, or indexing only public captions. | The integration indexes authorized text and metadata, defines disconnected/connected behavior, and explicitly excludes media redistribution and access bypass. |

**English summary:** The workshop turns an ambiguous “scraper” into an access-aware indexing integration with explicit refresh, failure, and compliance boundaries.

# Direct coding vs. Requirements Workshop

This is a reproducible comparison scenario, not a measured benchmark. It shows how the same vague request can lead to different delivery boundaries.

## 同一个模糊请求

> 做一个把 YouTube 视频加入知识库的功能。

| Decision | Direct coding may assume | Requirements Workshop confirms |
|---|---|---|
| Input | A single public video URL | Video, playlist, channel, and keyword search |
| Authentication | No login, or an unspecified API key | Public-only while disconnected; OAuth-authorized private and subscription content after connection |
| Content | Downloaded media or captions only | Metadata, captions, chapters, timestamps, and thumbnails; no media redistribution |
| Refresh | One-time import | Per-source schedules and ID-based updates |
| Missing captions | Silent failure | Ask whether to run speech transcription |
| Removed source | Delete everything or ignore it | Preserve extracted text and mark the source unavailable |
| Acceptance | “Import works” | Searchable within five minutes, timestamp deep links, and no unauthorized access expansion |

### Likely rework boundary

Direct coding is not inherently wrong. The risk is that implementation decisions become accidental product decisions. If the user later expects account connection, scheduled refresh, or retained text for removed videos, the data model and background jobs may need redesign.

The workshop moves those decisions before implementation and obtains explicit confirmation. It does not guarantee fewer engineering hours; it makes the source of scope and acceptance decisions inspectable.

## English takeaway

The comparison is about decision timing. Direct coding can silently turn implementation assumptions into product behavior. Requirements Workshop makes access, scope, failure handling, and acceptance criteria explicit before those assumptions harden into architecture.

Use the complete [external integration dialogue](../examples/external-integration.md) to reproduce the workshop path.

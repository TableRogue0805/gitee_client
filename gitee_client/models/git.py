"""Data models for Gitee Git."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 获取 Gitee 指数
class GiteeMetrics(TypedDict, total=False):
    data: str
    total_score: int
    created_at: str
    repo: Optional["ProjectBasic"]



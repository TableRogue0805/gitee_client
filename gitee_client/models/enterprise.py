"""Data models for Gitee Enterprise."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 获取一个企业
class EnterpriseBasic(TypedDict, total=False):
    id: int  # 企业ID
    path: str  # 企业命名空间
    name: str  # 企业名称
    url: str  # 企业地址
    avatar_url: str  # 企业头像地址


# 修改企业成员权限或备注
class EnterpriseMember(TypedDict, total=False):
    url: str
    active: bool
    remark: str
    role: str
    outsourced: bool
    enterprise: Optional["EnterpriseBasic"]
    user: Optional["UserMini"]


# 新建周报
class WeekReport(TypedDict, total=False):
    id: int
    content: str
    content_html: str
    year: int
    month: int
    week_index: int
    week_begin: str
    week_end: str
    created_at: str  # 创建时间
    updated_at: str  # 更新时间
    user: Optional["UserMini"]



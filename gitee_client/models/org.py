"""Data models for Gitee Org."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 创建组织
class Group(TypedDict, total=False):
    id: int
    login: str
    name: str
    url: str
    avatar_url: str
    repos_url: str
    events_url: str
    members_url: str
    description: str
    follow_count: int


class GroupBasic(TypedDict, total=False):
    id: int
    login: str
    name: str
    url: str
    avatar_url: str


# 更新授权用户所管理的组织资料
class GroupDetail(TypedDict, total=False):
    id: int
    login: str
    name: str
    url: str
    avatar_url: str
    repos_url: str
    events_url: str
    members_url: str
    description: str
    follow_count: int
    type: str
    location: str
    email: str
    created_at: str
    html_url: str
    public: bool
    enterprise: str
    members: int
    public_repos: int
    private_repos: int
    owner: Optional["UserMini"]


# 列出指定组织的所有关注者
class GroupFollowers(TypedDict, total=False):
    self: Optional["UserBasic"]
    followed_at: str


# 增加或更新授权用户所管理组织的成员
class GroupMember(TypedDict, total=False):
    url: str
    active: bool
    remark: str
    role: str
    organization_url: str
    organization: Optional["Group"]
    user: Optional["UserMini"]



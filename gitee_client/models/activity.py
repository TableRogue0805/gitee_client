"""Data models for Gitee Activity."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 列出仓库的所有公开动态
class Event(TypedDict, total=False):
    id: str
    type: str
    actor: Optional["UserMini"]
    repo: Optional["ProjectMini"]
    org: Optional["GroupBasic"]
    public: bool
    created_at: str
    payload: dict  # 不同类型动态的内容


# 获取一条私信
class UserMessage(TypedDict, total=False):
    id: int
    sender: Optional["UserBasic"]  # 发送者
    unread: bool
    content: str
    updated_at: str
    url: str
    html_url: str


# 列出授权用户的所有私信
class UserMessageList(TypedDict, total=False):
    total_count: int
    list: Optional[list["UserMessage"]]  # 私信列表


# 获取一条通知
class UserNotification(TypedDict, total=False):
    id: int
    content: str
    type: str
    unread: bool
    mute: bool
    updated_at: str
    url: str
    html_url: str
    actor: Optional["UserBasic"]  # 通知发送者
    repository: Optional["ProjectBasic"]
    subject: Optional["UserNotificationSubject"]  # 通知直接关联对象
    namespaces: Optional[list["UserNotificationNamespace"]]  # 通知次级关联对象


# 获取授权用户的通知数
class UserNotificationCount(TypedDict, total=False):
    total_count: int  # 通知总数
    notification_count: int  # 通知数量
    message_count: int  # 私信数量


# 列出授权用户的所有通知
class UserNotificationList(TypedDict, total=False):
    total_count: int
    list: Optional[list["UserNotification"]]  # 通知列表


class UserNotificationNamespace(TypedDict, total=False):
    name: str
    html_url: str
    type: str


class UserNotificationSubject(TypedDict, total=False):
    title: str
    url: str
    latest_comment_url: str
    type: str



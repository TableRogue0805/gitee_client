"""Data models for Gitee Issue."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 搜索 Issues
class Issue(TypedDict, total=False):
    id: int
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    html_url: str
    parent_url: str
    number: str  # 唯一标识
    parent_id: int  # 上级 id
    depth: int  # 所在层级
    state: str  # 状态
    title: str  # 标题
    body: str  # 描述
    body_html: str  # 描述 html 格式
    user: Optional["UserBasic"]  # 作者
    labels: Optional[list["Label"]]  # 标签
    assignee: Optional["UserBasic"]  # 负责人
    collaborators: Optional[list["UserBasic"]]  # 协作者
    repository: Optional["Project"]  # 关联的仓库
    milestone: Optional["Milestone"]  # 关联的里程碑
    created_at: str  # 创建时间
    updated_at: str  # 更新时间
    plan_started_at: str  # 计划开始时间
    deadline: str  # 结束时间
    finished_at: str  # 完成时间
    scheduled_time: int  # 预计工期
    comments: int  # 评论数量
    priority: int  # 优先级(0: 不指定 1: 不重要 2: 次要 3: 主要 4: 严重)
    issue_type_detail: Optional["IssueType"]  # 任务类型详情
    program: Optional["ProgramBasic"]  # 关联的项目
    security_hole: bool  # 是否为私有issue
    cve_id: str  # CVE identifier for security issues
    issue_state_detail: Optional["IssueState"]  # 任务类型详情
    branch: str  # 关联分支


class IssueState(TypedDict, total=False):
    id: int  # 状态 ID
    title: str  # 状态的名称
    color: str  # 状态的颜色
    icon: str  # 任务状态的 Icon
    command: str  # 任务状态的 指令
    serial: int  # 任务状态的 排序
    created_at: str  # 任务状态创建时间
    updated_at: str  # 任务状态更新时间


class IssueType(TypedDict, total=False):
    id: int  # 任务类型 ID
    title: str  # 任务类型的名称
    template: str  # 任务类型模板
    ident: str  # 唯一标识符
    color: str  # 颜色
    is_system: bool  # 是否系统默认类型
    created_at: str  # 任务类型创建时间
    updated_at: str  # 任务类型更新时间


# 更新仓库里程碑
class Milestone(TypedDict, total=False):
    url: str
    html_url: str
    number: int
    repository_id: int
    state: str
    title: str
    description: str
    updated_at: str
    created_at: str
    open_issues: int
    closed_issues: int
    due_on: str



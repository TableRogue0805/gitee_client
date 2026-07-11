"""Data models for Gitee Common."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


class BotInfo(TypedDict, total=False):
    bot_type: str  # 机器人类型
    status: int  # 状态：1-活跃 2-暂停 3-禁用


class GitUser(TypedDict, total=False):
    name: str
    email: str
    date: str


# 获取授权用户的一个 Namespace
class Namespace(TypedDict, total=False):
    id: int  # namespace id
    type: str  # namespace 类型，企业：Enterprise，组织：Group，用户：null
    name: str  # namespace 名称
    path: str  # namespace 路径
    enterprise_id: int  # 所属企业ID，0表示不属于企业
    html_url: str  # namespace 地址
    parent: Optional["NamespaceMini"]


class NamespaceMini(TypedDict, total=False):
    id: int  # namespace id
    type: str  # namespace 类型，企业：Enterprise，组织：Group，用户：null
    name: str  # namespace 名称
    path: str  # namespace 路径
    enterprise_id: int  # 所属企业ID，0表示不属于企业
    html_url: str  # namespace 地址


# 获取企业某个Issue所有评论
class Note(TypedDict, total=False):
    id: int
    body: str
    body_html: str
    user: Optional["UserBasic"]
    source: str
    target: dict
    created_at: str
    updated_at: str
    in_reply_to_id: int
    in_reply_to_user: Optional["UserBasic"]


# 获取某个Pull Request的操作日志
class OperateLog(TypedDict, total=False):
    id: int
    icon: str  # 图标
    user: Optional["UserBasic"]  # 操作者
    target: dict  # 被操作者
    content: str  # 操作描述
    link_target: dict  # 关联对象
    created_at: str  # 操作日志产生时间
    action_type: str  # 动作
    before_change_value: str  # 修改前的值
    after_change_value: str  # 修改后的值
    before_change_id: int  # 修改之前的对象ID
    after_change_id: int  # 修改之后的对象ID


class ProgramBasic(TypedDict, total=False):
    id: int  # 项目id
    name: str  # 项目名称
    description: str  # 项目描述
    assignee: Optional["UserBasic"]  # 项目负责人
    author: Optional["UserBasic"]  # 项目创建者


# 替换所有仓库标签
class ProjectLabel(TypedDict, total=False):
    id: int
    name: str
    ident: str


# 获取一个公钥
class SSHKey(TypedDict, total=False):
    id: int
    key: str
    url: str
    title: str
    created_at: str


# 列出指定用户的所有公钥
class SSHKeyBasic(TypedDict, total=False):
    id: int
    key: str


# 搜索用户
class User(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    member_role: str
    blog: str
    weibo: str
    bio: str
    public_repos: int
    public_gists: int
    followers: int  # 关注用户的人数
    following: int  # 用户关注的人数
    stared: int  # 用户收藏仓库数
    watched: int  # 用户关注仓库数
    created_at: str
    updated_at: str


class UserAssignee(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    member_role: str
    assignee: bool  # 是否默认指派审查
    code_owner: bool  # 是否CodeOwner指派审查
    accept: bool  # 是否审查通过


# 列出一个组织的所有成员
class UserBasic(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    member_role: str


# 获取授权用户的资料
class UserDetail(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    member_role: str
    blog: str
    weibo: str
    bio: str
    public_repos: int
    public_gists: int
    followers: int  # 关注用户的人数
    following: int  # 用户关注的人数
    stared: int  # 用户收藏仓库数
    watched: int  # 用户关注仓库数
    created_at: str
    updated_at: str
    email: str
    bot_info: Optional["BotInfo"]


# 获取授权用户的全部邮箱
class UserEmail(TypedDict, total=False):
    email: str
    state: str
    scope: Optional[list[str]]


# 获取一个用户
class UserInfo(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    member_role: str
    blog: str
    weibo: str
    bio: str
    public_repos: int
    public_gists: int
    followers: int  # 关注用户的人数
    following: int  # 用户关注的人数
    stared: int  # 用户收藏仓库数
    watched: int  # 用户关注仓库数
    created_at: str
    updated_at: str
    company: str
    profession: str
    wechat: str
    qq: str
    linkedin: str
    email: str


class UserMini(TypedDict, total=False):
    id: int
    login: str
    name: str
    avatar_url: str
    url: str
    html_url: str
    remark: str  # 企业备注名


# 提交多个文件变更
class postV5ReposOwnerRepoCommits(TypedDict, total=False):
    access_token: str  # 用户授权码
    branch: str  # 变更的目标分支名。创建新分支时需提供 `start_branch` 参数
    message: str  # 提交信息
    actions: Optional[list[dict]]
    start_branch: str  # 分支起地点。新建分支时使用，更新分支时可选
    author: dict



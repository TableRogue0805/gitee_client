"""Data models for Gitee Repo."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 上传附件到仓库指定 Release
class AttachFile(TypedDict, total=False):
    id: int
    name: str
    size: int
    uploader: Optional["UserMini"]
    browser_download_url: str


# Blame
class Blame(TypedDict, total=False):
    commit: Optional["Commit"]
    lines: Optional[list[str]]  # 代码行


# 获取文件Blob
class Blob(TypedDict, total=False):
    sha: str
    size: int
    url: str
    content: str
    encoding: str


# 获取所有分支
class Branch(TypedDict, total=False):
    name: str
    commit: str
    protected: bool
    protection_url: str


# 获取用户Star的代码片段
class Code(TypedDict, total=False):
    url: str
    forks_url: str
    commits_url: str
    id: str
    description: str
    public: bool
    owner: Optional["UserBasic"]
    user: Optional["UserBasic"]
    files: str
    truncated: bool
    html_url: str
    comments: int
    comments_url: str
    git_pull_url: str
    git_push_url: str
    created_at: str
    updated_at: str


# 修改代码片段的评论
class CodeComment(TypedDict, total=False):
    id: int
    body: str
    created_at: str
    updated_at: str


# 获取 Fork 了指定代码片段的列表
class CodeForks(TypedDict, total=False):
    user: Optional["UserBasic"]
    url: str
    id: str
    created_at: str
    updated_at: str


# 获取代码片段的commit
class CodeForksHistory(TypedDict, total=False):
    url: str
    forks_url: str
    commits_url: str
    id: str
    description: str
    public: bool
    owner: Optional["UserBasic"]
    user: Optional["UserBasic"]
    files: str
    truncated: bool
    html_url: str
    comments: int
    comments_url: str
    git_pull_url: str
    git_push_url: str
    created_at: str
    updated_at: str
    forks: str
    history: str


class Commit(TypedDict, total=False):
    sha: str
    author: Optional["GitUser"]
    committer: Optional["GitUser"]
    message: str
    tree: str
    parents: Optional[list[str]]


# 删除文件
class CommitContent(TypedDict, total=False):
    content: Optional["ContentBasic"]
    commit: Optional["Commit"]


class CommitParentsBasic(TypedDict, total=False):
    url: str
    sha: str  # 第一个父级commit的sha值（即将废弃）
    shas: Optional[list[str]]  # 全部父级 commit 的 sha 值


# Commits 对比
#  返回的 commits 数量限制在 100 以内
class Compare(TypedDict, total=False):
    base_commit: Optional["RepoCommit"]
    merge_base_commit: Optional["RepoCommit"]
    commits: Optional[list["RepoCommit"]]  # commits 数量限制在 100 以内
    files: Optional[list["DiffFile"]]  # 文件列表
    truncated: bool  # 文件列表是否被截断


# 创建分支
class CompleteBranch(TypedDict, total=False):
    name: str
    commit: str
    _links: str
    protected: bool
    protection_url: str


# 获取仓库具体路径下的内容
class Content(TypedDict, total=False):
    type: str
    encoding: str
    size: int
    name: str
    path: str
    content: str
    sha: str
    url: str
    html_url: str
    download_url: str
    _links: str


class ContentBasic(TypedDict, total=False):
    name: str
    path: str
    size: int
    sha: str
    type: str
    url: str
    html_url: str
    download_url: str
    _links: str


# 获取仓库贡献者
class Contributor(TypedDict, total=False):
    email: str
    name: str
    contributions: int


class DiffFile(TypedDict, total=False):
    sha: str
    filename: str  # 文件路径
    status: str  # 文件状态
    additions: int  # 新增行数
    deletions: int  # 删除行数
    changes: int  # 变更行数
    blob_url: str  # blob 链接
    raw_url: str  # raw 链接
    content_url: str  # content 链接
    patch: str  # patch
    truncated: bool  # patch 内容是否被截断


# 更新一个仓库WebHook
class Hook(TypedDict, total=False):
    id: int
    url: str
    password: str
    result: str
    project_id: int
    result_code: int
    created_at: str
    push_events: bool
    tag_push_events: bool
    issues_events: bool
    note_events: bool
    merge_requests_events: bool
    title: str  # WebHook名称


# 获取企业某个标签
class Label(TypedDict, total=False):
    id: int
    color: str
    name: str
    repository_id: int
    url: str
    created_at: str
    updated_at: str


# 搜索仓库
class Project(TypedDict, total=False):
    id: int
    full_name: str
    human_name: str
    url: str
    namespace: Optional["NamespaceMini"]
    path: str  # 仓库路径
    name: str  # 仓库名称
    owner: Optional["UserBasic"]  # 仓库拥有者
    assigner: Optional["UserBasic"]  # 仓库负责人
    description: str  # 仓库描述
    private: bool  # 是否私有
    public: bool  # 是否公开
    internal: bool  # 是否内部开源
    fork: bool  # 是否是fork仓库
    html_url: str  # 仓库地址
    ssh_url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    hooks_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    stargazers_url: str
    contributors_url: str
    commits_url: str
    comments_url: str
    issue_comment_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    recommend: bool  # 是否是推荐仓库
    gvp: bool  # 是否是 GVP 仓库
    homepage: str  # 主页
    language: str  # 语言
    forks_count: int  # 仓库fork数量
    stargazers_count: int  # 仓库star数量
    watchers_count: int  # 仓库watch数量
    default_branch: str  # 默认分支
    open_issues_count: int  # 开启的issue数量
    has_issues: bool  # 是否开启issue功能
    has_wiki: bool  # 是否开启Wiki功能
    issue_comment: bool  # 是否允许用户对“关闭”状态的 Issue 进行评论
    can_comment: bool  # 是否允许用户对仓库进行评论
    pull_requests_enabled: bool  # 是否接受 Pull Request，协作开发
    has_page: bool  # 是否开启了 Pages
    license: str  # 开源许可
    outsourced: bool  # 仓库类型（内部/外包）
    project_creator: str  # 仓库创建者的 username
    members: Optional[list[str]]  # 仓库成员的username
    pushed_at: str  # 最近一次代码推送时间
    created_at: str
    updated_at: str
    parent: Optional["Project"]  # 源仓库
    paas: str
    stared: bool  # 是否 star（此字段已废弃，固定返回 false）
    watched: bool  # 是否 watch
    permission: dict  # 操作权限
    relation: str  # 当前用户相对于仓库的角色
    assignees_number: int  # 代码审查设置，审查人数
    testers_number: int  # 代码审查设置，测试人数
    assignee: Optional[list["UserBasic"]]  # 代码审查设置，审查人员
    testers: Optional[list["UserBasic"]]  # 代码审查设置，测试人员
    status: str  # 仓库状态
    programs: Optional[list["ProgramBasic"]]  # 仓库所属的项目
    enterprise: Optional["NamespaceMini"]  # 仓库所属的企业
    project_labels: Optional[list["ProjectLabel"]]
    issue_template_source: str  # Issue 模版来源 project: 使用仓库 Issue Template 作为模版； enterprise: 使用企业工作项作为模版


class ProjectBasic(TypedDict, total=False):
    id: int
    full_name: str
    human_name: str
    url: str
    namespace: Optional["NamespaceMini"]
    path: str  # 仓库路径
    name: str  # 仓库名称
    owner: Optional["UserBasic"]  # 仓库拥有者
    assigner: Optional["UserBasic"]  # 仓库负责人
    description: str  # 仓库描述
    private: bool  # 是否私有
    public: bool  # 是否公开
    internal: bool  # 是否内部开源
    fork: bool  # 是否是fork仓库
    html_url: str  # 仓库地址
    ssh_url: str


# 仓库代码语言字节数
class ProjectLanguage(TypedDict, total=False):
    languages: dict  # 编程语言及对应的字节数


# 添加仓库成员或更新仓库成员权限
class ProjectMember(TypedDict, total=False):
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
    permissions: str


# 查看仓库成员的权限
class ProjectMemberPermission(TypedDict, total=False):
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
    permission: str


class ProjectMini(TypedDict, total=False):
    id: int
    full_name: str
    human_name: str
    url: str
    namespace: Optional["NamespaceMini"]


# 修改仓库推送规则设置
class ProjectPushConfig(TypedDict, total=False):
    restrict_push_own_commit: bool
    restrict_author_email_suffix: bool
    author_email_suffix: str
    restrict_commit_message: bool
    commit_message_regex: str
    restrict_file_size: bool
    max_file_size: int
    except_manager: bool


# 获取最近30天的七日以内访问量
class ProjectTrafficData(TypedDict, total=False):
    counts: Optional[list["ProjectTrafficDataDesc"]]  # 每天的访问量数据集
    summary: Optional["ProjectTrafficDataSummary"]  # 该次查询的总访问数据


class ProjectTrafficDataDesc(TypedDict, total=False):
    bucket: int  # 日期,10位日期时间戳
    ip: int  # 浏览次数
    pull: int  # 拉取次数
    push: int  # 推送次数
    download_zip: int  # 每天的ZIP包下载次数


class ProjectTrafficDataSummary(TypedDict, total=False):
    ip: int  # 浏览次数
    pull: int  # 拉取次数
    push: int  # 推送次数
    download_zip: int  # 每天的ZIP包下载次数


# 列出 watch 了仓库的用户
class ProjectWatchers(TypedDict, total=False):
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
    watch_at: str


# 删除保护分支规则
class ProtectionRule(TypedDict, total=False):
    id: int
    project_id: int
    wildcard: str
    pushers: dict
    mergers: dict
    contexts: Optional[list[str]]  # 检查项列表
    strict: bool  # 是否严格检查
    mode: str  # 模式 standard: 标准模式, review: 评审模式
    escapse_protect_branch_list: list  # 不受规则影响的分支列表，以英文逗号分隔，形如：['a', 'b']


# 更新仓库Release
class Release(TypedDict, total=False):
    id: int
    tag_name: str
    target_commitish: str
    prerelease: bool
    name: str
    body: str
    author: Optional["UserBasic"]
    created_at: str
    assets: Optional[list[str]]


# 仓库的所有提交
class RepoCommit(TypedDict, total=False):
    url: str
    sha: str
    html_url: str
    comments_url: str
    commit: str
    author: Optional["UserBasic"]
    committer: Optional["UserBasic"]
    parents: Optional[list[str]]


# 仓库的某个提交
class RepoCommitWithFiles(TypedDict, total=False):
    url: str
    sha: str
    html_url: str
    comments_url: str
    commit: str
    author: Optional["UserBasic"]
    committer: Optional["UserBasic"]
    parents: Optional[list[str]]
    stats: str
    files: Optional[list["DiffFile"]]  # 文件列表
    truncated: bool  # 文件列表是否被截断


# 创建一个仓库的 Tag
class Tag(TypedDict, total=False):
    name: str
    message: str
    commit: str
    tagger: Optional["GitUser"]


# 获取目录Tree
class Tree(TypedDict, total=False):
    sha: str
    url: str
    tree: Optional[list[str]]
    truncated: bool



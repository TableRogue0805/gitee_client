"""Data models for Gitee Pull Request."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 企业 Pull Request 列表
class PullRequest(TypedDict, total=False):
    id: int
    url: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    number: int
    close_related_issue: int
    prune_branch: bool
    state: str
    assignees_number: int
    testers_number: int
    assignees: Optional[list["UserAssignee"]]
    testers: Optional[list["UserAssignee"]]
    api_reviewers_number: int
    api_reviewers: Optional[list["UserAssignee"]]
    milestone: Optional["Milestone"]
    labels: Optional[list["Label"]]
    locked: bool
    created_at: str
    updated_at: str
    closed_at: str
    draft: bool
    merged_at: str
    security_hole: bool  # 是否为私有PR
    mergeable: bool
    can_merge_check: bool
    _links: str
    user: Optional["UserBasic"]
    ref_pull_requests: Optional[list["RefPullRequest"]]
    title: str
    body: str
    body_html: str
    head: str
    base: str


# 编辑评论
class PullRequestComments(TypedDict, total=False):
    url: str
    id: int
    path: str
    position: str
    original_position: str
    new_line: str
    commit_id: str
    original_commit_id: str
    user: Optional["UserBasic"]
    created_at: str
    updated_at: str
    body: str
    html_url: str
    pull_request_url: str
    _links: str
    comment_type: str
    in_reply_to_id: int


# 获取某Pull Request的所有Commit信息。最多显示250条Commit
class PullRequestCommits(TypedDict, total=False):
    url: str
    sha: str
    html_url: str
    comments_url: str
    commit: str
    author: Optional["UserBasic"]
    committer: str
    parents: Optional["CommitParentsBasic"]


# Pull Request Commit文件列表。最多显示300条diff
class PullRequestFiles(TypedDict, total=False):
    sha: str
    filename: str
    status: str
    additions: str
    deletions: str
    blob_url: str
    raw_url: str
    patch: str


class RefPullRequest(TypedDict, total=False):
    number: str
    title: str
    state: str



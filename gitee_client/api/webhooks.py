"""Webhooks API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class WebhooksAPI(BaseAPI):
    """Gitee Webhooks API.

    All methods correspond to endpoints under the ``Webhooks`` group.
    """

    def create_repos_hooks(self, owner: str, repo: str, url: str, encryption_type: Optional[int] = None, issues_events: Optional[bool] = None, merge_requests_events: Optional[bool] = None, note_events: Optional[bool] = None, password: Optional[str] = None, push_events: Optional[bool] = None, tag_push_events: Optional[bool] = None, title: Optional[str] = None) -> Any:
        """创建一个仓库WebHook

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        url: 远程HTTP URL (**必填**)
        title: WebHook名称，最多191个字符
        encryption_type: 加密类型: 0: 密码, 1: 签名密钥
        password: 请求URL时会带上该密码，防止URL被恶意请求
        push_events: Push代码到仓库
        tag_push_events: 提交Tag到仓库
        issues_events: 创建/关闭Issue
        note_events: 评论了Issue/代码等等
        merge_requests_events: 合并请求和合并后

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "url": url,
                "title": title,
                "encryption_type": encryption_type,
                "password": password,
                "push_events": push_events,
                "tag_push_events": tag_push_events,
                "issues_events": issues_events,
                "note_events": note_events,
                "merge_requests_events": merge_requests_events,
            },
        )

    def create_repos_hooks_tests(self, id: int, owner: str, repo: str) -> Any:
        """测试WebHook是否发送成功

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: Webhook的ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks/{id}/tests", id=id, owner=owner, repo=repo)
        return self._post(
            url,
        )

    def delete_repos_hooks(self, id: int, owner: str, repo: str) -> Any:
        """删除一个仓库WebHook

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: Webhook的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def get_repos_hooks(self, id: int, owner: str, repo: str) -> Any:
        """获取仓库单个WebHook

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: Webhook的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_hooks(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出仓库的WebHooks

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def update_repos_hooks(self, id: int, owner: str, repo: str, url: str, encryption_type: Optional[int] = None, issues_events: Optional[bool] = None, merge_requests_events: Optional[bool] = None, note_events: Optional[bool] = None, password: Optional[str] = None, push_events: Optional[bool] = None, tag_push_events: Optional[bool] = None, title: Optional[str] = None) -> Any:
        """更新一个仓库WebHook

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: Webhook的ID (**必填**)
        Query/Form parameters:
        url: 远程HTTP URL (**必填**)
        title: WebHook名称，最多191个字符
        encryption_type: 加密类型: 0: 密码, 1: 签名密钥
        password: 请求URL时会带上该密码，防止URL被恶意请求
        push_events: Push代码到仓库
        tag_push_events: 提交Tag到仓库
        issues_events: 创建/关闭Issue
        note_events: 评论了Issue/代码等等
        merge_requests_events: 合并请求和合并后

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks/{id}", id=id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "url": url,
                "title": title,
                "encryption_type": encryption_type,
                "password": password,
                "push_events": push_events,
                "tag_push_events": tag_push_events,
                "issues_events": issues_events,
                "note_events": note_events,
                "merge_requests_events": merge_requests_events,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_repos_hooks_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_hooks()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_hooks` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/hooks", owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )


"""Milestones API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class MilestonesAPI(BaseAPI):
    """Gitee Milestones API.

    All methods correspond to endpoints under the ``Milestones`` group.
    """

    def create_repos_milestones(self, due_on: str, owner: str, repo: str, title: str, description: Optional[str] = None, state: Optional[str] = None) -> Any:
        """创建仓库里程碑

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        title: 里程碑标题 (**必填**)
        state: 里程碑状态: open, closed, all。默认: open
        description: 里程碑具体描述
        due_on: 里程碑的截止日期 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "title": title,
                "state": state,
                "description": description,
                "due_on": due_on,
            },
        )

    def delete_repos_milestones(self, number: int, owner: str, repo: str) -> Any:
        """删除仓库单个里程碑

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 里程碑序号(id) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones/{number}", number=number, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def get_repos_milestones(self, number: int, owner: str, repo: str) -> Any:
        """获取仓库单个里程碑

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 里程碑序号(id) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones/{number}", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_milestones(self, owner: str, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """获取仓库所有里程碑

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        state: 里程碑状态: open, closed, all。默认: open
        sort: 排序方式: due_on
        direction: 升序(asc)或是降序(desc)。默认: asc
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "state": state,
                "sort": sort,
                "direction": direction,
                "page": page,
                "per_page": per_page,
            },
        )

    def update_repos_milestones(self, due_on: str, number: int, owner: str, repo: str, title: str, description: Optional[str] = None, state: Optional[str] = None) -> Any:
        """更新仓库里程碑

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 里程碑序号(id) (**必填**)
        Query/Form parameters:
        title: 里程碑标题 (**必填**)
        state: 里程碑状态: open, closed, all。默认: open
        description: 里程碑具体描述
        due_on: 里程碑的截止日期 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones/{number}", number=number, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "title": title,
                "state": state,
                "description": description,
                "due_on": due_on,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_repos_milestones_all(self, owner: str, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_milestones()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_milestones` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/milestones", owner=owner, repo=repo)
        params = {
            "state": state,            "sort": sort,            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


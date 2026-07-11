"""Search API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class SearchAPI(BaseAPI):
    """Gitee Search API.

    All methods correspond to endpoints under the ``Search`` group.
    """

    def list_search_issues(self, q: str, assignee: Optional[str] = None, author: Optional[str] = None, label: Optional[str] = None, language: Optional[str] = None, order: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, repo: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """搜索 Issues

        Query/Form parameters:
        q: 搜索关键字 (**必填**)
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        repo: 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues
        language: 筛选指定语言的 issues
        label: 筛选指定标签的 issues
        state: 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝)
        author: 筛选指定创建者 (username/login) 的 issues
        assignee: 筛选指定负责人 (username/login) 的 issues
        sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配
        order: 排序顺序: desc(default)、asc

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/search/issues")
        return self._get(
            url,
            params={
                "q": q,
                "page": page,
                "per_page": per_page,
                "repo": repo,
                "language": language,
                "label": label,
                "state": state,
                "author": author,
                "assignee": assignee,
                "sort": sort,
                "order": order,
            },
        )

    def list_search_repositories(self, q: str, fork: Optional[bool] = None, language: Optional[str] = None, order: Optional[str] = None, owner: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """搜索仓库

        Query/Form parameters:
        q: 搜索关键字 (**必填**)
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        owner: 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库
        fork: 是否搜索含 fork 的仓库，默认：否
        language: 筛选指定语言的仓库
        sort: 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配
        order: 排序顺序: desc(default)、asc

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/search/repositories")
        return self._get(
            url,
            params={
                "q": q,
                "page": page,
                "per_page": per_page,
                "owner": owner,
                "fork": fork,
                "language": language,
                "sort": sort,
                "order": order,
            },
        )

    def list_search_users(self, q: str, order: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """搜索用户

        Query/Form parameters:
        q: 搜索关键字 (**必填**)
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        sort: 排序字段，joined_at(注册时间)，默认为最佳匹配
        order: 排序顺序: desc(default)、asc

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/search/users")
        return self._get(
            url,
            params={
                "q": q,
                "page": page,
                "per_page": per_page,
                "sort": sort,
                "order": order,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_search_issues_all(self, q: str, assignee: Optional[str] = None, author: Optional[str] = None, label: Optional[str] = None, language: Optional[str] = None, max_pages: Optional[int] = None, order: Optional[str] = None, per_page: int = 100, repo: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_search_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_search_issues` for parameter documentation.
        """
        url = build_url("", "/v5/search/issues")
        params = {
            "q": q,            "repo": repo,            "language": language,            "label": label,            "state": state,            "author": author,            "assignee": assignee,            "sort": sort,            "order": order,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_search_repositories_all(self, q: str, fork: Optional[bool] = None, language: Optional[str] = None, max_pages: Optional[int] = None, order: Optional[str] = None, owner: Optional[str] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_search_repositories()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_search_repositories` for parameter documentation.
        """
        url = build_url("", "/v5/search/repositories")
        params = {
            "q": q,            "owner": owner,            "fork": fork,            "language": language,            "sort": sort,            "order": order,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_search_users_all(self, q: str, max_pages: Optional[int] = None, order: Optional[str] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_search_users()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_search_users` for parameter documentation.
        """
        url = build_url("", "/v5/search/users")
        params = {
            "q": q,            "sort": sort,            "order": order,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


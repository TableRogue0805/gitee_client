"""Gists API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class GistsAPI(BaseAPI):
    """Gitee Gists API.

    All methods correspond to endpoints under the ``Gists`` group.
    """

    def create_gists(self, description: str, files: dict, public: Optional[bool] = None) -> Any:
        """创建代码片段

        Query/Form parameters:
        files: Hash形式的代码片段文件名以及文件内容。如: { "file1.txt": { "content": "String file contents" } } (**必填**)
        description: 代码片段描述，1~30个字符 (**必填**)
        public: 公开/私有，默认: 私有

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists")
        return self._post(
            url,
            data={
                "files": files,
                "description": description,
                "public": public,
            },
        )

    def create_gists_comments(self, body: str, gist_id: str) -> Any:
        """增加代码片段的评论

        Path parameters:
        gist_id: 代码片段的ID (**必填**)
        Query/Form parameters:
        body: 评论内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{gist_id}/comments", gist_id=gist_id)
        return self._post(
            url,
            data={
                "body": body,
            },
        )

    def create_gists_forks(self, id: str) -> Any:
        """Fork代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/forks", id=id)
        return self._post(
            url,
        )

    def delete_gists(self, id: str) -> Any:
        """删除指定代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}", id=id)
        return self._delete(
            url,
        )

    def delete_gists_comments(self, gist_id: str, id: int) -> Any:
        """删除代码片段的评论

        Path parameters:
        gist_id: 代码片段的ID (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{gist_id}/comments/{id}", gist_id=gist_id, id=id)
        return self._delete(
            url,
        )

    def delete_gists_star(self, id: str) -> Any:
        """取消Star代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/star", id=id)
        return self._delete(
            url,
        )

    def get_gists(self, id: str) -> Any:
        """获取单条代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}", id=id)
        return self._get(
            url,
        )

    def get_gists_comments(self, gist_id: str, id: int) -> Any:
        """获取单条代码片段的评论

        Path parameters:
        gist_id: 代码片段的ID (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{gist_id}/comments/{id}", gist_id=gist_id, id=id)
        return self._get(
            url,
        )

    def get_gists_star(self, id: str) -> Any:
        """判断代码片段是否已Star

        Path parameters:
        id: 代码片段的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/star", id=id)
        return self._get(
            url,
        )

    def list_gists(self, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None) -> Any:
        """获取代码片段

        Query/Form parameters:
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists")
        return self._get(
            url,
            params={
                "since": since,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_gists_comments(self, gist_id: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取代码片段的评论

        Path parameters:
        gist_id: 代码片段的ID (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{gist_id}/comments", gist_id=gist_id)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_gists_commits(self, id: str) -> Any:
        """获取代码片段的commit

        Path parameters:
        id: 代码片段的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/commits", id=id)
        return self._get(
            url,
        )

    def list_gists_forks(self, id: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取 Fork 了指定代码片段的列表

        Path parameters:
        id: 代码片段的ID (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/forks", id=id)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_gists_starred(self, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None) -> Any:
        """获取用户Star的代码片段

        Query/Form parameters:
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/starred")
        return self._get(
            url,
            params={
                "since": since,
                "page": page,
                "per_page": per_page,
            },
        )

    def update_gists(self, id: str, description: Optional[str] = None, files: Optional[dict] = None) -> Any:
        """修改代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)
        Query/Form parameters:
        files: Hash形式的代码片段文件名以及文件内容。如: { "file1.txt": { "content": "String file contents" } }
        description: 代码片段描述，1~30个字符

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}", id=id)
        return self._patch(
            url,
            data={
                "files": files,
                "description": description,
            },
        )

    def update_gists_comments(self, body: str, gist_id: str, id: int) -> Any:
        """修改代码片段的评论

        Path parameters:
        gist_id: 代码片段的ID (**必填**)
        id: 评论的ID (**必填**)
        Query/Form parameters:
        body: 评论内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{gist_id}/comments/{id}", gist_id=gist_id, id=id)
        return self._patch(
            url,
            data={
                "body": body,
            },
        )

    def update_gists_star(self, id: str) -> Any:
        """Star代码片段

        Path parameters:
        id: 代码片段的ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gists/{id}/star", id=id)
        return self._put(
            url,
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_gists_all(self, max_pages: Optional[int] = None, per_page: int = 100, since: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_gists()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_gists` for parameter documentation.
        """
        url = build_url("", "/v5/gists")
        params = {
            "since": since,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_gists_comments_all(self, gist_id: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_gists_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_gists_comments` for parameter documentation.
        """
        url = build_url("", "/v5/gists/{gist_id}/comments", gist_id=gist_id)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_gists_forks_all(self, id: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_gists_forks()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_gists_forks` for parameter documentation.
        """
        url = build_url("", "/v5/gists/{id}/forks", id=id)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_gists_starred_all(self, max_pages: Optional[int] = None, per_page: int = 100, since: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_gists_starred()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_gists_starred` for parameter documentation.
        """
        url = build_url("", "/v5/gists/starred")
        params = {
            "since": since,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


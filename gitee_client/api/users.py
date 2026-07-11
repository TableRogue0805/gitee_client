"""Users API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class UsersAPI(BaseAPI):
    """Gitee Users API.

    All methods correspond to endpoints under the ``Users`` group.
    """

    def create_user_keys(self, key: str, title: str) -> Any:
        """添加一个公钥

        Query/Form parameters:
        key: 公钥内容 (**必填**)
        title: 公钥名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/keys")
        return self._post(
            url,
            data={
                "key": key,
                "title": title,
            },
        )

    def delete_user_following(self, username: str) -> Any:
        """取消关注一个用户

        Path parameters:
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/following/{username}", username=username)
        return self._delete(
            url,
        )

    def delete_user_keys(self, id: int) -> Any:
        """删除一个公钥

        Path parameters:
        id: 公钥 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/keys/{id}", id=id)
        return self._delete(
            url,
        )

    def get_user_following(self, username: str) -> Any:
        """检查授权用户是否关注了一个用户

        Path parameters:
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/following/{username}", username=username)
        return self._get(
            url,
        )

    def get_user_keys(self, id: int) -> Any:
        """获取一个公钥

        Path parameters:
        id: 公钥 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/keys/{id}", id=id)
        return self._get(
            url,
        )

    def get_users(self, username: str) -> Any:
        """获取一个用户

        Path parameters:
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}", username=username)
        return self._get(
            url,
        )

    def get_users_following(self, target_user: str, username: str) -> Any:
        """检查指定用户是否关注目标用户

        Path parameters:
        username: 用户名(username/login) (**必填**)
        target_user: 目标用户的用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/following/{target_user}", target_user=target_user, username=username)
        return self._get(
            url,
        )

    def list_user(self) -> Any:
        """获取授权用户的资料


        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user")
        return self._get(
            url,
        )

    def list_user_followers(self, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户的关注者

        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/followers")
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_following(self, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户正关注的用户

        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/following")
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_keys(self, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户的所有公钥

        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/keys")
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_namespace(self, path: str) -> Any:
        """获取授权用户的一个 Namespace

        Query/Form parameters:
        path: Namespace path (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/namespace")
        return self._get(
            url,
            params={
                "path": path,
            },
        )

    def list_user_namespaces(self, mode: Optional[str] = None) -> Any:
        """列出授权用户所有的 Namespace

        Query/Form parameters:
        mode: 参与方式: project(所有参与仓库的namepsce)、intrant(所加入的namespace)、all(包含前两者)，默认(intrant)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/namespaces")
        return self._get(
            url,
            params={
                "mode": mode,
            },
        )

    def list_users_followers(self, username: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出指定用户的关注者

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/followers", username=username)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_users_following(self, username: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出指定用户正在关注的用户

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/following", username=username)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_users_keys(self, username: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出指定用户的所有公钥

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/keys", username=username)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def update_user(self, bio: Optional[str] = None, blog: Optional[str] = None, name: Optional[str] = None, weibo: Optional[str] = None) -> Any:
        """更新授权用户的资料

        Query/Form parameters:
        name: 昵称
        blog: 微博链接
        weibo: 博客站点
        bio: 自我介绍

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user")
        return self._patch(
            url,
            data={
                "name": name,
                "blog": blog,
                "weibo": weibo,
                "bio": bio,
            },
        )

    def update_user_following(self, username: str) -> Any:
        """关注一个用户

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/following/{username}", username=username)
        return self._put(
            url,
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_user_followers_all(self, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_followers()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_followers` for parameter documentation.
        """
        url = build_url("", "/v5/user/followers")
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_user_following_all(self, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_following()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_following` for parameter documentation.
        """
        url = build_url("", "/v5/user/following")
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_user_keys_all(self, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_keys()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_keys` for parameter documentation.
        """
        url = build_url("", "/v5/user/keys")
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_users_followers_all(self, username: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_users_followers()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_users_followers` for parameter documentation.
        """
        url = build_url("", "/v5/users/{username}/followers", username=username)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_users_following_all(self, username: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_users_following()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_users_following` for parameter documentation.
        """
        url = build_url("", "/v5/users/{username}/following", username=username)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_users_keys_all(self, username: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_users_keys()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_users_keys` for parameter documentation.
        """
        url = build_url("", "/v5/users/{username}/keys", username=username)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )


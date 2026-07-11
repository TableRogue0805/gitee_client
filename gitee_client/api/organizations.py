"""Organizations API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class OrganizationsAPI(BaseAPI):
    """Gitee Organizations API.

    All methods correspond to endpoints under the ``Organizations`` group.
    """

    def create_users_organization(self, name: str, org: str, description: Optional[str] = None) -> Any:
        """创建组织

        Query/Form parameters:
        name: 组织名称 (**必填**)
        org: 组织的路径(path/login) (**必填**)
        description: 组织描述

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/organization")
        return self._post(
            url,
            data={
                "name": name,
                "org": org,
                "description": description,
            },
        )

    def delete_orgs_memberships(self, org: str, username: str) -> Any:
        """移除授权用户所管理组织中的成员

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/memberships/{username}", org=org, username=username)
        return self._delete(
            url,
        )

    def delete_user_memberships_orgs(self, org: str) -> Any:
        """退出一个组织

        Path parameters:
        org: 组织的路径(path/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/memberships/orgs/{org}", org=org)
        return self._delete(
            url,
        )

    def get_orgs(self, org: str) -> Any:
        """获取一个组织

        Path parameters:
        org: 组织的路径(path/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}", org=org)
        return self._get(
            url,
        )

    def get_orgs_memberships(self, org: str, username: str) -> Any:
        """获取授权用户所属组织的一个成员

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/memberships/{username}", org=org, username=username)
        return self._get(
            url,
        )

    def get_user_memberships_orgs(self, org: str) -> Any:
        """获取授权用户在一个组织的成员资料

        Path parameters:
        org: 组织的路径(path/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/memberships/orgs/{org}", org=org)
        return self._get(
            url,
        )

    def list_orgs_followers(self, org: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出指定组织的所有关注者

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/followers", org=org)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_orgs_members(self, org: str, page: Optional[int] = None, per_page: Optional[int] = None, role: Optional[str] = None) -> Any:
        """列出一个组织的所有成员

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        role: 根据角色筛选成员

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/members", org=org)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "role": role,
            },
        )

    def list_user_memberships_orgs(self, active: Optional[bool] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户在所属组织的成员资料

        Query/Form parameters:
        active: 根据成员是否已激活进行筛选资料，缺省返回所有资料
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/memberships/orgs")
        return self._get(
            url,
            params={
                "active": active,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_orgs(self, admin: Optional[bool] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户所属的组织

        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        admin: 只列出授权用户管理的组织

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/orgs")
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "admin": admin,
            },
        )

    def list_users_orgs(self, username: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出用户所属的组织

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/orgs", username=username)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def update_orgs(self, org: str, description: Optional[str] = None, email: Optional[str] = None, html_url: Optional[str] = None, location: Optional[str] = None, name: Optional[str] = None) -> Any:
        """更新授权用户所管理的组织资料

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        email: 组织公开的邮箱地址
        location: 组织所在地
        name: 组织名称
        description: 组织简介
        html_url: 组织站点

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}", org=org)
        return self._patch(
            url,
            data={
                "email": email,
                "location": location,
                "name": name,
                "description": description,
                "html_url": html_url,
            },
        )

    def update_orgs_memberships(self, org: str, username: str, role: Optional[str] = None) -> Any:
        """增加或更新授权用户所管理组织的成员

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        role: 设置用户在组织的角色

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/memberships/{username}", org=org, username=username)
        return self._put(
            url,
            data={
                "role": role,
            },
        )

    def update_user_memberships_orgs(self, org: str, remark: Optional[str] = None) -> Any:
        """更新授权用户在一个组织的成员资料

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        remark: 在组织中的备注信息

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/memberships/orgs/{org}", org=org)
        return self._patch(
            url,
            data={
                "remark": remark,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_orgs_followers_all(self, org: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_orgs_followers()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_orgs_followers` for parameter documentation.
        """
        url = build_url("", "/v5/orgs/{org}/followers", org=org)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_orgs_members_all(self, org: str, max_pages: Optional[int] = None, per_page: int = 100, role: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_orgs_members()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_orgs_members` for parameter documentation.
        """
        url = build_url("", "/v5/orgs/{org}/members", org=org)
        params = {
            "role": role,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_user_memberships_orgs_all(self, active: Optional[bool] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_memberships_orgs()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_memberships_orgs` for parameter documentation.
        """
        url = build_url("", "/v5/user/memberships/orgs")
        params = {
            "active": active,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_user_orgs_all(self, admin: Optional[bool] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_orgs()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_orgs` for parameter documentation.
        """
        url = build_url("", "/v5/user/orgs")
        params = {
            "admin": admin,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_users_orgs_all(self, username: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_users_orgs()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_users_orgs` for parameter documentation.
        """
        url = build_url("", "/v5/users/{username}/orgs", username=username)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )


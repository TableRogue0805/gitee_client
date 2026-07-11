"""Enterprises API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class EnterprisesAPI(BaseAPI):
    """Gitee Enterprises API.

    All methods correspond to endpoints under the ``Enterprises`` group.
    """

    def create_enterprises_members(self, enterprise: str, email: Optional[str] = None, name: Optional[str] = None, role: Optional[str] = None, username: Optional[str] = None) -> Any:
        """添加或邀请企业成员

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        username: 需要邀请的用户名(username/login)，username,email至少填写一个
        email: 要添加邮箱地址，若该邮箱未注册则自动创建帐号。username,email至少填写一个
        role: 企业角色：member => 普通成员, outsourced => 外包成员, admin => 管理员
        name: 企业成员真实姓名（备注）

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members", enterprise=enterprise)
        return self._post(
            url,
            data={
                "username": username,
                "email": email,
                "role": role,
                "name": name,
            },
        )

    def create_enterprises_week_report(self, content: str, enterprise: str, week_index: int, year: int, date: Optional[str] = None) -> Any:
        """新建周报

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        year: 周报所属年 (**必填**)
        content: 周报内容 (**必填**)
        week_index: 周报所属周 (**必填**)
        date: 周报日期(格式：2019-03-25)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_report", enterprise=enterprise)
        return self._post(
            url,
            data={
                "year": year,
                "content": content,
                "week_index": week_index,
                "date": date,
            },
        )

    def create_enterprises_week_reports_comment(self, body: str, enterprise: str, id: int) -> Any:
        """评论周报

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        id: 周报ID (**必填**)
        Query/Form parameters:
        body: 评论的内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports/{id}/comment", enterprise=enterprise, id=id)
        return self._post(
            url,
            data={
                "body": body,
            },
        )

    def delete_enterprises_members(self, enterprise: str, username: str) -> Any:
        """移除企业成员

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members/{username}", enterprise=enterprise, username=username)
        return self._delete(
            url,
        )

    def delete_enterprises_week_reports_comments(self, enterprise: str, id: int, report_id: int) -> Any:
        """删除周报某个评论

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        report_id: 周报ID (**必填**)
        id: 评论ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports/{report_id}/comments/{id}", enterprise=enterprise, id=id, report_id=report_id)
        return self._delete(
            url,
        )

    def get_enterprises(self, enterprise: str) -> Any:
        """获取一个企业

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}", enterprise=enterprise)
        return self._get(
            url,
        )

    def get_enterprises_members(self, enterprise: str, username: str) -> Any:
        """获取企业的一个成员

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members/{username}", enterprise=enterprise, username=username)
        return self._get(
            url,
        )

    def get_enterprises_week_reports(self, enterprise: str, id: int) -> Any:
        """周报详情

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        id: 周报ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports/{id}", enterprise=enterprise, id=id)
        return self._get(
            url,
        )

    def list_enterprise_pull_requests(self, enterprise: str, base: Optional[str] = None, direction: Optional[str] = None, head: Optional[str] = None, issue_number: Optional[str] = None, labels: Optional[str] = None, milestone_number: Optional[int] = None, page: Optional[int] = None, per_page: Optional[int] = None, program_id: Optional[int] = None, repo: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """企业 Pull Request 列表

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        issue_number: 可选。Issue 编号(区分大小写，无需添加 # 号)
        repo: 可选。仓库路径(path)
        program_id: 可选。项目ID
        state: 可选。Pull Request 状态
        head: 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch
        base: 可选。Pull Request 提交目标分支的名称。
        sort: 可选。排序字段，默认按创建时间
        since: 可选。起始的更新时间，要求时间格式为 ISO 8601
        direction: 可选。升序/降序
        milestone_number: 可选。里程碑序号(id)
        labels: 用逗号分开的标签。如: bug,performance
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprise/{enterprise}/pull_requests", enterprise=enterprise)
        return self._get(
            url,
            params={
                "issue_number": issue_number,
                "repo": repo,
                "program_id": program_id,
                "state": state,
                "head": head,
                "base": base,
                "sort": sort,
                "since": since,
                "direction": direction,
                "milestone_number": milestone_number,
                "labels": labels,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_enterprises_members(self, enterprise: str, page: Optional[int] = None, per_page: Optional[int] = None, role: Optional[str] = None) -> Any:
        """列出企业的所有成员

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        role: 根据角色筛选成员
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members", enterprise=enterprise)
        return self._get(
            url,
            params={
                "role": role,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_enterprises_members_search(self, enterprise: str, query_type: str, query_value: str) -> Any:
        """获取企业成员信息(通过用户名/邮箱)

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        query_type: 查询类型：username/email (**必填**)
        query_value: 查询值 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members/search", enterprise=enterprise)
        return self._get(
            url,
            params={
                "query_type": query_type,
                "query_value": query_value,
            },
        )

    def list_enterprises_users_week_reports(self, enterprise: str, username: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """个人周报列表

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/users/{username}/week_reports", enterprise=enterprise, username=username)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_enterprises_week_reports(self, enterprise: str, date: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, username: Optional[str] = None, week_index: Optional[int] = None, year: Optional[int] = None) -> Any:
        """企业成员周报列表

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        username: 用户名(username/login)
        year: 周报所属年
        week_index: 周报所属周
        date: 周报日期(格式：2019-03-25)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports", enterprise=enterprise)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "username": username,
                "year": year,
                "week_index": week_index,
                "date": date,
            },
        )

    def list_enterprises_week_reports_comments(self, enterprise: str, id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """某个周报评论列表

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        id: 周报ID (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports/{id}/comments", enterprise=enterprise, id=id)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_enterprises(self, admin: Optional[bool] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出授权用户所属的企业

        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        admin: 只列出授权用户管理的企业

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/enterprises")
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "admin": admin,
            },
        )

    def update_enterprises_members(self, enterprise: str, username: str, active: Optional[bool] = None, name: Optional[str] = None, role: Optional[str] = None) -> Any:
        """修改企业成员权限或备注

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        role: 企业角色：member => 普通成员, outsourced => 外包成员, admin => 管理员
        active: 是否可访问企业资源，默认:是。（若选否则禁止该用户访问企业资源）
        name: 企业成员真实姓名（备注）

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members/{username}", enterprise=enterprise, username=username)
        return self._put(
            url,
            data={
                "role": role,
                "active": active,
                "name": name,
            },
        )

    def update_enterprises_week_report(self, content: str, enterprise: str, id: int) -> Any:
        """编辑周报

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        id: 周报ID (**必填**)
        Query/Form parameters:
        content: 周报内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_report/{id}", enterprise=enterprise, id=id)
        return self._patch(
            url,
            data={
                "content": content,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_enterprise_pull_requests_all(self, enterprise: str, base: Optional[str] = None, direction: Optional[str] = None, head: Optional[str] = None, issue_number: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, milestone_number: Optional[int] = None, per_page: int = 100, program_id: Optional[int] = None, repo: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_enterprise_pull_requests()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprise_pull_requests` for parameter documentation.
        """
        url = build_url("", "/v5/enterprise/{enterprise}/pull_requests", enterprise=enterprise)
        params = {
            "issue_number": issue_number,            "repo": repo,            "program_id": program_id,            "state": state,            "head": head,            "base": base,            "sort": sort,            "since": since,            "direction": direction,            "milestone_number": milestone_number,            "labels": labels,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_enterprises_members_all(self, enterprise: str, max_pages: Optional[int] = None, per_page: int = 100, role: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_enterprises_members()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_members` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/members", enterprise=enterprise)
        params = {
            "role": role,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_enterprises_users_week_reports_all(self, enterprise: str, username: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_enterprises_users_week_reports()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_users_week_reports` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/users/{username}/week_reports", enterprise=enterprise, username=username)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_enterprises_week_reports_all(self, enterprise: str, date: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, username: Optional[str] = None, week_index: Optional[int] = None, year: Optional[int] = None) -> Any:
        """Iterate over all pages of ``list_enterprises_week_reports()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_week_reports` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports", enterprise=enterprise)
        params = {
            "username": username,            "year": year,            "week_index": week_index,            "date": date,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_enterprises_week_reports_comments_all(self, enterprise: str, id: int, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_enterprises_week_reports_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_week_reports_comments` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/week_reports/{id}/comments", enterprise=enterprise, id=id)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_user_enterprises_all(self, admin: Optional[bool] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_user_enterprises()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_enterprises` for parameter documentation.
        """
        url = build_url("", "/v5/user/enterprises")
        params = {
            "admin": admin,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


"""Issues API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class IssuesAPI(BaseAPI):
    """Gitee Issues API.

    All methods correspond to endpoints under the ``Issues`` group.
    """

    def create_repos_issues(self, owner: str, title: str, assignee: Optional[str] = None, body: Optional[str] = None, branch: Optional[str] = None, collaborators: Optional[str] = None, cve_id: Optional[str] = None, issue_type: Optional[str] = None, labels: Optional[str] = None, milestone: Optional[int] = None, program: Optional[str] = None, repo: Optional[str] = None, security_hole: Optional[bool] = None) -> Any:
        """创建Issue

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        Query/Form parameters:
        repo: 仓库路径(path)
        title: Issue标题 (**必填**)
        issue_type: 企业自定义任务类型，非企业默认任务类型为“任务”
        body: Issue描述
        assignee: Issue负责人的个人空间地址
        collaborators: Issue协助者的个人空间地址, 以 , 分隔
        milestone: 里程碑序号
        labels: 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance
        program: 项目ID
        security_hole: 是否是私有issue(默认为false)
        cve_id: CVE identifier for security issues
        branch: 分支名称，传空串表示取消关联分支

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/issues", owner=owner)
        return self._post(
            url,
            data={
                "repo": repo,
                "title": title,
                "issue_type": issue_type,
                "body": body,
                "assignee": assignee,
                "collaborators": collaborators,
                "milestone": milestone,
                "labels": labels,
                "program": program,
                "security_hole": security_hole,
                "cve_id": cve_id,
                "branch": branch,
            },
        )

    def create_repos_issues_comments(self, body: str, number: str, owner: str, repo: str) -> Any:
        """创建某个Issue评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        body: The contents of the comment. (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/comments", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "body": body,
            },
        )

    def delete_repos_issues_comments(self, id: int, owner: str, repo: str) -> Any:
        """删除Issue某条评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/comments/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def get_enterprises_issues(self, enterprise: str, number: str) -> Any:
        """获取企业的某个Issue

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}", enterprise=enterprise, number=number)
        return self._get(
            url,
        )

    def get_repos_issues(self, number: str, owner: str, repo: str) -> Any:
        """仓库的某个Issue

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_issues_comments(self, id: int, owner: str, repo: str) -> Any:
        """获取仓库Issue某条评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/comments/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_enterprises_issues(self, enterprise: str, assignee: Optional[str] = None, created_at: Optional[str] = None, creator: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, milestone: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, program: Optional[str] = None, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """获取某个企业的所有Issues

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        state: Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open
        labels: 用逗号分开的标签。如: bug,performance
        sort: 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at
        direction: 排序方式: 升序(asc)，降序(desc)。默认: desc
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        schedule: 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80
        deadline: 计划截止日期，格式同上
        created_at: 任务创建时间，格式同上
        finished_at: 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上
        milestone: 根据里程碑标题。none为没里程碑的，*为所有带里程碑的
        assignee: 用户的username。 none为没指派者, *为所有带有指派者的
        creator: 创建Issues的用户username
        program: 所属项目名称。none为没所属有项目的，*为所有带所属项目的

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues", enterprise=enterprise)
        return self._get(
            url,
            params={
                "state": state,
                "labels": labels,
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
                "schedule": schedule,
                "deadline": deadline,
                "created_at": created_at,
                "finished_at": finished_at,
                "milestone": milestone,
                "assignee": assignee,
                "creator": creator,
                "program": program,
            },
        )

    def list_enterprises_issues_comments(self, enterprise: str, number: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取企业某个Issue所有评论

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}/comments", enterprise=enterprise, number=number)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_enterprises_issues_labels(self, enterprise: str, number: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取企业某个Issue所有标签

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}/labels", enterprise=enterprise, number=number)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_enterprises_issues_pull_requests(self, enterprise: str, number: str) -> Any:
        """获取企业 issue 关联的 Pull Requests

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}/pull_requests", enterprise=enterprise, number=number)
        return self._get(
            url,
        )

    def list_issues(self, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """获取当前授权用户的所有Issues

        Query/Form parameters:
        filter: 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned
        state: Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open
        labels: 用逗号分开的标签。如: bug,performance
        sort: 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at
        direction: 排序方式: 升序(asc)，降序(desc)。默认: desc
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        schedule: 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80
        deadline: 计划截止日期，格式同上
        created_at: 任务创建时间，格式同上
        finished_at: 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/issues")
        return self._get(
            url,
            params={
                "filter": filter,
                "state": state,
                "labels": labels,
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
                "schedule": schedule,
                "deadline": deadline,
                "created_at": created_at,
                "finished_at": finished_at,
            },
        )

    def list_orgs_issues(self, org: str, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """获取当前用户某个组织的Issues

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        filter: 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned
        state: Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open
        labels: 用逗号分开的标签。如: bug,performance
        sort: 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at
        direction: 排序方式: 升序(asc)，降序(desc)。默认: desc
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        schedule: 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80
        deadline: 计划截止日期，格式同上
        created_at: 任务创建时间，格式同上
        finished_at: 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/issues", org=org)
        return self._get(
            url,
            params={
                "filter": filter,
                "state": state,
                "labels": labels,
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
                "schedule": schedule,
                "deadline": deadline,
                "created_at": created_at,
                "finished_at": finished_at,
            },
        )

    def list_repos_issues(self, owner: str, repo: str, assignee: Optional[str] = None, created_at: Optional[str] = None, creator: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, milestone: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, program: Optional[str] = None, q: Optional[str] = None, schedule: Optional[str] = None, security_hole: Optional[bool] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """仓库的所有Issues

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        state: Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open
        labels: 用逗号分开的标签。如: bug,performance
        sort: 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at
        direction: 排序方式: 升序(asc)，降序(desc)。默认: desc
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        schedule: 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80
        deadline: 计划截止日期，格式同上
        created_at: 任务创建时间，格式同上
        finished_at: 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上
        milestone: 根据里程碑标题。none为没里程碑的，*为所有带里程碑的
        assignee: 用户的username。 none为没指派者, *为所有带有指派者的
        creator: 创建Issues的用户username
        program: 所属项目名称。none为没有所属项目，*为所有带所属项目的
        q: 搜索关键字
        security_hole: 是否只看安全属性的issue

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "state": state,
                "labels": labels,
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
                "schedule": schedule,
                "deadline": deadline,
                "created_at": created_at,
                "finished_at": finished_at,
                "milestone": milestone,
                "assignee": assignee,
                "creator": creator,
                "program": program,
                "q": q,
                "security_hole": security_hole,
            },
        )

    def list_repos_issues_comments(self, owner: str, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None, sort: Optional[str] = None) -> Any:
        """获取仓库所有Issue的评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        sort: Either created or updated. Default: created
        direction: Either asc or desc. Ignored without the sort parameter.
        since: Only comments updated at or after this time are returned.
                                              This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/comments", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_issues_comments_2(self, number: str, owner: str, repo: str, order: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None) -> Any:
        """获取仓库某个Issue所有的评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        since: Only comments updated at or after this time are returned.
                                              This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        order: 排序顺序: asc(default),desc

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/comments", number=number, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "since": since,
                "page": page,
                "per_page": per_page,
                "order": order,
            },
        )

    def list_repos_issues_operate_logs(self, number: str, owner: str, repo: Optional[str] = None, sort: Optional[str] = None) -> Any:
        """获取某个Issue下的操作日志

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        repo: 仓库路径(path)
        sort: 按递增(asc)或递减(desc)排序，默认：递减

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/issues/{number}/operate_logs", number=number, owner=owner)
        return self._get(
            url,
            params={
                "repo": repo,
                "sort": sort,
            },
        )

    def list_repos_issues_pull_requests(self, number: str, owner: str, repo: Optional[str] = None) -> Any:
        """获取 issue 关联的 Pull Requests

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        repo: 仓库路径(path)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/issues/{number}/pull_requests", number=number, owner=owner)
        return self._get(
            url,
            params={
                "repo": repo,
            },
        )

    def list_user_issues(self, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """获取授权用户的所有Issues

        Query/Form parameters:
        filter: 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned
        state: Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open
        labels: 用逗号分开的标签。如: bug,performance
        sort: 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at
        direction: 排序方式: 升序(asc)，降序(desc)。默认: desc
        since: 起始的更新时间，要求时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        schedule: 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80
        deadline: 计划截止日期，格式同上
        created_at: 任务创建时间，格式同上
        finished_at: 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/issues")
        return self._get(
            url,
            params={
                "filter": filter,
                "state": state,
                "labels": labels,
                "sort": sort,
                "direction": direction,
                "since": since,
                "page": page,
                "per_page": per_page,
                "schedule": schedule,
                "deadline": deadline,
                "created_at": created_at,
                "finished_at": finished_at,
            },
        )

    def update_enterprises_issues(self, enterprise: str, number: str, assignee: Optional[str] = None, body: Optional[str] = None, branch: Optional[str] = None, collaborators: Optional[str] = None, cve_id: Optional[str] = None, labels: Optional[str] = None, milestone: Optional[int] = None, program: Optional[str] = None, security_hole: Optional[bool] = None, state: Optional[str] = None, title: Optional[str] = None) -> Any:
        """更新企业的某个Issue

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        title: Issue标题
        state: Issue 状态，open（开启的）、progressing（进行中）、closed（关闭的）
        body: Issue描述
        assignee: Issue负责人的个人空间地址
        collaborators: Issue协助者的个人空间地址, 以 , 分隔
        milestone: 里程碑序号
        labels: 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance
        program: 项目ID
        security_hole: 是否是私有issue(默认为false)
        cve_id: CVE identifier for security issues
        branch: 分支名称，传空串表示取消关联分支

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}", enterprise=enterprise, number=number)
        return self._patch(
            url,
            data={
                "title": title,
                "state": state,
                "body": body,
                "assignee": assignee,
                "collaborators": collaborators,
                "milestone": milestone,
                "labels": labels,
                "program": program,
                "security_hole": security_hole,
                "cve_id": cve_id,
                "branch": branch,
            },
        )

    def update_repos_issues(self, number: str, owner: str, assignee: Optional[str] = None, body: Optional[str] = None, branch: Optional[str] = None, collaborators: Optional[str] = None, cve_id: Optional[str] = None, labels: Optional[str] = None, milestone: Optional[int] = None, program: Optional[str] = None, repo: Optional[str] = None, security_hole: Optional[bool] = None, state: Optional[str] = None, title: Optional[str] = None) -> Any:
        """更新Issue

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        repo: 仓库路径(path)
        title: Issue标题
        state: Issue 状态，open（开启的）、progressing（进行中）、closed（关闭的）
        body: Issue描述
        assignee: Issue负责人的个人空间地址
        collaborators: Issue协助者的个人空间地址, 以 , 分隔
        milestone: 里程碑序号
        labels: 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance
        program: 项目ID
        security_hole: 是否是私有issue(默认为false)
        cve_id: CVE identifier for security issues
        branch: 分支名称，传空串表示取消关联分支

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/issues/{number}", number=number, owner=owner)
        return self._patch(
            url,
            data={
                "repo": repo,
                "title": title,
                "state": state,
                "body": body,
                "assignee": assignee,
                "collaborators": collaborators,
                "milestone": milestone,
                "labels": labels,
                "program": program,
                "security_hole": security_hole,
                "cve_id": cve_id,
                "branch": branch,
            },
        )

    def update_repos_issues_comments(self, body: str, id: int, owner: str, repo: str) -> Any:
        """更新Issue某条评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)
        Query/Form parameters:
        body: The contents of the comment. (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/comments/{id}", id=id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "body": body,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_enterprises_issues_all(self, enterprise: str, assignee: Optional[str] = None, created_at: Optional[str] = None, creator: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, milestone: Optional[str] = None, per_page: int = 100, program: Optional[str] = None, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_enterprises_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_issues` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues", enterprise=enterprise)
        params = {
            "state": state,            "labels": labels,            "sort": sort,            "direction": direction,            "since": since,            "schedule": schedule,            "deadline": deadline,            "created_at": created_at,            "finished_at": finished_at,            "milestone": milestone,            "assignee": assignee,            "creator": creator,            "program": program,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_enterprises_issues_comments_all(self, enterprise: str, number: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_enterprises_issues_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_issues_comments` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}/comments", enterprise=enterprise, number=number)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_enterprises_issues_labels_all(self, enterprise: str, number: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_enterprises_issues_labels()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_issues_labels` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/issues/{number}/labels", enterprise=enterprise, number=number)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_issues_all(self, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_issues` for parameter documentation.
        """
        url = build_url("", "/v5/issues")
        params = {
            "filter": filter,            "state": state,            "labels": labels,            "sort": sort,            "direction": direction,            "since": since,            "schedule": schedule,            "deadline": deadline,            "created_at": created_at,            "finished_at": finished_at,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_orgs_issues_all(self, org: str, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_orgs_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_orgs_issues` for parameter documentation.
        """
        url = build_url("", "/v5/orgs/{org}/issues", org=org)
        params = {
            "filter": filter,            "state": state,            "labels": labels,            "sort": sort,            "direction": direction,            "since": since,            "schedule": schedule,            "deadline": deadline,            "created_at": created_at,            "finished_at": finished_at,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_issues_all(self, owner: str, repo: str, assignee: Optional[str] = None, created_at: Optional[str] = None, creator: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, milestone: Optional[str] = None, per_page: int = 100, program: Optional[str] = None, q: Optional[str] = None, schedule: Optional[str] = None, security_hole: Optional[bool] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_issues` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues", owner=owner, repo=repo)
        params = {
            "state": state,            "labels": labels,            "sort": sort,            "direction": direction,            "since": since,            "schedule": schedule,            "deadline": deadline,            "created_at": created_at,            "finished_at": finished_at,            "milestone": milestone,            "assignee": assignee,            "creator": creator,            "program": program,            "q": q,            "security_hole": security_hole,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_issues_comments_all(self, owner: str, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, since: Optional[str] = None, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_issues_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_issues_comments` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/comments", owner=owner, repo=repo)
        params = {
            "sort": sort,            "direction": direction,            "since": since,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_issues_comments_2_all(self, number: str, owner: str, repo: str, max_pages: Optional[int] = None, order: Optional[str] = None, per_page: int = 100, since: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_issues_comments_2()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_issues_comments_2` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/comments", number=number, owner=owner, repo=repo)
        params = {
            "since": since,            "order": order,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_user_issues_all(self, created_at: Optional[str] = None, deadline: Optional[str] = None, direction: Optional[str] = None, filter: Optional[str] = None, finished_at: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, schedule: Optional[str] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_user_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_issues` for parameter documentation.
        """
        url = build_url("", "/v5/user/issues")
        params = {
            "filter": filter,            "state": state,            "labels": labels,            "sort": sort,            "direction": direction,            "since": since,            "schedule": schedule,            "deadline": deadline,            "created_at": created_at,            "finished_at": finished_at,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


"""Pull Requests API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class PullsAPI(BaseAPI):
    """Gitee Pull Requests API.

    All methods correspond to endpoints under the ``Pull Requests`` group.
    """

    def create_repos_pulls(self, base: str, head: str, owner: str, repo: str, title: str, assignees: Optional[str] = None, assignees_number: Optional[int] = None, body: Optional[str] = None, close_related_issue: Optional[bool] = None, draft: Optional[bool] = None, issue: Optional[str] = None, labels: Optional[str] = None, milestone_number: Optional[int] = None, prune_source_branch: Optional[bool] = None, ref_pull_request_numbers: Optional[str] = None, security_hole: Optional[bool] = None, squash: Optional[bool] = None, testers: Optional[str] = None, testers_number: Optional[int] = None) -> Any:
        """创建Pull Request

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        title: 必填。Pull Request 标题 (**必填**)
        head: 必填。Pull Request 提交的源分支。格式：branch (master) 或者：path_with_namespace:branch (oschina/gitee:master) (**必填**)
        base: 必填。Pull Request 提交目标分支的名称 (**必填**)
        body: 可选。Pull Request 内容
        milestone_number: 可选。里程碑序号(id)
        labels: 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance
        issue: 可选。Pull Request的标题和内容可以根据指定的Issue Id自动填充
        assignees: 可选。审查人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派审查人员】则此选项无效
        testers: 可选。测试人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派测试人员】则此选项无效
        assignees_number: 可选。最少审查人数
        testers_number: 可选。最少测试人数
        ref_pull_request_numbers: 可选。依赖的当前仓库下的PR编号，置空则清空依赖的PR。如：17,18,19
        prune_source_branch: 可选。合并PR后是否删除源分支，默认false（不删除）
        close_related_issue: 可选，合并后是否关闭关联的 Issue，默认根据仓库配置设置
        draft: 是否设置为草稿
        squash: 接受 Pull Request 时使用扁平化（Squash）合并
        security_hole: 是否为私有PR

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "title": title,
                "head": head,
                "base": base,
                "body": body,
                "milestone_number": milestone_number,
                "labels": labels,
                "issue": issue,
                "assignees": assignees,
                "testers": testers,
                "assignees_number": assignees_number,
                "testers_number": testers_number,
                "ref_pull_request_numbers": ref_pull_request_numbers,
                "prune_source_branch": prune_source_branch,
                "close_related_issue": close_related_issue,
                "draft": draft,
                "squash": squash,
                "security_hole": security_hole,
            },
        )

    def create_repos_pulls_assignees(self, assignees: str, number: int, owner: int, repo: int) -> Any:
        """指派用户审查 Pull Request

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        assignees: 用户的个人空间地址, 以 , 分隔 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/assignees", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "assignees": assignees,
            },
        )

    def create_repos_pulls_comments(self, body: str, number: int, owner: str, repo: str, commit_id: Optional[str] = None, path: Optional[str] = None, position: Optional[int] = None) -> Any:
        """提交Pull Request评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        body: 必填。评论内容 (**必填**)
        commit_id: 可选。PR代码评论的commit id
        path: 可选。PR代码评论的文件名
        position: 可选。PR代码评论diff中的行数

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/comments", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "body": body,
                "commit_id": commit_id,
                "path": path,
                "position": position,
            },
        )

    def create_repos_pulls_labels(self, number: int, owner: str, repo: str, body: Any = None) -> Any:
        """创建 Pull Request 标签

        创建 Pull Request 标签
 需要在请求的 body 里填上数组，元素为标签的名字。如: ["performance", "bug"]

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/labels", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            json=body,
        )

    def create_repos_pulls_review(self, number: int, owner: int, repo: int, force: Optional[bool] = None) -> Any:
        """处理 Pull Request 审查

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        force: 是否强制审查通过（默认否），只对管理员生效

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/review", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "force": force,
            },
        )

    def create_repos_pulls_test(self, number: int, owner: int, repo: int, force: Optional[bool] = None) -> Any:
        """处理 Pull Request 测试

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        force: 是否强制测试通过（默认否），只对管理员生效

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/test", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "force": force,
            },
        )

    def create_repos_pulls_testers(self, number: int, owner: int, repo: int, testers: str) -> Any:
        """指派用户测试 Pull Request

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        testers: 用户的个人空间地址, 以 , 分隔 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/testers", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "testers": testers,
            },
        )

    def delete_repos_pulls_assignees(self, assignees: str, number: int, owner: int, repo: int) -> Any:
        """取消用户审查 Pull Request

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        assignees: 用户的个人空间地址, 以 , 分隔 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/assignees", number=number, owner=owner, repo=repo)
        return self._delete(
            url,
            params={
                "assignees": assignees,
            },
        )

    def delete_repos_pulls_comments(self, id: int, owner: str, repo: str) -> Any:
        """删除评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/comments/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_pulls_labels(self, name: str, number: int, owner: str, repo: str) -> Any:
        """删除 Pull Request 标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        name: 标签名称(批量删除用英文逗号分隔，如: bug,feature) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/labels/{name}", name=name, number=number, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_pulls_testers(self, number: int, owner: int, repo: int, testers: str) -> Any:
        """取消用户测试 Pull Request

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        testers: 用户的个人空间地址, 以 , 分隔 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/testers", number=number, owner=owner, repo=repo)
        return self._delete(
            url,
            params={
                "testers": testers,
            },
        )

    def get_repos_pulls(self, number: int, owner: str, repo: str) -> Any:
        """获取单个Pull Request

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_pulls_comments(self, id: int, owner: str, repo: str) -> Any:
        """获取Pull Request的某个评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id:  (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/comments/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_pulls_merge(self, number: int, owner: str, repo: str) -> Any:
        """判断Pull Request是否已经合并

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/merge", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_pulls(self, owner: str, repo: str, assignee: Optional[str] = None, author: Optional[str] = None, base: Optional[str] = None, direction: Optional[str] = None, head: Optional[str] = None, labels: Optional[str] = None, milestone_number: Optional[int] = None, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None, tester: Optional[str] = None) -> Any:
        """获取Pull Request列表

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
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
        author: 可选。PR 创建者用户名
        assignee: 可选。评审者用户名
        tester: 可选。测试者用户名

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls", owner=owner, repo=repo)
        return self._get(
            url,
            params={
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
                "author": author,
                "assignee": assignee,
                "tester": tester,
            },
        )

    def list_repos_pulls_comments(self, number: int, owner: str, repo: str, comment_type: Optional[str] = None, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取某个Pull Request的所有评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        direction: 可选。升序/降序
        comment_type: 可选。筛选评论类型。代码行评论/pr普通评论

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/comments", number=number, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "direction": direction,
                "comment_type": comment_type,
            },
        )

    def list_repos_pulls_commits(self, number: int, owner: str, repo: str) -> Any:
        """获取某Pull Request的所有Commit信息。最多显示250条Commit

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/commits", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_pulls_files(self, number: int, owner: str, repo: str) -> Any:
        """Pull Request Commit文件列表。最多显示300条diff

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/files", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_pulls_issues(self, number: int, owner: int, repo: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取 Pull Request 关联的 issues

        Path parameters:
        owner:  (**必填**)
        repo:  (**必填**)
        number:  (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/issues", number=number, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_pulls_labels(self, number: int, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取某个 Pull Request 的所有标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/labels", number=number, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_pulls_operate_logs(self, number: int, owner: str, repo: str, sort: Optional[str] = None) -> Any:
        """获取某个Pull Request的操作日志

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        sort: 按递增(asc)或递减(desc)排序，默认：递减

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/operate_logs", number=number, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sort": sort,
            },
        )

    def update_repos_pulls(self, number: int, owner: str, repo: str, assignees_number: Optional[int] = None, body: Optional[str] = None, close_related_issue: Optional[bool] = None, draft: Optional[bool] = None, labels: Optional[str] = None, milestone_number: Optional[int] = None, ref_pull_request_numbers: Optional[str] = None, security_hole: Optional[bool] = None, squash: Optional[bool] = None, state: Optional[str] = None, testers_number: Optional[int] = None, title: Optional[str] = None) -> Any:
        """更新Pull Request信息

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        title: 可选。Pull Request 标题
        body: 可选。Pull Request 内容
        state: 可选。Pull Request 状态
        milestone_number: 可选。里程碑序号(id)
        labels: 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance
        assignees_number: 可选。最少审查人数
        testers_number: 可选。最少测试人数
        ref_pull_request_numbers: 可选。依赖的当前仓库下的PR编号，置空则清空依赖的PR。如：17,18,19
        close_related_issue: 可选，合并后是否关闭关联的 Issue，默认根据仓库配置设置
        draft: 是否设置为草稿
        squash: 接受 Pull Request 时使用扁平化（Squash）合并
        security_hole: 是否为私有PR

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}", number=number, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "title": title,
                "body": body,
                "state": state,
                "milestone_number": milestone_number,
                "labels": labels,
                "assignees_number": assignees_number,
                "testers_number": testers_number,
                "ref_pull_request_numbers": ref_pull_request_numbers,
                "close_related_issue": close_related_issue,
                "draft": draft,
                "squash": squash,
                "security_hole": security_hole,
            },
        )

    def update_repos_pulls_assignees(self, number: int, owner: int, repo: int, reset_all: Optional[bool] = None) -> Any:
        """重置 Pull Request 审查 的状态

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        reset_all: 是否重置所有审查人，默认：false，只对管理员生效

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/assignees", number=number, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "reset_all": reset_all,
            },
        )

    def update_repos_pulls_comments(self, body: str, id: int, owner: str, repo: str) -> Any:
        """编辑评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)
        Query/Form parameters:
        body: 必填。评论内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/comments/{id}", id=id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "body": body,
            },
        )

    def update_repos_pulls_labels(self, number: int, owner: str, repo: str, body: Any = None) -> Any:
        """替换 Pull Request 所有标签

        替换 Pull Request 所有标签
 需要在请求的body里填上数组，元素为标签的名字。如: ["performance", "bug"]

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/labels", number=number, owner=owner, repo=repo)
        return self._put(
            url,
            json=body,
        )

    def update_repos_pulls_merge(self, number: int, owner: str, repo: str, close_related_issue: Optional[bool] = None, description: Optional[str] = None, merge_method: Optional[str] = None, prune_source_branch: Optional[bool] = None, title: Optional[str] = None) -> Any:
        """合并Pull Request

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        Query/Form parameters:
        merge_method: 可选。合并PR的方法，merge（合并所有提交）、squash（扁平化分支合并）和rebase（变基并合并）。默认为merge。
        prune_source_branch: 可选。合并PR后是否删除源分支，默认false（不删除）
        close_related_issue: 可选。合并PR后是否关闭提到的issue，默认false（不关闭）
        title: 可选。合并标题，默认为PR的标题
        description: 可选。合并描述，默认为 "Merge pull request !{pr_id} from {author}/{source_branch}"，与页面显示的默认一致。

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/merge", number=number, owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "merge_method": merge_method,
                "prune_source_branch": prune_source_branch,
                "close_related_issue": close_related_issue,
                "title": title,
                "description": description,
            },
        )

    def update_repos_pulls_testers(self, number: int, owner: int, repo: int, reset_all: Optional[bool] = None) -> Any:
        """重置 Pull Request 测试 的状态

        Path parameters:
        number: 第几个PR，即本仓库PR的序数 (**必填**)
        owner:  (**必填**)
        repo:  (**必填**)
        Query/Form parameters:
        reset_all: 是否重置所有测试人，默认：false，只对管理员生效

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/testers", number=number, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "reset_all": reset_all,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_repos_pulls_all(self, owner: str, repo: str, assignee: Optional[str] = None, author: Optional[str] = None, base: Optional[str] = None, direction: Optional[str] = None, head: Optional[str] = None, labels: Optional[str] = None, max_pages: Optional[int] = None, milestone_number: Optional[int] = None, per_page: int = 100, since: Optional[str] = None, sort: Optional[str] = None, state: Optional[str] = None, tester: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_pulls()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_pulls` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls", owner=owner, repo=repo)
        params = {
            "state": state,            "head": head,            "base": base,            "sort": sort,            "since": since,            "direction": direction,            "milestone_number": milestone_number,            "labels": labels,            "author": author,            "assignee": assignee,            "tester": tester,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_pulls_comments_all(self, number: int, owner: str, repo: str, comment_type: Optional[str] = None, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_pulls_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_pulls_comments` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/comments", number=number, owner=owner, repo=repo)
        params = {
            "direction": direction,            "comment_type": comment_type,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_pulls_issues_all(self, number: int, owner: int, repo: int, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_pulls_issues()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_pulls_issues` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/issues", number=number, owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_pulls_labels_all(self, number: int, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_pulls_labels()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_pulls_labels` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/pulls/{number}/labels", number=number, owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )


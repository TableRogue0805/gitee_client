"""Labels API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class LabelsAPI(BaseAPI):
    """Gitee Labels API.

    All methods correspond to endpoints under the ``Labels`` group.
    """

    def create_repos_issues_labels(self, number: str, owner: str, repo: str, body: Any = None) -> Any:
        """创建Issue标签

        创建Issue标签
 需要在请求的body里填上数组，元素为标签的名字。如: ["performance", "bug"]

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/labels", number=number, owner=owner, repo=repo)
        return self._post(
            url,
            json=body,
        )

    def create_repos_labels(self, color: str, name: str, owner: str, repo: str) -> Any:
        """创建仓库任务标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        name: 标签名称 (**必填**)
        color: 标签颜色。为6位的数字，如: 000000 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/labels", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "name": name,
                "color": color,
            },
        )

    def create_repos_project_labels(self, owner: str, repo: str, body: Any = None) -> Any:
        """添加仓库标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/project_labels", owner=owner, repo=repo)
        return self._post(
            url,
            json=body,
        )

    def delete_repos_issues_labels(self, number: str, owner: str, repo: str) -> Any:
        """删除Issue所有标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/labels", number=number, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_issues_labels_2(self, name: str, number: str, owner: str, repo: str) -> Any:
        """删除Issue标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        name: 标签名称(批量删除用英文逗号分隔，如: bug,feature) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/labels/{name}", name=name, number=number, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_labels(self, name: str, owner: str, repo: str) -> Any:
        """删除一个仓库任务标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        name: 标签名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/labels/{name}", name=name, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_project_labels(self, owner: str, repo: str, body: Any = None) -> Any:
        """删除仓库标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/project_labels", owner=owner, repo=repo)
        return self._delete(
            url,
            json=body,
        )

    def get_enterprises_labels(self, enterprise: str, name: str) -> Any:
        """获取企业某个标签

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        name: 标签名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/labels/{name}", enterprise=enterprise, name=name)
        return self._get(
            url,
        )

    def get_repos_labels(self, name: str, owner: str, repo: str) -> Any:
        """根据标签名称获取单个标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        name: 标签名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/labels/{name}", name=name, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_enterprises_labels(self, enterprise: str) -> Any:
        """获取企业所有标签

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/labels", enterprise=enterprise)
        return self._get(
            url,
        )

    def list_repos_issues_labels(self, number: str, owner: str, repo: str) -> Any:
        """获取仓库任务的所有标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/labels", number=number, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_labels(self, owner: str, repo: str) -> Any:
        """获取仓库所有任务标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/labels", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_project_labels(self, owner: str, repo: str) -> Any:
        """获取仓库所有标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/project_labels", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def update_repos_issues_labels(self, number: str, owner: str, repo: str, body: Any = None) -> Any:
        """替换Issue所有标签

        替换Issue所有标签
 需要在请求的body里填上数组，元素为标签的名字。如: ["performance", "bug"]

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        number: Issue 编号(区分大小写，无需添加 # 号) (**必填**)
        Query/Form parameters:
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/issues/{number}/labels", number=number, owner=owner, repo=repo)
        return self._put(
            url,
            json=body,
        )

    def update_repos_labels(self, original_name: str, owner: str, repo: str, color: Optional[str] = None, name: Optional[str] = None) -> Any:
        """更新一个仓库任务标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        original_name: 标签原有名称 (**必填**)
        Query/Form parameters:
        name: 标签新名称
        color: 标签新颜色

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/labels/{original_name}", original_name=original_name, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "name": name,
                "color": color,
            },
        )

    def update_repos_project_labels(self, owner: str, repo: str, body: Any = None) -> Any:
        """替换所有仓库标签

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/project_labels", owner=owner, repo=repo)
        return self._put(
            url,
            json=body,
        )


"""Checks API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class ChecksAPI(BaseAPI):
    """Gitee Checks API.

    All methods correspond to endpoints under the ``Checks`` group.
    """

    def create_repos_check_runs(self, head_sha: str, name: str, owner: str, repo: str, completed_at: Optional[str] = None, conclusion: Optional[str] = None, details_url: Optional[str] = None, pull_request_id: Optional[int] = None, started_at: Optional[str] = None, status: Optional[str] = None, actions: Optional[dict] = None, output: Optional[dict] = None) -> Any:
        """创建检查项

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        pull_request_id: PullRequest ID
        details_url: 详情链接
        status: 状态
        started_at: 开始时间
        conclusion: 结论
        completed_at: 完成时间
        name: 名字 (**必填**)
        head_sha: 提交的 sha 值（必须是完整的） (**必填**)
        Other parameters:
        output_title: 标题 (**必填**)
        output_summary: 概论 (**必填**)
        output_text: 详细信息
        output_annotations_path: 路径 (**必填**)
        output_annotations_start_line: 开始行 (**必填**)
        output_annotations_end_line: 结束行 (**必填**)
        output_annotations_start_column: 开始列
        output_annotations_end_column: 结束列
        output_annotations_annotation_level: 注释级别 (**必填**)
        output_annotations_message: 注释信息 (**必填**)
        output_annotations_title: 标题
        output_annotations_raw_details: 详情内容
        output_images_alt: 注释 (**必填**)
        output_images_image_url: URL (**必填**)
        output_images_caption: 描述
        actions_label: 文本 (**必填**)
        actions_description: 描述 (**必填**)
        actions_identifier: 标识 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/check-runs", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "pull_request_id": pull_request_id,
                "details_url": details_url,
                "status": status,
                "started_at": started_at,
                "conclusion": conclusion,
                "completed_at": completed_at,
                "name": name,
                "head_sha": head_sha,
                **(actions if actions is not None else {}),
                **(output if output is not None else {}),
            },
        )

    def get_repos_check_runs(self, check_run_id: int, owner: str, repo: str) -> Any:
        """获取检查项详情

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        check_run_id: 检查项 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/check-runs/{check_run_id}", check_run_id=check_run_id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_check_runs_annotations(self, check_run_id: int, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取检查项代码注释

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        check_run_id: 检查项 ID (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations", check_run_id=check_run_id, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_commits_check_runs(self, owner: str, ref: str, repo: str, check_name: Optional[str] = None, filter: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, pull_request_id: Optional[int] = None, status: Optional[str] = None) -> Any:
        """获取某个提交的检查项

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        ref: 分支名\标签名\sha 值 (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        pull_request_id: 关联 pull request 的 ID
        check_name: 检查项名称
        status: 检查项状态
        filter: 最新的\全部

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{ref}/check-runs", owner=owner, ref=ref, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "pull_request_id": pull_request_id,
                "check_name": check_name,
                "status": status,
                "filter": filter,
            },
        )

    def update_repos_check_runs(self, check_run_id: int, owner: str, repo: str, completed_at: Optional[str] = None, conclusion: Optional[str] = None, details_url: Optional[str] = None, name: Optional[str] = None, pull_request_id: Optional[int] = None, started_at: Optional[str] = None, status: Optional[str] = None, actions: Optional[dict] = None, output: Optional[dict] = None) -> Any:
        """更新检查项

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        check_run_id: 检查项 ID (**必填**)
        Query/Form parameters:
        pull_request_id: 关联 pull_request 的 ID
        details_url: 详情链接
        status: 状态
        started_at: 开始时间
        conclusion: 结论
        completed_at: 完成时间
        name: 名字
        Other parameters:
        output_title: 标题 (**必填**)
        output_summary: 概论 (**必填**)
        output_text: 详细信息
        output_annotations_path: 路径 (**必填**)
        output_annotations_start_line: 开始行 (**必填**)
        output_annotations_end_line: 结束行 (**必填**)
        output_annotations_start_column: 开始列
        output_annotations_end_column: 结束列
        output_annotations_annotation_level: 注释级别 (**必填**)
        output_annotations_message: 注释信息 (**必填**)
        output_annotations_title: 标题
        output_annotations_raw_details: 详情内容
        output_images_alt: 注释 (**必填**)
        output_images_image_url: URL (**必填**)
        output_images_caption: 描述
        actions_label: 文本 (**必填**)
        actions_description: 描述 (**必填**)
        actions_identifier: 标识 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/check-runs/{check_run_id}", check_run_id=check_run_id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "pull_request_id": pull_request_id,
                "details_url": details_url,
                "status": status,
                "started_at": started_at,
                "conclusion": conclusion,
                "completed_at": completed_at,
                "name": name,
                **(actions if actions is not None else {}),
                **(output if output is not None else {}),
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_repos_check_runs_annotations_all(self, check_run_id: int, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_check_runs_annotations()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_check_runs_annotations` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations", check_run_id=check_run_id, owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_commits_check_runs_all(self, owner: str, ref: str, repo: str, check_name: Optional[str] = None, filter: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, pull_request_id: Optional[int] = None, status: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_commits_check_runs()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_commits_check_runs` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{ref}/check-runs", owner=owner, ref=ref, repo=repo)
        params = {
            "pull_request_id": pull_request_id,            "check_name": check_name,            "status": status,            "filter": filter,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


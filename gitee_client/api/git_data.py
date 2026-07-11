"""Git Data API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class GitDataAPI(BaseAPI):
    """Gitee Git Data API.

    All methods correspond to endpoints under the ``Git Data`` group.
    """

    def get_repos_git_blobs(self, owner: str, repo: str, sha: str) -> Any:
        """获取文件Blob

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        sha: 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/git/blobs/{sha}", owner=owner, repo=repo, sha=sha)
        return self._get(
            url,
        )

    def get_repos_git_trees(self, owner: str, repo: str, sha: str, recursive: Optional[int] = None) -> Any:
        """获取目录Tree

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        sha: 可以是分支名(如master)、Commit或者目录Tree的SHA值 (**必填**)
        Query/Form parameters:
        recursive: 赋值为1递归获取目录

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/git/trees/{sha}", owner=owner, repo=repo, sha=sha)
        return self._get(
            url,
            params={
                "recursive": recursive,
            },
        )

    def list_repos_git_gitee_metrics(self, owner: str, repo: str) -> Any:
        """获取 Gitee 指数

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/git/gitee_metrics", owner=owner, repo=repo)
        return self._get(
            url,
        )


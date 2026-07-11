"""Miscellaneous API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class MiscellaneousAPI(BaseAPI):
    """Gitee Miscellaneous API.

    All methods correspond to endpoints under the ``Miscellaneous`` group.
    """

    def create_markdown(self, text: str) -> Any:
        """渲染 Markdown 文本

        Query/Form parameters:
        text: Markdown 文本 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/markdown")
        return self._post(
            url,
            data={
                "text": text,
            },
        )

    def get_gitignore_templates(self, name: str) -> Any:
        """获取一个 .gitignore 模板

        Path parameters:
        name: .gitignore 模板名 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gitignore/templates/{name}", name=name)
        return self._get(
            url,
        )

    def get_gitignore_templates_raw(self, name: str) -> Any:
        """获取一个 .gitignore 模板原始文件

        Path parameters:
        name: .gitignore 模板名 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gitignore/templates/{name}/raw", name=name)
        return self._get(
            url,
        )

    def get_licenses(self, license: str) -> Any:
        """获取一个开源许可协议

        Path parameters:
        license: 协议名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/licenses/{license}", license=license)
        return self._get(
            url,
        )

    def get_licenses_raw(self, license: str) -> Any:
        """获取一个开源许可协议原始文件

        Path parameters:
        license: 协议名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/licenses/{license}/raw", license=license)
        return self._get(
            url,
        )

    def get_repos_license(self, owner: str, repo: str) -> Any:
        """获取一个仓库使用的开源许可协议

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/license", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_emojis(self) -> Any:
        """列出可使用的 Emoji


        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/emojis")
        return self._get(
            url,
        )

    def list_gitignore_templates(self) -> Any:
        """列出可使用的 .gitignore 模板


        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/gitignore/templates")
        return self._get(
            url,
        )

    def list_licenses(self) -> Any:
        """列出可使用的开源许可协议


        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/licenses")
        return self._get(
            url,
        )


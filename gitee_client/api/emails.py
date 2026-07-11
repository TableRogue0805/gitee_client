"""Emails API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class EmailsAPI(BaseAPI):
    """Gitee Emails API.

    All methods correspond to endpoints under the ``Emails`` group.
    """

    def list_emails(self) -> Any:
        """获取授权用户的全部邮箱


        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/emails")
        return self._get(
            url,
        )


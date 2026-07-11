"""Exception hierarchy for Gitee API client."""

from __future__ import annotations

import json
from typing import Any, Optional

import requests


class GiteeError(Exception):
    """Base exception for all Gitee client errors."""

    def __init__(self, message: str, *, response: Optional[requests.Response] = None) -> None:
        super().__init__(message)
        self.response = response


class GiteeAPIError(GiteeError):
    """Raised when the Gitee API returns an HTTP error.

    Attributes:
        status_code: HTTP status code from the response.
        error_message: Parsed error message from the response body (if available).
        response: The full ``requests.Response`` object.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error_message: str = "",
        response: Optional[requests.Response] = None,
    ) -> None:
        super().__init__(message, response=response)
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self) -> str:
        parts = [f"{self.status_code}"]
        if self.error_message:
            parts.append(str(self.error_message))
        return " ".join(parts)

    @classmethod
    def from_response(cls, response: requests.Response) -> GiteeAPIError:
        """Create the appropriate exception subclass from a response."""
        status = response.status_code
        error_message = ""

        try:
            body = response.json()
            if isinstance(body, dict):
                raw = body.get("error_description") or body.get("message") or body.get("error") or ""
                # Gitee may return error as a nested dict like {"base": ["msg"]}
                if isinstance(raw, dict):
                    # Flatten the first list value from the first key
                    try:
                        first_val = next(iter(raw.values()))
                        error_message = first_val[0] if isinstance(first_val, list) and first_val else str(first_val)
                    except (StopIteration, IndexError):
                        error_message = str(raw)
                else:
                    error_message = str(raw)
            elif isinstance(body, str):
                error_message = body
        except (json.JSONDecodeError, ValueError):
            error_message = response.text[:500] if response.text else ""

        if status == 401:
            return GiteeAuthError(error_message or "认证失败，请检查 access_token", status_code=status, error_message=error_message, response=response)
        elif status == 403:
            return GiteeAuthError(error_message or "没有权限执行此操作", status_code=status, error_message=error_message, response=response)
        elif status == 404:
            return GiteeNotFoundError(error_message or "资源不存在", status_code=status, error_message=error_message, response=response)
        elif status == 422:
            return GiteeValidationError(error_message or "请求数据不合法", status_code=status, error_message=error_message, response=response)
        elif status == 429:
            return GiteeRateLimitError(error_message or "请求频率超限", status_code=status, error_message=error_message, response=response)
        elif status >= 500:
            return GiteeServerError(error_message or "Gitee 服务器内部错误", status_code=status, error_message=error_message, response=response)
        else:
            return cls(error_message or f"HTTP {status}", status_code=status, error_message=error_message, response=response)


class GiteeAuthError(GiteeAPIError):
    """Raised for authentication/authorization errors (401, 403)."""

    pass


class GiteeNotFoundError(GiteeAPIError):
    """Raised when a requested resource does not exist (404)."""

    pass


class GiteeValidationError(GiteeAPIError):
    """Raised when the request data fails validation (422)."""

    pass


class GiteeRateLimitError(GiteeAPIError):
    """Raised when API rate limit is exceeded (429)."""

    pass


class GiteeServerError(GiteeAPIError):
    """Raised for server-side errors (5xx)."""

    pass

"""Gitee API v5 Python Client Library.

A comprehensive, easy-to-use client for the Gitee Open API v5.
Covers all 175 endpoints across 16 resource groups.

Usage::

    from gitee_client import GiteeClient

    client = GiteeClient()  # reads GITEE_ACCESS_TOKEN from env
    repos = client.repos.list()
    repo = client.repos.create(name="my-project", auto_init=True)
"""

from gitee_client.client import GiteeClient
from gitee_client.error import (
    GiteeError,
    GiteeAPIError,
    GiteeAuthError,
    GiteeNotFoundError,
    GiteeValidationError,
    GiteeRateLimitError,
    GiteeServerError,
)

__all__ = [
    "GiteeClient",
    "GiteeError",
    "GiteeAPIError",
    "GiteeAuthError",
    "GiteeNotFoundError",
    "GiteeValidationError",
    "GiteeRateLimitError",
    "GiteeServerError",
]
__version__ = "1.1.2"

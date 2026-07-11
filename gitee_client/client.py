"""Main GiteeClient class — the primary entry point for the library."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests

from gitee_client.error import GiteeAPIError
from gitee_client.pagination import PaginatedList, list_all


class GiteeClient:
    """A client for the Gitee Open API v5.

    Provides domain-specific accessors (``.repos``, ``.issues``, ``.pulls``, etc.)
    for all API endpoints.

    Args:
        access_token: Gitee personal access token.
            If not provided, reads from ``GITEE_ACCESS_TOKEN`` environment variable.
        base_url: Base URL for the Gitee API. Defaults to ``https://gitee.com/api/v5``.
        timeout: Request timeout in seconds (default 30).
        session: An existing ``requests.Session`` to use. If not provided, a new one is created.

    Basic usage::

        client = GiteeClient()
        repos = client.repos.list()
    """

    BASE_URL = "https://gitee.com/api"

    def __init__(
        self,
        access_token: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        timeout: int = 30,
        session: Optional[requests.Session] = None,
    ) -> None:
        self._access_token = access_token or os.environ.get("GITEE_ACCESS_TOKEN")
        self._base_url = (base_url or self.BASE_URL).rstrip("/")
        self._timeout = timeout
        self._session = session or requests.Session()
        self._session.headers.setdefault("Accept", "application/json")
        self._session.headers.setdefault("User-Agent", "gitee-client-python/1.0")

        # Lazily-loaded API modules
        self._repos = None
        self._issues = None
        self._pulls = None
        self._users = None
        self._organizations = None
        self._enterprises = None
        self._labels = None
        self._milestones = None
        self._gists = None
        self._activity = None
        self._webhooks = None
        self._checks = None
        self._search = None
        self._git_data = None
        self._emails = None
        self._misc = None

    # ── internal request machinery ─────────────────────────────────────────

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Any = None,
        files: Optional[Dict[str, Any]] = None,
        raw_response: bool = False,
    ) -> Any:
        """Send an HTTP request to the Gitee API.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE).
            path: API path relative to base URL (e.g. ``/v5/user/repos``).
            params: URL query parameters.
            data: Form-encoded body data.
            json: JSON-encoded body.
            files: Multipart file uploads.
            raw_response: If True, return the ``requests.Response`` object instead of parsed JSON.

        Returns:
            Parsed JSON response (dict or list), or ``None`` for 204/205 responses.

        Raises:
            GiteeAPIError: On any HTTP error (4xx, 5xx).
        """
        url = self._base_url + path

        # Inject access_token if not explicitly provided
        if self._access_token:
            if params is None:
                params = {}
            if "access_token" not in params:
                params["access_token"] = self._access_token

        # For POST/PUT/PATCH with form data, also add token to data if not in query
        if method in ("POST", "PUT", "PATCH") and data is not None and self._access_token:
            if "access_token" not in data:
                data["access_token"] = self._access_token

        response = self._session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=self._timeout,
        )

        if raw_response:
            return response

        if 200 <= response.status_code < 300:
            if response.status_code in (204, 205):
                return None
            return response.json()

        raise GiteeAPIError.from_response(response)

    # ── pagination helpers ──────────────────────────────────────────────────

    def paginate(
        self,
        path: str,
        *,
        per_page: int = 50,
        max_pages: Optional[int] = None,
        **params: Any,
    ) -> PaginatedList:
        """Return a page-by-page iterator for a paginated GET endpoint.

        Usage::

            for page in client.paginate("/v5/user/repos", per_page=50):
                for repo in page:
                    print(repo["full_name"])
        """
        return PaginatedList(self._get, path, per_page=per_page, max_pages=max_pages, **params)

    def list_all(
        self,
        path: str,
        *,
        per_page: int = 100,
        max_pages: Optional[int] = None,
        **params: Any,
    ):
        """Return a flat generator iterating over all items across pages.

        Usage::

            for repo in client.list_all("/v5/user/repos"):
                print(repo["full_name"])
        """
        return list_all(self._get, path, per_page=per_page, max_pages=max_pages, **params)

    def _get(self, path: str, *, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Simple GET request (used internally by pagination)."""
        return self._request("GET", path, params=params, **kwargs)

    # ── lazy accessors for API resource modules ─────────────────────────────

    @property
    def repos(self):
        """Access the Repositories API."""
        if self._repos is None:
            from gitee_client.api.repos import ReposAPI
            self._repos = ReposAPI(self)
        return self._repos

    @property
    def issues(self):
        """Access the Issues API."""
        if self._issues is None:
            from gitee_client.api.issues import IssuesAPI
            self._issues = IssuesAPI(self)
        return self._issues

    @property
    def pulls(self):
        """Access the Pull Requests API."""
        if self._pulls is None:
            from gitee_client.api.pulls import PullsAPI
            self._pulls = PullsAPI(self)
        return self._pulls

    @property
    def users(self):
        """Access the Users API."""
        if self._users is None:
            from gitee_client.api.users import UsersAPI
            self._users = UsersAPI(self)
        return self._users

    @property
    def organizations(self):
        """Access the Organizations API."""
        if self._organizations is None:
            from gitee_client.api.organizations import OrganizationsAPI
            self._organizations = OrganizationsAPI(self)
        return self._organizations

    @property
    def enterprises(self):
        """Access the Enterprises API."""
        if self._enterprises is None:
            from gitee_client.api.enterprises import EnterprisesAPI
            self._enterprises = EnterprisesAPI(self)
        return self._enterprises

    @property
    def labels(self):
        """Access the Labels API."""
        if self._labels is None:
            from gitee_client.api.labels import LabelsAPI
            self._labels = LabelsAPI(self)
        return self._labels

    @property
    def milestones(self):
        """Access the Milestones API."""
        if self._milestones is None:
            from gitee_client.api.milestones import MilestonesAPI
            self._milestones = MilestonesAPI(self)
        return self._milestones

    @property
    def gists(self):
        """Access the Gists API."""
        if self._gists is None:
            from gitee_client.api.gists import GistsAPI
            self._gists = GistsAPI(self)
        return self._gists

    @property
    def activity(self):
        """Access the Activity API."""
        if self._activity is None:
            from gitee_client.api.activity import ActivityAPI
            self._activity = ActivityAPI(self)
        return self._activity

    @property
    def webhooks(self):
        """Access the Webhooks API."""
        if self._webhooks is None:
            from gitee_client.api.webhooks import WebhooksAPI
            self._webhooks = WebhooksAPI(self)
        return self._webhooks

    @property
    def checks(self):
        """Access the Checks API."""
        if self._checks is None:
            from gitee_client.api.checks import ChecksAPI
            self._checks = ChecksAPI(self)
        return self._checks

    @property
    def search(self):
        """Access the Search API."""
        if self._search is None:
            from gitee_client.api.search import SearchAPI
            self._search = SearchAPI(self)
        return self._search

    @property
    def git_data(self):
        """Access the Git Data API."""
        if self._git_data is None:
            from gitee_client.api.git_data import GitDataAPI
            self._git_data = GitDataAPI(self)
        return self._git_data

    @property
    def emails(self):
        """Access the Emails API."""
        if self._emails is None:
            from gitee_client.api.emails import EmailsAPI
            self._emails = EmailsAPI(self)
        return self._emails

    @property
    def misc(self):
        """Access the Miscellaneous API (emojis, gitignore, licenses, markdown)."""
        if self._misc is None:
            from gitee_client.api.miscellaneous import MiscellaneousAPI
            self._misc = MiscellaneousAPI(self)
        return self._misc

    # ── context manager ─────────────────────────────────────────────────────

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()

    def __enter__(self) -> GiteeClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

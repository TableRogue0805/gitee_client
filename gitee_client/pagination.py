"""Pagination support for Gitee API list endpoints."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class PaginatedList(Iterator[List[Any]]):
    """Iterator that automatically handles Gitee API pagination.

    Gitee uses ``page`` and ``per_page`` query parameters for pagination.
    This iterator fetches pages one at a time as you iterate.

    Usage::

        for page in PaginatedList(client._get, "/v5/user/repos", per_page=50):
            for repo in page:
                print(repo["full_name"])
    """

    def __init__(
        self,
        fetch_fn: Callable[..., Any],
        path: str,
        *,
        per_page: int = 50,
        max_pages: Optional[int] = None,
        **params: Any,
    ) -> None:
        """Initialize the paginated iterator.

        Args:
            fetch_fn: The function to call for each page (e.g. ``client._get``).
            path: The API path to request.
            per_page: Number of items per page (max 100, default 50).
            max_pages: Maximum number of pages to fetch (None = unlimited).
            **params: Additional query parameters to pass with each request.
        """
        self._fetch_fn = fetch_fn
        self._path = path
        self._per_page = min(per_page, 100)
        self._max_pages = max_pages
        self._params = params
        self._current_page = 1
        self._pages_fetched = 0
        self._exhausted = False

    def __iter__(self) -> PaginatedList:
        return self

    def __next__(self) -> List[Any]:
        if self._exhausted:
            raise StopIteration
        if self._max_pages is not None and self._pages_fetched >= self._max_pages:
            raise StopIteration

        page_params = {
            **self._params,
            "page": self._current_page,
            "per_page": self._per_page,
        }
        result = self._fetch_fn(self._path, params=page_params)

        if isinstance(result, list):
            data = result
        elif isinstance(result, dict) and "items" in result:
            data = result["items"]
        elif isinstance(result, dict):
            data = result.get("data", []) or result.get("list", [])
        else:
            data = []

        self._current_page += 1
        self._pages_fetched += 1

        if not data or len(data) < self._per_page:
            self._exhausted = True

        return data


def list_all(
    fetch_fn: Callable[..., Any],
    path: str,
    *,
    per_page: int = 100,
    max_pages: Optional[int] = None,
    **params: Any,
) -> Iterator[Any]:
    """Convenience generator that yields individual items across all pages.

    Usage::

        for repo in list_all(client._get, "/v5/user/repos"):
            print(repo["full_name"])
    """
    for page in PaginatedList(fetch_fn, path, per_page=per_page, max_pages=max_pages, **params):
        yield from page

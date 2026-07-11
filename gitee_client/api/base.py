"""Base API class providing shared HTTP communication methods."""

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from gitee_client.error import GiteeAPIError
from gitee_client.utils import filter_none_params


class BaseAPI:
    """Base class for all API resource modules.

    Provides ``_get``, ``_post``, ``_put``, ``_patch``, ``_delete`` methods
    that delegate to the client's internal ``_request`` method.

    Subclasses are instantiated with a reference to the ``GiteeClient``,
    which manages the HTTP session, authentication, and base URL.
    """

    def __init__(self, client: Any) -> None:
        """Initialize with a reference to the GiteeClient.

        Args:
            client: The ``GiteeClient`` instance that owns this API module.
        """
        self._client = client

    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Send a GET request."""
        return self._client._request("GET", path, params=filter_none_params(params or {}), **kwargs)

    def _post(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Any = None,
        files: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Send a POST request."""
        return self._client._request(
            "POST", path,
            params=filter_none_params(params or {}),
            data=filter_none_params(data or {}) if data else None,
            json=json,
            files=files,
            **kwargs,
        )

    def _put(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Any = None,
        **kwargs: Any,
    ) -> Any:
        """Send a PUT request."""
        return self._client._request(
            "PUT", path,
            params=filter_none_params(params or {}),
            data=filter_none_params(data or {}) if data else None,
            json=json,
            **kwargs,
        )

    def _patch(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Any = None,
        **kwargs: Any,
    ) -> Any:
        """Send a PATCH request."""
        return self._client._request(
            "PATCH", path,
            params=filter_none_params(params or {}),
            data=filter_none_params(data or {}) if data else None,
            json=json,
            **kwargs,
        )

    def _delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Send a DELETE request."""
        return self._client._request(
            "DELETE", path,
            params=filter_none_params(params or {}),
            data=filter_none_params(data or {}) if data else None,
            **kwargs,
        )

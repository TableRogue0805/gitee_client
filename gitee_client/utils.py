"""Utility functions for URL building and parameter handling."""

from __future__ import annotations

import re
from typing import Any, Dict, Optional


def build_url(base_path: str, path_template: str, **path_params: Any) -> str:
    """Fill path template parameters to build a full URL path.

    Args:
        base_path: The API base path (e.g. ``/api/v5``).
        path_template: The Swagger path template (e.g. ``/v5/repos/{owner}/{repo}``).
        **path_params: Values for each path parameter.

    Returns:
        The complete URL path.

    Example::

        >>> build_url("/api/v5", "/v5/repos/{owner}/{repo}", owner="foo", repo="bar")
        '/api/v5/repos/foo/bar'
    """
    url = base_path + path_template
    # Replace {param} with actual values
    for key, value in path_params.items():
        url = url.replace(f"{{{key}}}", str(value))

    # Handle optional path segments like (/{path})
    url = re.sub(r"\(\{([^}]+)\}\)", r"{\1}", url)

    return url


def filter_none_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """Remove ``None`` values from a parameter dict.

    This is the standard behavior: optional parameters that are not set
    should simply be omitted from the request.
    """
    return {k: v for k, v in params.items() if v is not None}

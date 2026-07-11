"""Activity API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class ActivityAPI(BaseAPI):
    """Gitee Activity API.

    All methods correspond to endpoints under the ``Activity`` group.
    """

    def create_notification_messages(self, content: str, username: str) -> Any:
        """发送私信给指定用户

        Query/Form parameters:
        username: 用户名(username/login) (**必填**)
        content: 私信内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/messages")
        return self._post(
            url,
            data={
                "username": username,
                "content": content,
            },
        )

    def delete_user_subscriptions(self, owner: str, repo: str) -> Any:
        """取消 watch 一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/subscriptions/{owner}/{repo}", owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def get_notification_messages(self, id: str) -> Any:
        """获取一条私信

        Path parameters:
        id: 私信的 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/messages/{id}", id=id)
        return self._get(
            url,
        )

    def get_notification_threads(self, id: str) -> Any:
        """获取一条通知

        Path parameters:
        id: 通知的 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/threads/{id}", id=id)
        return self._get(
            url,
        )

    def get_notifications_count(self, unread: Optional[bool] = None) -> Any:
        """获取授权用户的通知数

        Query/Form parameters:
        unread: 是否只获取未读消息，默认：否

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/count")
        return self._get(
            url,
            params={
                "unread": unread,
            },
        )

    def get_user_subscriptions(self, owner: str, repo: str) -> Any:
        """检查授权用户是否 watch 了一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/subscriptions/{owner}/{repo}", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_users_events_orgs(self, org: str, username: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出用户所属组织的动态

        Path parameters:
        username: 用户名(username/login) (**必填**)
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/events/orgs/{org}", org=org, username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_networks_events(self, owner: str, repo: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出仓库的所有公开动态

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/networks/{owner}/{repo}/events", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_notification_messages(self, before: Optional[str] = None, ids: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, since: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """列出授权用户的所有私信

        Query/Form parameters:
        unread: 是否只显示未读私信，默认：否
        since: 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601
        before: 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601
        ids: 指定一组私信 ID，以 , 分隔
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/messages")
        return self._get(
            url,
            params={
                "unread": unread,
                "since": since,
                "before": before,
                "ids": ids,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_notification_threads(self, before: Optional[str] = None, ids: Optional[str] = None, page: Optional[int] = None, participating: Optional[bool] = None, per_page: Optional[int] = None, since: Optional[str] = None, type: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """列出授权用户的所有通知

        Query/Form parameters:
        unread: 是否只获取未读消息，默认：否
        participating: 是否只获取自己直接参与的消息，默认：否
        type: 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知
        since: 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601
        before: 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601
        ids: 指定一组通知 ID，以 , 分隔
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/threads")
        return self._get(
            url,
            params={
                "unread": unread,
                "participating": participating,
                "type": type,
                "since": since,
                "before": before,
                "ids": ids,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_orgs_events(self, org: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出组织的公开动态

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/events", org=org)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_repos_events(self, owner: str, repo: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出仓库的所有动态

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/events", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_repos_notifications(self, owner: str, repo: str, before: Optional[str] = None, ids: Optional[str] = None, page: Optional[int] = None, participating: Optional[bool] = None, per_page: Optional[int] = None, since: Optional[str] = None, type: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """列出一个仓库里的通知

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        unread: 是否只获取未读消息，默认：否
        participating: 是否只获取自己直接参与的消息，默认：否
        type: 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知
        since: 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601
        before: 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601
        ids: 指定一组通知 ID，以 , 分隔
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/notifications", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "unread": unread,
                "participating": participating,
                "type": type,
                "since": since,
                "before": before,
                "ids": ids,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_subscribers(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """列出 watch 了仓库的用户

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/subscribers", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_subscriptions(self, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """列出授权用户 watch 了的仓库

        Query/Form parameters:
        sort: 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间
        direction: 按递增(asc)或递减(desc)排序，默认：递减
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/subscriptions")
        return self._get(
            url,
            params={
                "sort": sort,
                "direction": direction,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_users_events(self, username: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出用户的动态

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/events", username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_users_events_public(self, username: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出用户的公开动态

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/events/public", username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_users_received_events(self, username: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出一个用户收到的动态

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/received_events", username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_users_received_events_public(self, username: str, limit: Optional[int] = None, prev_id: Optional[int] = None) -> Any:
        """列出一个用户收到的公开动态

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/received_events/public", username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
            },
        )

    def list_users_subscriptions(self, username: str, direction: Optional[str] = None, limit: Optional[int] = None, prev_id: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """列出用户 watch 了的仓库

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        prev_id: 滚动列表的最后一条记录的id
        limit: 滚动列表每页的数量，最大为 100
        sort: 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间
        direction: 按递增(asc)或递减(desc)排序，默认：递减

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/subscriptions", username=username)
        return self._get(
            url,
            params={
                "prev_id": prev_id,
                "limit": limit,
                "sort": sort,
                "direction": direction,
            },
        )

    def update_notification_messages(self, ids: Optional[str] = None) -> Any:
        """标记所有私信为已读

        Query/Form parameters:
        ids: 指定一组私信 ID，以 , 分隔

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/messages")
        return self._put(
            url,
            data={
                "ids": ids,
            },
        )

    def update_notification_messages_2(self, id: str) -> Any:
        """标记一条私信为已读

        Path parameters:
        id: 私信的 ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/messages/{id}", id=id)
        return self._patch(
            url,
        )

    def update_notification_threads(self, ids: Optional[str] = None) -> Any:
        """标记所有通知为已读

        Query/Form parameters:
        ids: 指定一组通知 ID，以 , 分隔

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/threads")
        return self._put(
            url,
            data={
                "ids": ids,
            },
        )

    def update_notification_threads_2(self, id: str) -> Any:
        """标记一条通知为已读

        Path parameters:
        id: 通知的 ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/notifications/threads/{id}", id=id)
        return self._patch(
            url,
        )

    def update_repos_notifications(self, owner: str, repo: str, ids: Optional[str] = None) -> Any:
        """标记一个仓库里的通知为已读

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        ids: 指定一组通知 ID，以 , 分隔

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/notifications", owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "ids": ids,
            },
        )

    def update_user_subscriptions(self, owner: str, repo: str, watch_type: str) -> Any:
        """watch 一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        watch_type: watch策略, watching: 关注所有动态, ignoring: 关注但不提醒动态 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/subscriptions/{owner}/{repo}", owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "watch_type": watch_type,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_notification_messages_all(self, before: Optional[str] = None, ids: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, since: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """Iterate over all pages of ``list_notification_messages()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_notification_messages` for parameter documentation.
        """
        url = build_url("", "/v5/notifications/messages")
        params = {
            "unread": unread,            "since": since,            "before": before,            "ids": ids,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_notification_threads_all(self, before: Optional[str] = None, ids: Optional[str] = None, max_pages: Optional[int] = None, participating: Optional[bool] = None, per_page: int = 100, since: Optional[str] = None, type: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """Iterate over all pages of ``list_notification_threads()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_notification_threads` for parameter documentation.
        """
        url = build_url("", "/v5/notifications/threads")
        params = {
            "unread": unread,            "participating": participating,            "type": type,            "since": since,            "before": before,            "ids": ids,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_notifications_all(self, owner: str, repo: str, before: Optional[str] = None, ids: Optional[str] = None, max_pages: Optional[int] = None, participating: Optional[bool] = None, per_page: int = 100, since: Optional[str] = None, type: Optional[str] = None, unread: Optional[bool] = None) -> Any:
        """Iterate over all pages of ``list_repos_notifications()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_notifications` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/notifications", owner=owner, repo=repo)
        params = {
            "unread": unread,            "participating": participating,            "type": type,            "since": since,            "before": before,            "ids": ids,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_subscribers_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_subscribers()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_subscribers` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/subscribers", owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_user_subscriptions_all(self, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_user_subscriptions()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_subscriptions` for parameter documentation.
        """
        url = build_url("", "/v5/user/subscriptions")
        params = {
            "sort": sort,            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )


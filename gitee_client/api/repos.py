"""Repositories API endpoints."""

from __future__ import annotations

from typing import Any, Optional

from gitee_client.api.base import BaseAPI
from gitee_client.pagination import list_all
from gitee_client.utils import build_url


class ReposAPI(BaseAPI):
    """Gitee Repositories API.

    All methods correspond to endpoints under the ``Repositories`` group.
    """

    def create_enterprises_repos(self, enterprise: str, name: str, auto_init: Optional[bool] = None, can_comment: Optional[bool] = None, description: Optional[str] = None, gitignore_template: Optional[str] = None, has_issues: Optional[bool] = None, has_wiki: Optional[bool] = None, homepage: Optional[str] = None, license_template: Optional[str] = None, members: Optional[str] = None, outsourced: Optional[bool] = None, path: Optional[str] = None, private: Optional[int] = None, project_creator: Optional[str] = None) -> Any:
        """创建企业仓库

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        name: 仓库名称 (**必填**)
        description: 仓库描述
        homepage: 主页(eg: https://gitee.com)
        has_issues: 允许提Issue与否。默认: 允许(true)
        has_wiki: 提供Wiki与否。默认: 提供(true)
        can_comment: 允许用户对仓库进行评论。默认： 允许(true)
        auto_init: 值为true时则会用README初始化仓库。默认: 不初始化(false)
        gitignore_template: Git Ignore模版
        license_template: License模版
        path: 仓库路径
        private: 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)。默认: 0
        outsourced: 值为true值为外包仓库, false值为内部仓库。默认: 内部仓库(false)
        project_creator: 负责人的username
        members: 用逗号分开的仓库成员。如: member1,member2

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/repos", enterprise=enterprise)
        return self._post(
            url,
            data={
                "name": name,
                "description": description,
                "homepage": homepage,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "can_comment": can_comment,
                "auto_init": auto_init,
                "gitignore_template": gitignore_template,
                "license_template": license_template,
                "path": path,
                "private": private,
                "outsourced": outsourced,
                "project_creator": project_creator,
                "members": members,
            },
        )

    def create_orgs_repos(self, name: str, org: str, auto_init: Optional[bool] = None, can_comment: Optional[bool] = None, description: Optional[str] = None, gitignore_template: Optional[str] = None, has_issues: Optional[bool] = None, has_wiki: Optional[bool] = None, homepage: Optional[str] = None, license_template: Optional[str] = None, path: Optional[str] = None, private: Optional[bool] = None, public: Optional[int] = None) -> Any:
        """创建组织仓库

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        name: 仓库名称 (**必填**)
        description: 仓库描述
        homepage: 主页(eg: https://gitee.com)
        has_issues: 允许提Issue与否。默认: 允许(true)
        has_wiki: 提供Wiki与否。默认: 提供(true)
        can_comment: 允许用户对仓库进行评论。默认： 允许(true)
        public: 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)，注：与private互斥，以public为主。
        private: 仓库公开或私有。默认: 公开(false)，注：与public互斥，以public为主。
        auto_init: 值为true时则会用README初始化仓库。默认: 不初始化(false)
        gitignore_template: Git Ignore模版
        license_template: License模版
        path: 仓库路径

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/repos", org=org)
        return self._post(
            url,
            data={
                "name": name,
                "description": description,
                "homepage": homepage,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "can_comment": can_comment,
                "public": public,
                "private": private,
                "auto_init": auto_init,
                "gitignore_template": gitignore_template,
                "license_template": license_template,
                "path": path,
            },
        )

    def create_repos_baidu_statistic_key(self, owner: str, repo: str, key: Optional[str] = None) -> Any:
        """设置/更新仓库的百度统计 key

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        key: 通过百度统计页面获取的 hm.js? 后面的 key

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/baidu_statistic_key", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "key": key,
            },
        )

    def create_repos_branches(self, branch_name: str, owner: str, refs: str, repo: str) -> Any:
        """创建分支

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        refs: 起点名称, 默认：master (**必填**)
        branch_name: 新创建的分支名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "refs": refs,
                "branch_name": branch_name,
            },
        )

    def create_repos_commits(self, owner: str, repo: str, body: Any = None) -> Any:
        """提交多个文件变更

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        body: Request body payload.

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits", owner=owner, repo=repo)
        return self._post(
            url,
            json=body,
        )

    def create_repos_commits_comments(self, body: str, owner: str, repo: str, sha: str, path: Optional[str] = None, position: Optional[int] = None) -> Any:
        """创建Commit评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        sha: 评论的sha值 (**必填**)
        Query/Form parameters:
        body: 评论的内容 (**必填**)
        path: 文件的相对路径
        position: Diff的相对行数

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{sha}/comments", owner=owner, repo=repo, sha=sha)
        return self._post(
            url,
            data={
                "body": body,
                "path": path,
                "position": position,
            },
        )

    def create_repos_contents(self, content: str, message: str, owner: str, path: str, repo: str, branch: Optional[str] = None, author: Optional[dict] = None, committer: Optional[dict] = None) -> Any:
        """新建文件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径 (**必填**)
        Query/Form parameters:
        content: 文件内容, 要用 base64 编码 (**必填**)
        message: 提交信息 (**必填**)
        branch: 分支名称。默认为仓库对默认分支
        Other parameters:
        committer_name: Committer的名字，默认为当前用户的名字
        committer_email: Committer的邮箱，默认为当前用户的邮箱
        author_name: Author的名字，默认为当前用户的名字
        author_email: Author的邮箱，默认为当前用户的邮箱

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/contents/{path}", owner=owner, path=path, repo=repo)
        return self._post(
            url,
            data={
                "content": content,
                "message": message,
                "branch": branch,
                **(author if author is not None else {}),
                **(committer if committer is not None else {}),
            },
        )

    def create_repos_forks(self, owner: str, repo: str, name: Optional[str] = None, organization: Optional[str] = None, path: Optional[str] = None) -> Any:
        """Fork一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        organization: 组织空间完整地址，不填写默认Fork到用户个人空间地址
        name: fork 后仓库名称。默认: 源仓库名称
        path: fork 后仓库地址。默认: 源仓库地址

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/forks", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "organization": organization,
                "name": name,
                "path": path,
            },
        )

    def create_repos_keys(self, key: str, owner: str, repo: str, title: str) -> Any:
        """为仓库添加公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        key: 公钥内容 (**必填**)
        title: 公钥名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "key": key,
                "title": title,
            },
        )

    def create_repos_open(self, owner: str, repo: str) -> Any:
        """开通Gitee Go

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库path (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/open", owner=owner, repo=repo)
        return self._post(
            url,
        )

    def create_repos_releases(self, body: str, name: str, owner: str, repo: str, tag_name: str, target_commitish: str, prerelease: Optional[bool] = None) -> Any:
        """创建仓库Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        tag_name: Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4 (**必填**)
        name: Release 名称 (**必填**)
        body: Release 描述 (**必填**)
        prerelease: 是否为预览版本。默认: false（非预览版本）
        target_commitish: 分支名称或者commit SHA, 默认是当前默认分支 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "tag_name": tag_name,
                "name": name,
                "body": body,
                "prerelease": prerelease,
                "target_commitish": target_commitish,
            },
        )

    def create_repos_releases_attach_files(self, file: Any, owner: str, release_id: int, repo: str) -> Any:
        """上传附件到仓库指定 Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        release_id: 发行版本的ID (**必填**)
        Query/Form parameters:
        file: 上传的文件 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files", owner=owner, release_id=release_id, repo=repo)
        return self._post(
            url,
            files={'file': file} if file else None,
        )

    def create_repos_tags(self, owner: str, refs: str, repo: str, tag_name: str, tag_message: Optional[str] = None) -> Any:
        """创建一个仓库的 Tag

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        refs: 起点名称, 默认：master (**必填**)
        tag_name: 新创建的标签名称 (**必填**)
        tag_message: Tag 描述, 默认为空

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/tags", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "refs": refs,
                "tag_name": tag_name,
                "tag_message": tag_message,
            },
        )

    def create_repos_traffic_data(self, owner: str, repo: str, end_day: Optional[str] = None, start_day: Optional[str] = None) -> Any:
        """获取最近30天的七日以内访问量

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        start_day: 访问量的开始时间，默认今天，格式：yyyy-MM-dd
        end_day: 访问量的结束时间，默认七天前，格式：yyyy-MM-dd

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/traffic-data", owner=owner, repo=repo)
        return self._post(
            url,
            data={
                "start_day": start_day,
                "end_day": end_day,
            },
        )

    def create_user_repos(self, name: str, auto_init: Optional[bool] = None, can_comment: Optional[bool] = None, description: Optional[str] = None, enterprise: Optional[str] = None, gitignore_template: Optional[str] = None, has_issues: Optional[bool] = None, has_wiki: Optional[bool] = None, homepage: Optional[str] = None, license_template: Optional[str] = None, members: Optional[str] = None, model: Optional[str] = None, namespace: Optional[str] = None, outsourced: Optional[bool] = None, path: Optional[str] = None, private: Optional[bool] = None, project_creator: Optional[str] = None, public: Optional[int] = None, template_apply_scope: Optional[str] = None) -> Any:
        """创建一个仓库

        Query/Form parameters:
        name: 仓库名称 (**必填**)
        description: 仓库描述
        homepage: 主页(eg: https://gitee.com)
        has_issues: 允许提Issue与否。默认: 允许(true)
        has_wiki: 提供Wiki与否。默认: 提供(true)
        can_comment: 允许用户对仓库进行评论。默认： 允许(true)
        auto_init: 值为true时则会用README初始化仓库。默认: 不初始化(false)
        gitignore_template: Git Ignore模版
        license_template: License模版
        path: 仓库路径
        namespace: 归属路径 path，不传则创建到个人名下
        public: 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)，注：与private互斥，以public为主。
        outsourced: 值为true值为外包仓库, false值为内部仓库。默认: 内部仓库(false)
        project_creator: 负责人的username
        members: 用逗号分开的仓库成员。如: member1,member2
        template_apply_scope: 模版仓库运用范围。code: 代码；setting: 配置；code,settings：代码和配置
        model: 分支模型id
        enterprise: 企业的路径(path/login),仓库组必传参数
        private: 仓库是否私有，注：与public互斥，以public为主。个人创建仓库仅支持私有

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/repos")
        return self._post(
            url,
            data={
                "name": name,
                "description": description,
                "homepage": homepage,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "can_comment": can_comment,
                "auto_init": auto_init,
                "gitignore_template": gitignore_template,
                "license_template": license_template,
                "path": path,
                "namespace": namespace,
                "public": public,
                "outsourced": outsourced,
                "project_creator": project_creator,
                "members": members,
                "template_apply_scope": template_apply_scope,
                "model": model,
                "enterprise": enterprise,
                "private": private,
            },
        )

    def delete_repos(self, owner: str, repo: str) -> Any:
        """删除一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}", owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_baidu_statistic_key(self, owner: str, repo: str) -> Any:
        """删除仓库的百度统计 key

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/baidu_statistic_key", owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_branches_protection(self, branch: str, owner: str, repo: str) -> Any:
        """取消保护分支的设置

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        branch: 分支名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/{branch}/protection", branch=branch, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_branches_setting(self, owner: str, repo: str, wildcard: str) -> Any:
        """删除保护分支规则

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        wildcard: 分支/通配符 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/{wildcard}/setting", owner=owner, repo=repo, wildcard=wildcard)
        return self._delete(
            url,
        )

    def delete_repos_collaborators(self, owner: str, repo: str, username: str) -> Any:
        """移除仓库成员

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators/{username}", owner=owner, repo=repo, username=username)
        return self._delete(
            url,
        )

    def delete_repos_comments(self, id: int, owner: str, repo: str) -> Any:
        """删除Commit评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/comments/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_contents(self, message: str, owner: str, path: str, repo: str, sha: str, branch: Optional[str] = None, author: Optional[dict] = None, committer: Optional[dict] = None) -> Any:
        """删除文件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径 (**必填**)
        Query/Form parameters:
        sha: 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 (**必填**)
        message: 提交信息 (**必填**)
        branch: 分支名称。默认为仓库对默认分支
        Other parameters:
        committer_name: Committer的名字，默认为当前用户的名字
        committer_email: Committer的邮箱，默认为当前用户的邮箱
        author_name: Author的名字，默认为当前用户的名字
        author_email: Author的邮箱，默认为当前用户的邮箱

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/contents/{path}", owner=owner, path=path, repo=repo)
        return self._delete(
            url,
            params={
                "sha": sha,
                "message": message,
                "branch": branch,
            },
        )

    def delete_repos_keys(self, id: int, owner: str, repo: str) -> Any:
        """删除一个仓库公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 公钥 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_keys_enable(self, id: int, owner: str, repo: str) -> Any:
        """停用仓库公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 公钥 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/enable/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_releases(self, id: int, owner: str, repo: str) -> Any:
        """删除仓库Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id:  (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{id}", id=id, owner=owner, repo=repo)
        return self._delete(
            url,
        )

    def delete_repos_releases_attach_files(self, attach_file_id: int, owner: str, release_id: int, repo: str) -> Any:
        """删除仓库下指定 Release 的指定附件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        release_id:  (**必填**)
        attach_file_id:  (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files/{attach_file_id}", attach_file_id=attach_file_id, owner=owner, release_id=release_id, repo=repo)
        return self._delete(
            url,
        )

    def get_repos(self, owner: str, repo: str) -> Any:
        """获取用户的某个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_branches(self, branch: str, owner: str, repo: str) -> Any:
        """获取单个分支

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        branch: 分支名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/{branch}", branch=branch, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_collaborators(self, owner: str, repo: str, username: str) -> Any:
        """判断用户是否为仓库成员

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators/{username}", owner=owner, repo=repo, username=username)
        return self._get(
            url,
        )

    def get_repos_collaborators_permission(self, owner: str, repo: str, username: str) -> Any:
        """查看仓库成员的权限

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        username: 用户名(username/login) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators/{username}/permission", owner=owner, repo=repo, username=username)
        return self._get(
            url,
        )

    def get_repos_comments(self, id: int, owner: str, repo: str) -> Any:
        """获取仓库的某条Commit评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/comments/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_commits(self, owner: str, repo: str, sha: str) -> Any:
        """仓库的某个提交

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        sha: 提交的SHA值或者分支名 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{sha}", owner=owner, repo=repo, sha=sha)
        return self._get(
            url,
        )

    def get_repos_compare____(self, base: str, head: str, owner: str, repo: str, straight: Optional[bool] = None, suffix: Optional[str] = None) -> Any:
        """Commits 对比

        Commits 对比
 返回的 commits 数量限制在 100 以内

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        base: 对比的起点。Commit SHA、分支名或标签名 (**必填**)
        head: 对比的终点。Commit SHA、分支名或标签名 (**必填**)
        Query/Form parameters:
        straight: 是否直对比。默认 false
        suffix: 按照文件后缀过滤文件，如 `.txt`。只影响 `files`

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/compare/{base}...{head}", base=base, head=head, owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "straight": straight,
                "suffix": suffix,
            },
        )

    def get_repos_contents(self, owner: str, path: str, repo: str, ref: Optional[str] = None) -> Any:
        """获取仓库具体路径下的内容

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径 (**必填**)
        Query/Form parameters:
        ref: 分支、tag或commit。默认: 仓库的默认分支(通常是master)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/contents(/{path})", owner=owner, path=path, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
            },
        )

    def get_repos_keys(self, id: int, owner: str, repo: str) -> Any:
        """获取仓库的单个公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 公钥 ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_readme(self, owner: str, repo: str, ref: Optional[str] = None) -> Any:
        """获取仓库README

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        ref: 分支、tag或commit。默认: 仓库的默认分支(通常是master)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/readme", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
            },
        )

    def get_repos_releases(self, id: int, owner: str, repo: str) -> Any:
        """获取仓库的单个Releases

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 发行版本的ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{id}", id=id, owner=owner, repo=repo)
        return self._get(
            url,
        )

    def get_repos_releases_attach_files(self, attach_file_id: int, owner: str, release_id: int, repo: str) -> Any:
        """获取仓库下指定 Release 的单个附件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        release_id: 发行版本的ID (**必填**)
        attach_file_id: 发行版本下的附件ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files/{attach_file_id}", attach_file_id=attach_file_id, owner=owner, release_id=release_id, repo=repo)
        return self._get(
            url,
        )

    def get_repos_releases_tags(self, owner: str, repo: str, tag: str) -> Any:
        """根据Tag名称获取仓库的Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        tag: Tag 名称 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/tags/{tag}", owner=owner, repo=repo, tag=tag)
        return self._get(
            url,
        )

    def get_repos_tarball(self, owner: str, repo: str, expected_path: Optional[str] = None, ref: Optional[str] = None) -> Any:
        """下载仓库 tar.gz

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        ref: 分支、tag或commit。默认: 仓库的默认分支(通常是master)
        expected_path: 指定的目录或文件

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/tarball", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
                "expected_path": expected_path,
            },
        )

    def get_repos_zipball(self, owner: str, repo: str, expected_path: Optional[str] = None, ref: Optional[str] = None) -> Any:
        """下载仓库 zip

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        ref: 分支、tag或commit。默认: 仓库的默认分支(通常是master)
        expected_path: 指定的目录或文件

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/zipball", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
                "expected_path": expected_path,
            },
        )

    def list_enterprises_repos(self, enterprise: str, direct: Optional[bool] = None, page: Optional[int] = None, per_page: Optional[int] = None, search: Optional[str] = None, type: Optional[str] = None) -> Any:
        """获取企业的所有仓库

        Path parameters:
        enterprise: 企业的路径(path/login) (**必填**)
        Query/Form parameters:
        search: 搜索字符串
        type: 筛选仓库的类型，可以是 all, public, internal, private。默认: all
        direct: 只获取直属仓库，默认: false
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/enterprises/{enterprise}/repos", enterprise=enterprise)
        return self._get(
            url,
            params={
                "search": search,
                "type": type,
                "direct": direct,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_orgs_repos(self, org: str, page: Optional[int] = None, per_page: Optional[int] = None, type: Optional[str] = None) -> Any:
        """获取一个组织的仓库

        Path parameters:
        org: 组织的路径(path/login) (**必填**)
        Query/Form parameters:
        type: 筛选仓库的类型，可以是 all, public, private。默认: all
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/orgs/{org}/repos", org=org)
        return self._get(
            url,
            params={
                "type": type,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_baidu_statistic_key(self, owner: str, repo: str) -> Any:
        """获取仓库的百度统计 key

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/baidu_statistic_key", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_blame(self, owner: str, path: str, repo: str, ref: Optional[str] = None) -> Any:
        """Blame

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径（1 MB 以内的文件文件） (**必填**)
        Query/Form parameters:
        ref: 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master）

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/blame/{path}", owner=owner, path=path, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
            },
        )

    def list_repos_branches(self, owner: str, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """获取所有分支

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        sort: 排序字段
        direction: 排序方向
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sort": sort,
                "direction": direction,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_collaborators(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库的所有成员

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_comments(self, owner: str, repo: str, order: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库的 Commit 评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        order: 排序顺序: asc(default),desc

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/comments", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "order": order,
            },
        )

    def list_repos_commits(self, owner: str, repo: str, author: Optional[str] = None, page: Optional[int] = None, path: Optional[str] = None, per_page: Optional[int] = None, sha: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None) -> Any:
        """仓库的所有提交

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        sha: 提交起始的SHA值或者分支名. 默认: 仓库的默认分支
        path: 包含该文件的提交
        author: 提交作者的邮箱或个人空间地址(username/login)
        since: 提交的起始时间，时间格式为 ISO 8601
        until: 提交的最后时间，时间格式为 ISO 8601
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sha": sha,
                "path": path,
                "author": author,
                "since": since,
                "until": until,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_commits_comments(self, owner: str, ref: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取单个Commit的评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        ref: Commit的Reference (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{ref}/comments", owner=owner, ref=ref, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_contributors(self, owner: str, repo: str, type: Optional[str] = None) -> Any:
        """获取仓库贡献者

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        type: 贡献者类型

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/contributors", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "type": type,
            },
        )

    def list_repos_forks(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """查看仓库的Forks

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        sort: 排序方式: fork的时间(newest, oldest)，star的人数(stargazers)
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/forks", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sort": sort,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_keys(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库已部署的公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_keys_available(self, owner: str, repo: str, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库可部署的公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/available", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def list_repos_languages(self, owner: str, repo: str) -> Any:
        """仓库代码语言字节数

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/languages", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_push_config(self, owner: str, repo: str) -> Any:
        """获取仓库推送规则设置

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/push_config", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_raw(self, owner: str, path: str, repo: str, ref: Optional[str] = None) -> Any:
        """获取 raw 文件（100MB 以内）

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径 (**必填**)
        Query/Form parameters:
        ref: 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master）

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/raw/{path}", owner=owner, path=path, repo=repo)
        return self._get(
            url,
            params={
                "ref": ref,
            },
        )

    def list_repos_releases(self, owner: str, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库的所有Releases

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        direction: 可选。升序/降序。不填为升序

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "direction": direction,
            },
        )

    def list_repos_releases_attach_files(self, owner: str, release_id: int, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None) -> Any:
        """获取仓库下的指定 Release 的所有附件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        release_id: 发行版本的ID (**必填**)
        Query/Form parameters:
        page: 当前的页码
        per_page: 每页的数量，最大为 100
        direction: 可选: 升序/降序，默认为升序

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files", owner=owner, release_id=release_id, repo=repo)
        return self._get(
            url,
            params={
                "page": page,
                "per_page": per_page,
                "direction": direction,
            },
        )

    def list_repos_releases_attach_files_download(self, attach_file_id: int, owner: str, release_id: int, repo: str) -> Any:
        """下载指定 Release 的单个附件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        release_id: 发行版本的ID (**必填**)
        attach_file_id: 发行版本下的附件ID (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files/{attach_file_id}/download", attach_file_id=attach_file_id, owner=owner, release_id=release_id, repo=repo)
        return self._get(
            url,
        )

    def list_repos_releases_latest(self, owner: str, repo: str) -> Any:
        """获取仓库的最后更新的Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/latest", owner=owner, repo=repo)
        return self._get(
            url,
        )

    def list_repos_tags(self, owner: str, repo: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None) -> Any:
        """列出仓库所有的 tags

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        sort: 排序字段
        direction: 排序方向
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/tags", owner=owner, repo=repo)
        return self._get(
            url,
            params={
                "sort": sort,
                "direction": direction,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_user_repos(self, affiliation: Optional[str] = None, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, q: Optional[str] = None, sort: Optional[str] = None, type: Optional[str] = None, visibility: Optional[str] = None) -> Any:
        """列出授权用户的所有仓库

        Query/Form parameters:
        visibility: 公开(public)、私有(private)或者所有(all)，默认: 所有(all)
        affiliation: owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。
                   可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member
        type: 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误
        sort: 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name
        direction: 如果sort参数为full_name，用升序(asc)。否则降序(desc)
        q: 搜索关键字
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/user/repos")
        return self._get(
            url,
            params={
                "visibility": visibility,
                "affiliation": affiliation,
                "type": type,
                "sort": sort,
                "direction": direction,
                "q": q,
                "page": page,
                "per_page": per_page,
            },
        )

    def list_users_repos(self, username: str, direction: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, type: Optional[str] = None) -> Any:
        """获取某个用户的公开仓库

        Path parameters:
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        type: 用户创建的仓库(owner)，用户个人仓库(personal)，用户为仓库成员(member)，所有(all)。默认: 所有(all)
        sort: 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name
        direction: 如果sort参数为full_name，用升序(asc)。否则降序(desc)
        page: 当前的页码
        per_page: 每页的数量，最大为 100

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/users/{username}/repos", username=username)
        return self._get(
            url,
            params={
                "type": type,
                "sort": sort,
                "direction": direction,
                "page": page,
                "per_page": per_page,
            },
        )

    def update_repos(self, name: str, owner: str, repo: str, can_comment: Optional[bool] = None, default_branch: Optional[str] = None, default_merge_method: Optional[str] = None, description: Optional[str] = None, has_issues: Optional[bool] = None, has_wiki: Optional[bool] = None, homepage: Optional[str] = None, issue_comment: Optional[bool] = None, issue_template_source: Optional[str] = None, lightweight_pr_enabled: Optional[bool] = None, merge_enabled: Optional[bool] = None, online_edit_enabled: Optional[bool] = None, path: Optional[str] = None, private: Optional[bool] = None, pull_requests_enabled: Optional[bool] = None, rebase_enabled: Optional[bool] = None, security_hole_enabled: Optional[bool] = None, squash_enabled: Optional[bool] = None) -> Any:
        """更新仓库设置

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        name: 仓库名称 (**必填**)
        description: 仓库描述
        homepage: 主页(eg: https://gitee.com)
        has_issues: 允许提Issue与否。默认: 允许(true)
        has_wiki: 提供Wiki与否。默认: 提供(true)
        can_comment: 允许用户对仓库进行评论。默认： 允许(true)
        issue_comment: 允许对“关闭”状态的 Issue 进行评论。默认: 不允许(false)
        security_hole_enabled: 这个Issue涉及到安全/隐私问题，提交后不公开此Issue（可见范围：仓库成员, 企业成员）
        private: 仓库公开或私有。
        path: 更新仓库路径
        default_branch: 更新默认分支
        pull_requests_enabled: 接受 pull request，协作开发
        online_edit_enabled: 是否允许仓库文件在线编辑
        lightweight_pr_enabled: 是否接受轻量级 pull request
        merge_enabled: 是否开启 merge 合并方式, 默认为开启
        squash_enabled: 是否开启 squash 合并方式, 默认为开启
        rebase_enabled: 是否开启 rebase 合并方式, 默认为开启
        default_merge_method: 选择默认合并 Pull Request 的方式,分别为 merge squash rebase
        issue_template_source: Issue 模版来源 project: 使用仓库 Issue Template 作为模版； enterprise: 使用企业工作项作为模版

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}", owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "name": name,
                "description": description,
                "homepage": homepage,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "can_comment": can_comment,
                "issue_comment": issue_comment,
                "security_hole_enabled": security_hole_enabled,
                "private": private,
                "path": path,
                "default_branch": default_branch,
                "pull_requests_enabled": pull_requests_enabled,
                "online_edit_enabled": online_edit_enabled,
                "lightweight_pr_enabled": lightweight_pr_enabled,
                "merge_enabled": merge_enabled,
                "squash_enabled": squash_enabled,
                "rebase_enabled": rebase_enabled,
                "default_merge_method": default_merge_method,
                "issue_template_source": issue_template_source,
            },
        )

    def set_repo_visibility(self, owner: str, repo: str, private: bool) -> Any:
        """快速设置仓库公私有状态。

        这是一个便捷方法，自动获取仓库当前名称后仅更新 ``private`` 字段，
        无需手动传入 ``name`` 等其它参数。

        Args:
            owner: 仓库所属空间地址(企业、组织或个人的地址path)。
            repo: 仓库路径(path)。
            private: ``True`` 设为私有，``False`` 设为公开。

        Returns:
            更新后的仓库信息（dict）。

        Usage::

            # 设为私有
            client.repos.set_repo_visibility("owner", "repo", True)

            # 设为公开
            client.repos.set_repo_visibility("owner", "repo", False)
        """
        current = self.get_repos(owner, repo)
        return self.update_repos(
            owner=owner,
            repo=repo,
            name=current["name"],
            private=private,
        )

    def update_repos_branches_protection(self, branch: str, owner: str, repo: str) -> Any:
        """设置分支保护

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        branch: 分支名称 (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/{branch}/protection", branch=branch, owner=owner, repo=repo)
        return self._put(
            url,
        )

    def update_repos_branches_setting(self, merger: str, mode: str, owner: str, pusher: str, repo: str, wildcard: str, escapse_protect_branch_list: Optional[list[str]] = None, new_wildcard: Optional[str] = None) -> Any:
        """更新保护分支规则

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        wildcard: 分支/通配符 (**必填**)
        Query/Form parameters:
        new_wildcard: 新分支/通配符(为空不修改)
        pusher: 可推送代码成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开） (**必填**)
        merger: 可合并 Pull Request 成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开） (**必填**)
        mode: 模式。standard: 标准模式, review: 评审模式 (**必填**)
        escapse_protect_branch_list: 不受规则影响的分支列表，以英文逗号分隔，形如：['a', 'b']

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/{wildcard}/setting", owner=owner, repo=repo, wildcard=wildcard)
        return self._put(
            url,
            data={
                "new_wildcard": new_wildcard,
                "pusher": pusher,
                "merger": merger,
                "mode": mode,
                "escapse_protect_branch_list": escapse_protect_branch_list,
            },
        )

    def update_repos_branches_setting_new(self, merger: str, mode: str, owner: str, pusher: str, repo: str, wildcard: str, escapse_protect_branch_list: Optional[list[str]] = None) -> Any:
        """新建保护分支规则

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        wildcard: 分支/通配符 (**必填**)
        pusher: 可推送代码成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开） (**必填**)
        merger: 可合并 Pull Request 成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开） (**必填**)
        mode: 模式。standard: 标准模式, review: 评审模式 (**必填**)
        escapse_protect_branch_list: 不受规则影响的分支列表，以英文逗号分隔，形如：['a', 'b']

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches/setting/new", owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "wildcard": wildcard,
                "pusher": pusher,
                "merger": merger,
                "mode": mode,
                "escapse_protect_branch_list": escapse_protect_branch_list,
            },
        )

    def update_repos_clear(self, owner: str, repo: str) -> Any:
        """清空一个仓库

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/clear", owner=owner, repo=repo)
        return self._put(
            url,
        )

    def update_repos_collaborators(self, owner: str, permission: str, repo: str, username: str) -> Any:
        """添加仓库成员或更新仓库成员权限

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        username: 用户名(username/login) (**必填**)
        Query/Form parameters:
        permission: 成员权限: 拉代码(pull)，推代码(push)，管理员(admin)。默认: push (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators/{username}", owner=owner, repo=repo, username=username)
        return self._put(
            url,
            data={
                "permission": permission,
            },
        )

    def update_repos_comments(self, body: str, id: int, owner: str, repo: str) -> Any:
        """更新Commit评论

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 评论的ID (**必填**)
        Query/Form parameters:
        body: 评论的内容 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/comments/{id}", id=id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "body": body,
            },
        )

    def update_repos_contents(self, content: str, message: str, owner: str, path: str, repo: str, sha: str, branch: Optional[str] = None, author: Optional[dict] = None, committer: Optional[dict] = None) -> Any:
        """更新文件

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        path: 文件的路径 (**必填**)
        Query/Form parameters:
        content: 文件内容, 要用 base64 编码 (**必填**)
        sha: 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 (**必填**)
        message: 提交信息 (**必填**)
        branch: 分支名称。默认为仓库对默认分支
        Other parameters:
        committer_name: Committer的名字，默认为当前用户的名字
        committer_email: Committer的邮箱，默认为当前用户的邮箱
        author_name: Author的名字，默认为当前用户的名字
        author_email: Author的邮箱，默认为当前用户的邮箱

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/contents/{path}", owner=owner, path=path, repo=repo)
        return self._put(
            url,
            data={
                "content": content,
                "sha": sha,
                "message": message,
                "branch": branch,
                **(author if author is not None else {}),
                **(committer if committer is not None else {}),
            },
        )

    def update_repos_keys_enable(self, id: int, owner: str, repo: str) -> Any:
        """启用仓库公钥

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id: 公钥 ID (**必填**)
        Query/Form parameters:

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/enable/{id}", id=id, owner=owner, repo=repo)
        return self._put(
            url,
        )

    def update_repos_push_config(self, owner: str, repo: str, author_email_suffix: Optional[str] = None, commit_message_regex: Optional[str] = None, except_manager: Optional[bool] = None, max_file_size: Optional[int] = None, restrict_author_email_suffix: Optional[bool] = None, restrict_commit_message: Optional[bool] = None, restrict_file_size: Optional[bool] = None, restrict_push_own_commit: Optional[bool] = None) -> Any:
        """修改仓库推送规则设置

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        restrict_push_own_commit: 启用只能推送自己的提交（所推送提交中的邮箱必须与推送者所设置的提交邮箱一致）
        restrict_author_email_suffix: 启用只允许指定邮箱域名后缀的提交
        author_email_suffix: 指定邮箱域名的后缀
        restrict_commit_message: 启用提交信息正则表达式校验
        commit_message_regex: 用于验证提交信息的正则表达式
        restrict_file_size: 启用限制单文件大小
        max_file_size: 限制单文件大小（MB）
        except_manager: 仓库管理员不受上述规则限制

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/push_config", owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "restrict_push_own_commit": restrict_push_own_commit,
                "restrict_author_email_suffix": restrict_author_email_suffix,
                "author_email_suffix": author_email_suffix,
                "restrict_commit_message": restrict_commit_message,
                "commit_message_regex": commit_message_regex,
                "restrict_file_size": restrict_file_size,
                "max_file_size": max_file_size,
                "except_manager": except_manager,
            },
        )

    def update_repos_releases(self, body: str, id: int, name: str, owner: str, repo: str, tag_name: str, prerelease: Optional[bool] = None) -> Any:
        """更新仓库Release

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        id:  (**必填**)
        Query/Form parameters:
        tag_name: Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4 (**必填**)
        name: Release 名称 (**必填**)
        body: Release 描述 (**必填**)
        prerelease: 是否为预览版本。默认: false（非预览版本）

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{id}", id=id, owner=owner, repo=repo)
        return self._patch(
            url,
            data={
                "tag_name": tag_name,
                "name": name,
                "body": body,
                "prerelease": prerelease,
            },
        )

    def update_repos_reviewer(self, assignees: str, assignees_number: int, owner: str, repo: str, testers: str, testers_number: int) -> Any:
        """修改代码审查设置

        Path parameters:
        owner: 仓库所属空间地址(企业、组织或个人的地址path) (**必填**)
        repo: 仓库路径(path) (**必填**)
        Query/Form parameters:
        assignees: 审查人员username，可多个，半角逗号分隔，如：(username1,username2) (**必填**)
        testers: 测试人员username，可多个，半角逗号分隔，如：(username1,username2) (**必填**)
        assignees_number: 最少审查人数 (**必填**)
        testers_number: 最少测试人数 (**必填**)

        Returns:
            Parsed JSON response (dict, list, or None for 204).
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/reviewer", owner=owner, repo=repo)
        return self._put(
            url,
            data={
                "assignees": assignees,
                "testers": testers,
                "assignees_number": assignees_number,
                "testers_number": testers_number,
            },
        )

    # ── pagination helpers ──────────────────────────────────────────

    def list_enterprises_repos_all(self, enterprise: str, direct: Optional[bool] = None, max_pages: Optional[int] = None, per_page: int = 100, search: Optional[str] = None, type: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_enterprises_repos()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_enterprises_repos` for parameter documentation.
        """
        url = build_url("", "/v5/enterprises/{enterprise}/repos", enterprise=enterprise)
        params = {
            "search": search,            "type": type,            "direct": direct,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_orgs_repos_all(self, org: str, max_pages: Optional[int] = None, per_page: int = 100, type: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_orgs_repos()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_orgs_repos` for parameter documentation.
        """
        url = build_url("", "/v5/orgs/{org}/repos", org=org)
        params = {
            "type": type,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_branches_all(self, owner: str, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_branches()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_branches` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/branches", owner=owner, repo=repo)
        params = {
            "sort": sort,            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_collaborators_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_collaborators()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_collaborators` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/collaborators", owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_comments_all(self, owner: str, repo: str, max_pages: Optional[int] = None, order: Optional[str] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_comments` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/comments", owner=owner, repo=repo)
        params = {
            "order": order,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_commits_all(self, owner: str, repo: str, author: Optional[str] = None, max_pages: Optional[int] = None, path: Optional[str] = None, per_page: int = 100, sha: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_commits()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_commits` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits", owner=owner, repo=repo)
        params = {
            "sha": sha,            "path": path,            "author": author,            "since": since,            "until": until,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_commits_comments_all(self, owner: str, ref: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_commits_comments()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_commits_comments` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/commits/{ref}/comments", owner=owner, ref=ref, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_forks_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_forks()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_forks` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/forks", owner=owner, repo=repo)
        params = {
            "sort": sort,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_keys_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_keys()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_keys` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys", owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_keys_available_all(self, owner: str, repo: str, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_keys_available()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_keys_available` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/keys/available", owner=owner, repo=repo)
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
        )

    def list_repos_releases_all(self, owner: str, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_releases()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_releases` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases", owner=owner, repo=repo)
        params = {
            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_releases_attach_files_all(self, owner: str, release_id: int, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100) -> Any:
        """Iterate over all pages of ``list_repos_releases_attach_files()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_releases_attach_files` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/releases/{release_id}/attach_files", owner=owner, release_id=release_id, repo=repo)
        params = {
            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_repos_tags_all(self, owner: str, repo: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_repos_tags()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_repos_tags` for parameter documentation.
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/tags", owner=owner, repo=repo)
        params = {
            "sort": sort,            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_user_repos_all(self, affiliation: Optional[str] = None, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, q: Optional[str] = None, sort: Optional[str] = None, type: Optional[str] = None, visibility: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_user_repos()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_user_repos` for parameter documentation.
        """
        url = build_url("", "/v5/user/repos")
        params = {
            "visibility": visibility,            "affiliation": affiliation,            "type": type,            "sort": sort,            "direction": direction,            "q": q,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    def list_users_repos_all(self, username: str, direction: Optional[str] = None, max_pages: Optional[int] = None, per_page: int = 100, sort: Optional[str] = None, type: Optional[str] = None) -> Any:
        """Iterate over all pages of ``list_users_repos()``.

        This convenience wrapper handles pagination automatically.
        Yields individual items rather than pages.

        See :meth:`list_users_repos` for parameter documentation.
        """
        url = build_url("", "/v5/users/{username}/repos", username=username)
        params = {
            "type": type,            "sort": sort,            "direction": direction,        }
        return list_all(
            self._get,
            url,
            per_page=per_page,
            max_pages=max_pages,
            **params,
        )

    # ── download helpers ──────────────────────────────────────────

    def download_archive(
        self,
        owner: str,
        repo: str,
        format: str = "tarball",
        ref: Optional[str] = None,
        output: Optional[str] = None,
    ):
        """下载仓库压缩包。

        Args:
            owner: 仓库所属空间地址(企业、组织或个人的地址path)。
            repo: 仓库路径(path)。
            format: 压缩格式，``"tarball"`` (tar.gz) 或 ``"zip"``。
            ref: 分支、tag或commit。默认: 仓库的默认分支。
            output: 保存到本地文件路径。不传则返回 bytes 内容。

        Returns:
            若指定 ``output`` 则写入文件返回 ``None``，否则返回 ``bytes``。

        Usage::

            # 下载并保存到文件
            client.repos.download_archive("owner", "repo", output="repo.tar.gz")

            # 获取 bytes 内容
            data = client.repos.download_archive("owner", "repo", format="zip")
        """
        if format not in ("tarball", "zip"):
            raise ValueError(f"format 必须为 'tarball' 或 'zip'，收到: {format!r}")
        # Gitee API 端点名称: tarball → /tarball, zip → /zipball
        endpoint = "zipball" if format == "zip" else format
        url = build_url("", "/v5/repos/{owner}/{repo}/" + endpoint, owner=owner, repo=repo)
        resp = self._get(url, params={"ref": ref}, raw_response=True)
        if output:
            with open(output, "wb") as f:
                f.write(resp.content)
            return None
        return resp.content

    def download_file(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: Optional[str] = None,
        output: Optional[str] = None,
    ):
        """下载仓库中的单个原始文件。

        Args:
            owner: 仓库所属空间地址(企业、组织或个人的地址path)。
            repo: 仓库路径(path)。
            path: 文件在仓库中的路径，如 ``"README.md"`` 或 ``"src/main.py"``。
            ref: 分支、tag或commit。默认: 仓库的默认分支。
            output: 保存到本地文件路径。不传则返回文本内容。

        Returns:
            若指定 ``output`` 则写入文件返回 ``None``，否则返回 ``str``。

        Usage::

            # 获取文件内容
            content = client.repos.download_file("owner", "repo", "README.md")

            # 下载并保存到本地
            client.repos.download_file("owner", "repo", "src/main.py", output="main.py")
        """
        url = build_url("", "/v5/repos/{owner}/{repo}/raw/{path}", owner=owner, path=path, repo=repo)
        resp = self._get(url, params={"ref": ref}, raw_response=True)
        if output:
            with open(output, "wb") as f:
                f.write(resp.content)
            return None
        return resp.text


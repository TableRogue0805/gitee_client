# Gitee API v5 Python Client

基于 [Gitee Open API v5](https://gitee.com/api/v5/swagger.json) 的完整 Python 客户端库。

## 特性

- **完整覆盖** — 175 个端点、16 个资源分组，全部可用
- **直观的命名** — `client.repos.create_user_repos(...)`, `client.issues.list_repos_issues(...)`
- **类型安全** — 82 个 TypedDict 数据模型，完整的类型提示
- **自动分页** — `list_*_all()` 方法自动遍历所有页面
- **统一的错误处理** — 异常层次结构清晰
- **轻量依赖** — 仅需 `requests`

## 安装

```bash
pip install gitee-client
```

也可以从源码安装：

```bash
# 从 Gitee
pip install git+https://gitee.com/TableRogue/gitee_client.git

# 从 GitHub
pip install git+https://github.com/TableRogue0805/gitee_client.git
```

## 快速开始

```python
from gitee_client import GiteeClient

# 初始化（自动从 GITEE_ACCESS_TOKEN 环境变量读取 token）
client = GiteeClient()

# 或显式传入 token
client = GiteeClient(access_token="your_access_token")

# 也可用作上下文管理器
with GiteeClient() as client:
    repos = client.repos.list_user_repos()
```

## 使用示例

### 仓库操作

```python
# 列出当前用户的所有仓库
repos = client.repos.list_user_repos()

# 遍历所有仓库（自动分页）
for repo in client.repos.list_user_repos_all():
    print(repo["full_name"])

# 创建仓库
new_repo = client.repos.create_user_repos(
    name="my-project",
    description="项目描述",
    auto_init=True,
)

# 获取指定仓库
repo = client.repos.get_repos(owner="username", repo="repo-name")

# 更新仓库设置
client.repos.update_repos(
    owner="username", repo="repo-name",
    name="repo-name",
    description="新的描述",
    private=True,
)

# 删除仓库
client.repos.delete_repos(owner="username", repo="repo-name")

# 列出某个用户的公开仓库
repos = client.repos.list_users_repos(username="someone")
```

### 下载仓库 / 文件

```python
# 下载整个仓库（tar.gz / zip）
client.repos.download_archive("owner", "repo", format="tarball", output="repo.tar.gz")
client.repos.download_archive("owner", "repo", format="zip", output="repo.zip")

# 不指定 output 则返回内容（bytes）
data = client.repos.download_archive("owner", "repo", format="zip")

# 指定分支/标签/commit
data = client.repos.download_archive("owner", "repo", ref="main")

# 下载单个文件内容（返回文本）
content = client.repos.download_file("owner", "repo", "README.md")

# 下载文件并保存到本地
client.repos.download_file("owner", "repo", "README.md", ref="main", output="README.md")
```

### Issue 操作

```python
# 列出仓库的所有 Issue
issues = client.issues.list_repos_issues(
    owner="username", repo="repo-name", state="open"
)

# 创建 Issue
issue = client.issues.create_repos_issues(
    owner="username", repo="repo-name",
    title="Bug 报告",
    body="详细描述...",
)

# 获取单个 Issue
issue = client.issues.get_repos_issues(
    owner="username", repo="repo-name", number=1
)

# 更新 Issue
client.issues.update_repos_issues(
    owner="username", repo="repo-name",
    number=1, title="更新后的标题"
)

# 列出 Issue 评论
comments = client.issues.list_repos_issues_comments(
    owner="username", repo="repo-name", number=1
)

# 创建 Issue 评论
client.issues.create_repos_issues_comments(
    owner="username", repo="repo-name",
    number=1, body="我的评论"
)
```

### Pull Request 操作

```python
# 列出 Pull Requests
prs = client.pulls.list_repos_pulls(
    owner="username", repo="repo-name", state="open"
)

# 创建 Pull Request
pr = client.pulls.create_repos_pulls(
    owner="username", repo="repo-name",
    title="新功能",
    head="feature-branch",
    base="master",
    body="实现说明...",
)

# 获取单个 PR
pr = client.pulls.get_repos_pulls(
    owner="username", repo="repo-name", number=1
)

# 合并 PR
client.pulls.update_repos_pulls_merge(
    owner="username", repo="repo-name", number=1
)

# PR 审查
client.pulls.create_repos_pulls_review(
    owner="username", repo="repo-name", number=1
)
```

### 用户操作

```python
# 获取当前用户信息
me = client.users.list_user()

# 获取指定用户信息
user = client.users.get_users(username="someone")

# 更新用户资料
client.users.update_user(name="新名字", blog="https://example.com")

# 关注用户
client.users.update_user_following(username="someone")

# 取消关注
client.users.delete_user_following(username="someone")

# 列出关注者
followers = client.users.list_user_followers()
```

### 搜索

```python
# 搜索仓库
results = client.search.list_search_repositories(q="gitee", language="python")

# 遍历所有搜索结果
for repo in client.search.list_search_repositories_all(q="open source"):
    print(repo["full_name"])

# 搜索 Issue
issues = client.search.list_search_issues(q="bug", repo="owner/repo")

# 搜索用户
users = client.search.list_search_users(q="developer")
```

### 组织操作

```python
# 列出用户所属的组织
orgs = client.organizations.list_user_orgs()

# 获取组织信息
org = client.organizations.get_orgs(org="org-name")

# 列出组织成员
members = client.organizations.list_orgs_members(org="org-name")

# 创建组织
client.organizations.create_users_organization(
    name="new-org",
    org="new-org",
)
```

### Gist 操作

```python
# 列出代码片段
gists = client.gists.list_gists()

# 创建代码片段
gist = client.gists.create_gists(
    files={"hello.py": {"content": "print('Hello World')"}},
    description="我的第一个 Gist",
    public=True,
)

# 获取单个代码片段
gist = client.gists.get_gists(id="gist_id")

# 删除代码片段
client.gists.delete_gists(id="gist_id")
```

### 标签和里程碑

```python
# 列出仓库标签
labels = client.labels.list_repos_labels(owner="user", repo="repo")

# 创建标签
client.labels.create_repos_labels(
    owner="user", repo="repo",
    name="bug", color="#ff0000"
)

# 列出里程碑
milestones = client.milestones.list_repos_milestones(owner="user", repo="repo")

# 创建里程碑
client.milestones.create_repos_milestones(
    owner="user", repo="repo",
    title="v1.0",
    due_on="2026-12-31",
)
```

### Webhook 管理

```python
# 列出 Webhooks
hooks = client.webhooks.list_repos_hooks(owner="user", repo="repo")

# 创建 Webhook
hook = client.webhooks.create_repos_hooks(
    owner="user", repo="repo",
    url="https://example.com/webhook",
    password="secret",
    push_events=True,
)
```

### 企业版功能

```python
# 列出企业成员
members = client.enterprises.list_enterprises_members(enterprise="enterprise-name")

# 获取企业信息
enterprise = client.enterprises.get_enterprises(enterprise="enterprise-name")

# 企业 Issue 列表
issues = client.issues.list_enterprises_issues(enterprise="enterprise-name")
```

### 其他功能

```python
# 获取 Emoji 列表
emojis = client.misc.list_emojis()

# 获取 Gitignore 模板列表
templates = client.misc.list_gitignore_templates()

# 获取 License 列表
licenses = client.misc.list_licenses()

# 渲染 Markdown
html = client.misc.create_markdown(text="# Hello\n\nThis is **markdown**.")

# 获取授权用户的邮箱
emails = client.emails.list_emails()

# 获取 Gitee 指数
metrics = client.git_data.get_repos_git_gitee_metrics(owner="user", repo="repo")
```

## API 资源分组

| 属性 | 模块 | 端点数量 | 说明 |
|------|------|---------|------|
| `client.repos` | 仓库 | 76 | 仓库 CRUD、分支、标签、发布、协作者、提交、内容等 |
| `client.pulls` | Pull Requests | 27 | PR 的创建、审查、合并、测试、指派等 |
| `client.activity` | 动态 | 26 | 通知、私信、动态、Watch 等 |
| `client.issues` | Issues | 21 | Issue 的增删改查、评论、操作日志等 |
| `client.users` | 用户 | 18 | 用户资料、关注、SSH 公钥等 |
| `client.enterprises` | 企业 | 17 | 企业管理、成员管理、周报等 |
| `client.gists` | Gists | 17 | 代码片段的增删改查、评论、Star、Fork 等 |
| `client.labels` | 标签 | 16 | 仓库标签、Issue 标签的增删改查 |
| `client.organizations` | 组织 | 14 | 组织管理、成员管理、关注者等 |
| `client.misc` | 杂项 | 9 | Emoji、Gitignore 模板、License、Markdown 渲染 |
| `client.webhooks` | Webhooks | 6 | Webhook 的增删改查和测试 |
| `client.checks` | 检查 | 5 | Check Runs 的创建、更新、查询 |
| `client.milestones` | 里程碑 | 5 | 里程碑的增删改查 |
| `client.search` | 搜索 | 3 | 搜索仓库、Issue、用户 |
| `client.git_data` | Git 数据 | 3 | Blob、Tree、Gitee 指数 |
| `client.emails` | 邮箱 | 1 | 获取授权用户邮箱 |

## 方法命名规则

方法名遵循 `{动作}_{资源路径}` 的命名模式：

- `list_*` — GET 请求，返回列表（支持分页）
- `get_*` — GET 请求，返回单个资源
- `create_*` — POST 请求，创建资源
- `update_*` — PUT/PATCH 请求，更新资源
- `delete_*` — DELETE 请求，删除资源

带有 `_all` 后缀的方法（如 `list_user_repos_all()`）是自动分页的便捷包装，返回生成器遍历所有结果。

## 分页

支持分页的 `list_*` 方法接受 `page` 和 `per_page` 参数：

```python
# 手动分页
page1 = client.repos.list_user_repos(page=1, per_page=20)

# 自动遍历所有页面
for repo in client.repos.list_user_repos_all(per_page=50):
    print(repo["full_name"])
```

## 错误处理

```python
from gitee_client import (
    GiteeError, GiteeAPIError, GiteeAuthError,
    GiteeNotFoundError, GiteeValidationError,
)

try:
    client.repos.get_repos(owner="nonexistent", repo="repo")
except GiteeNotFoundError as e:
    print(f"资源不存在: {e}")
except GiteeAuthError as e:
    print(f"认证失败: {e}")
except GiteeAPIError as e:
    print(f"API 错误 {e.status_code}: {e.error_message}")
```

异常层次结构：

```
GiteeError
└── GiteeAPIError
    ├── GiteeAuthError       (401, 403)
    ├── GiteeNotFoundError   (404)
    ├── GiteeValidationError (422)
    ├── GiteeRateLimitError  (429)
    └── GiteeServerError     (5xx)
```

## 认证

通过 Gitee 个人访问令牌（[获取 token](https://gitee.com/profile/personal_access_tokens)）进行认证：

```python
# 方式 1: 环境变量
export GITEE_ACCESS_TOKEN="your_token_here"

# 方式 2: 直接传入
client = GiteeClient(access_token="your_token_here")
```

## 数据模型

所有响应数据都有对应的 TypedDict 类型定义：

```python
from gitee_client.models import Project, User, Issue, PullRequest

def process_repo(repo: Project) -> None:
    print(repo["full_name"])   # IDE 自动补全
    print(repo["html_url"])
```

## 依赖

- Python >= 3.8
- requests

## 许可

MIT

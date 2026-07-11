"""Data models for Gitee Check."""

from __future__ import annotations

from typing import Any, List, Optional, TypedDict


# 获取检查项代码注释
class CheckAnnotation(TypedDict, total=False):
    path: str  # 文件路径
    start_line: int  # 开始行
    end_line: int  # 结束行
    start_column: int  # 开始列
    end_column: int  # 结束列
    annotation_level: str  # 注释级别
    title: str  # 标题
    message: str  # 信息
    raw_details: str  # 详情
    blob_href: str  # 文件路由


# 获取某个提交的检查项
class CheckRun(TypedDict, total=False):
    id: int
    head_sha: str  # 提交 sha 值
    url: str  # api 路由
    html_url: str  # 页面路由
    details_url: str  # 外部详情路由
    status: str  # 状态
    conclusion: str  # 结论
    started_at: str  # 开始时间
    completed_at: str  # 完成事件
    output: dict  # 详情
    name: str  # 检查名



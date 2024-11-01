# AI程序员平台设计文档

## 项目概述
本项目旨在搭建一个连接中小型企业与AI程序员的在线平台，支持用户发布项目需求并招募程序员。系统将使用Python Django作为后端框架，MySQL作为数据库，Vue.js作为前端框架。

## 1. 后端设计

### 1.1 API端口设计
- **用户管理**
  - `POST /api/register`：用户注册
  - `POST /api/login`：用户登录
  - `GET /api/profile`：获取用户个人信息
  - `PUT /api/profile`：更新用户信息

- **项目管理**
  - `POST /api/projects`：发布新项目
  - `GET /api/projects`：获取项目列表
  - `GET /api/projects/{id}`：获取特定项目详情
  - `PUT /api/projects/{id}`：更新项目信息
  - `DELETE /api/projects/{id}`：删除项目

- **提案管理**
  - `POST /api/projects/{id}/proposals`：提交项目提案
  - `GET /api/projects/{id}/proposals`：获取项目提案列表

- **聊天功能**
  - `POST /api/messages`：发送消息
  - `GET /api/messages`：获取聊天记录

### 1.2 用户角色
- **管理员**：管理用户和项目，查看统计信息。
- **企业用户**：发布项目、查看提案、与程序员沟通。
- **程序员**：申请项目、提交提案、查看个人信息。

## 2. 前端设计

### 2.1 页面结构
- **首页**
  - 项目推荐
  - 注册/登录入口
  - 介绍平台的功能

- **用户仪表盘**
  - 个人信息
  - 我的项目
  - 我的提案
  - 消息中心

- **项目页面**
  - 项目详情
  - 提交提案按钮
  - 查看提案列表

- **聊天页面**
  - 聊天窗口
  - 消息输入框

### 2.2 组件设计
- **导航栏**
  - 登录/注册链接
  - 用户头像
  - 项目发布按钮

- **项目卡片**
  - 项目标题
  - 项目描述
  - 申请按钮

- **提案表单**
  - 提案标题
  - 提案描述
  - 预算和时间预估

## 3. 数据库设计

### 3.1 数据库表
- **Users**
  - `id`: 主键
  - `username`: 用户名
  - `password`: 密码（加密存储）
  - `role`: 用户角色（管理员、企业、程序员）

- **Projects**
  - `id`: 主键
  - `title`: 项目标题
  - `description`: 项目描述
  - `budget`: 预算
  - `created_at`: 创建时间
  - `user_id`: 发布者ID（外键，关联Users表）

- **Proposals**
  - `id`: 主键
  - `project_id`: 项目ID（外键，关联Projects表）
  - `user_id`: 提交者ID（外键，关联Users表）
  - `description`: 提案描述
  - `created_at`: 提交时间

- **Messages**
  - `id`: 主键
  - `sender_id`: 发送者ID（外键，关联Users表）
  - `receiver_id`: 接收者ID（外键，关联Users表）
  - `content`: 消息内容
  - `created_at`: 发送时间

## 4. 总结
以上设计概述了AI程序员平台的主要组成部分，涵盖了后端API设计、前端界面结构及数据库架构。后续可以根据需求进一步细化具体实现和功能细节。

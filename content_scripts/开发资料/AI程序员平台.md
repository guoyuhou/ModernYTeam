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

### 2.1 页面结构和功能
以下是平台的主要HTML页面及其功能：

- **首页 (`index.html`)**
  - 功能：展示平台的基本介绍、项目推荐和注册/登录入口。
  - 相关接口：
    - `GET /api/projects`：获取推荐项目列表。

- **用户仪表盘 (`dashboard.html`)**
  - 功能：显示用户的个人信息、我的项目、我的提案和消息中心。
  - 相关接口：
    - `GET /api/profile`：获取用户信息。
    - `GET /api/projects`：获取用户发布的项目列表。
    - `GET /api/projects/{id}/proposals`：获取用户提交的提案列表。

- **项目页面 (`project.html`)**
  - 功能：显示项目详情，允许程序员提交提案。
  - 相关接口：
    - `GET /api/projects/{id}`：获取项目详情。
    - `POST /api/projects/{id}/proposals`：提交提案。

- **提案提交页面 (`submit_proposal.html`)**
  - 功能：提供提案表单，允许程序员提交提案。
  - 相关接口：
    - `POST /api/projects/{id}/proposals`：提交提案。

- **聊天页面 (`chat.html`)**
  - 功能：实时聊天功能，允许企业和程序员进行沟通。
  - 相关接口：
    - `POST /api/messages`：发送消息。
    - `GET /api/messages`：获取聊天记录。

- **注册页面 (`register.html`)**
  - 功能：用户注册表单。
  - 相关接口：
    - `POST /api/register`：用户注册。

- **登录页面 (`login.html`)**
  - 功能：用户登录表单。
  - 相关接口：
    - `POST /api/login`：用户登录。

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

## 4. 开发逻辑

1. **用户注册和登录**
   - 用户通过注册页面提交信息，调用注册API，注册成功后重定向到登录页面。
   - 用户登录后，前端获取用户信息，跳转到用户仪表盘。

2. **项目管理**
   - 企业用户在仪表盘上发布新项目，填写项目表单并提交，调用项目发布API。
   - 程序员在项目页面查看项目详情并提交提案，调用提案提交API。

3. **提案和消息功能**
   - 程序员提交提案后，企业用户在仪表盘上查看提案列表。
   - 企业用户和程序员通过聊天页面实时沟通，调用消息API进行消息的发送和接收。

4. **数据存储**
   - 所有用户信息、项目、提案和消息均存储在MySQL数据库中，通过Django后端进行数据管理。

## 5. 总结
以上设计概述了AI程序员平台的主要组成部分，涵盖了后端API设计、前端界面结构、数据库架构以及详细的开发逻辑。后续可以根据需求进一步细化具体实现和功能细节。

# 以Django为基础的Web

#### 1.前言
Django是Python中较为流行的Web框架，其功能强大，生态丰富，是值得我们学习的。而且Django为基础的Web框架非常适合AI+Web的结合，可以大大简化我们的开发流程。ta的上限更高。以Django作为后端，CSS和JavaScript作为前端，借助GPT和Cursor作为辅助，便可以创造出所有的Web页面

#### 2. 基础知识
Django的文件框架一般是这样的：
代码框架：
xin_yang_chemical/
│
├── xinyang_project/         # 项目根目录
│   ├── __init__.py            # 项目初始化文件
│   ├── settings.py            # 项目配置文件（数据库、静态资源、模板等）
│   ├── urls.py                # 项目URL映射入口
│   ├── wsgi.py                # 部署时的WSGI入口
│   └── asgi.py                # 异步部署时的ASGI入口
│
├── app/                       # 核心应用目录（创建具体业务逻辑的Django App）
│   ├── __init__.py
│   ├── admin.py               # 管理后台配置
│   ├── apps.py                # 应用配置
│   ├── models.py              # 数据库模型
│   ├── urls.py                # 该应用的URL映射
│   ├── views.py               # 视图逻辑
│   ├── forms.py               # 表单处理
│   ├── static/                # 静态资源文件（CSS、JS、图片）
│   │   ├── css/
│   │   │   └── styles.css     # 样式文件
│   │   ├── js/
│   │   │   └── scripts.js     # 前端交互的JavaScript
│   │   └── images/            # 网站图片（产品展示、工厂图片等）
│   ├── templates/             # 前端HTML模板文件
│   │   ├── base.html          # 基础模板，包含头部和脚部
│   │   ├── index.html         # 首页
│   │   ├── about.html         # 关于我们页面
│   │   ├── products.html      # 产品与服务页面
│   │   ├── contact.html       # 联系我们页面
│   │   └── cooperation.html   # 合作案例页面
│   ├── migrations/            # 数据迁移文件
│   └── tests.py               # 测试文件
│
├── media/                     # 用户上传的文件（如产品图片）
│
├── staticfiles/               # 收集的静态文件（用于部署）
│
├── manage.py                  # Django项目的管理命令
└── requirements.txt           # 项目依赖文件

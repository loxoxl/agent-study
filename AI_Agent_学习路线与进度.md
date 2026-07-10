# AI Agent 学习路线（PHP 开发者）

## 当前目标

从 PHP + LNMP + ThinkPHP 开发工程师，成长为能够独立开发 AI Agent
的工程师。

------------------------------------------------------------------------

# 已完成（Day 1）

## 环境搭建

-   安装 Python 3.13
-   创建并理解虚拟环境 `.venv`
-   学会激活/退出虚拟环境
-   安装 `openai`
-   安装 `python-dotenv`
-   学会 `pip list`、`pip freeze`、`pip show`

## 项目结构

``` text
agent_study/
├── .venv/
├── .env
├── config.py
├── llm.py
├── main.py
└── requirements.txt
```

## 已完成模块

### config.py

-   使用 `.env`
-   API Key 配置
-   Base URL
-   Model 配置

### llm.py

-   创建 OpenAI Client（连接 DeepSeek）
-   封装 `chat(messages)` 接口
-   返回 AI 回复文本

### main.py

-   多轮聊天
-   System Prompt
-   用户输入
-   保存 messages
-   调用 LLM
-   保存 AI 回复
-   `try/except`
-   `exit` 退出

------------------------------------------------------------------------

# 已掌握 Python

-   import
-   from ... import ...
-   函数
-   类型提示
-   list
-   dict
-   append()
-   while True
-   break
-   input()
-   f-string
-   try/except
-   模块拆分

------------------------------------------------------------------------

# 已掌握的软件设计思想

-   单一职责
-   配置与业务分离
-   封装
-   模块化
-   LLM 与业务解耦

------------------------------------------------------------------------

# 下一阶段（按顺序）

## Stage 2：Python 面向对象

-   class
-   **init**
-   self
-   成员变量
-   成员方法
-   Agent 类

## Stage 3：真正的 Agent

-   Agent 类
-   Memory
-   Prompt 管理
-   Tool 管理

## Stage 4：Tool Calling

-   自定义工具
-   天气工具
-   文件工具
-   MySQL 工具

## Stage 5：数据库

-   MySQL 查询
-   ORM（可选）
-   AI 查询数据库

## Stage 6：RAG

-   文档解析
-   向量数据库
-   检索增强

## Stage 7：LangGraph

-   State
-   Node
-   Edge
-   多 Agent

## Stage 8：MCP

-   MCP Server
-   MCP Client
-   工具接入

## Stage 9：部署

-   FastAPI
-   Docker
-   Linux
-   Nginx
-   HTTPS
-   云服务器

------------------------------------------------------------------------

# 学习方式

每个阶段遵循：

1.  完成一个真实功能
2.  学习相关 Python 知识
3.  Code Review
4.  重构优化
5.  总结

目标不是会调用模型，而是具备独立设计、开发、调试和部署 AI Agent 的能力。

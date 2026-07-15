# AI Agent 学习路线（PHP 开发者）

## 当前目标

从 PHP + LNMP + ThinkPHP 开发工程师，成长为能够独立开发 AI Agent
的工程师。

------------------------------------------------------------------------

# 已完成

## Stage 1：Python 基础 + 环境搭建（Day 1）

### 环境搭建

-   安装 Python 3.13
-   创建并理解虚拟环境 `.venv`
-   学会激活/退出虚拟环境
-   安装 `openai`
-   安装 `python-dotenv`
-   学会 `pip list`、`pip freeze`、`pip show`

### 项目结构

``` text
agent_study/
├── .venv/
├── .env
├── config.py
├── llm.py
├── main.py
└── requirements.txt
```

### 已完成模块

#### config.py

-   使用 `.env`
-   API Key 配置
-   Base URL
-   Model 配置

#### llm.py

-   创建 OpenAI Client（连接 DeepSeek）
-   封装 `chat(messages)` 接口
-   返回 AI 回复文本

#### main.py

-   多轮聊天
-   System Prompt
-   用户输入
-   保存 messages
-   调用 LLM
-   保存 AI 回复
-   `try/except`
-   `exit` 退出

---

## Stage 2：Python 面向对象（Day 2）

### 当前项目结构

``` text
agent_study/
├── .venv/
├── .env
├── config.py       → 环境变量和 API 配置
├── llm.py          → LLM 调用封装
├── agent.py        → Agent 类（封装消息 + 调用 LLM）
├── main.py         → 入口（循环 + 显示）
└── requirements.txt
```

**依赖方向**：`config.py` ← `llm.py` ← `agent.py` ← `main.py`

### agent.py

-   `class Agent` — 封装对话状态和行为
-   `__init__(system_prompt)` — 构造时接受可选的 system prompt
-   `self.messages` — 成员变量，管理对话历史
-   `chat(user_input) → str | None` — 核心方法：
    -   用**临时列表**先试探 LLM（不污染 `self.messages`）
    -   成功后再追加 user 消息和 assistant 消息
    -   失败返回 `None`，`self.messages` 保持原样

### main.py（重构后）

-   从 48 行缩减到 24 行
-   不再直接操作 `messages`、不直接调用 `llm.chat()`
-   只负责：创建 Agent → 循环读输入 → 调用 `agent.chat()` → 打印结果
-   输入校验（空输入、exit）留在 UI 层，不进入 Agent

### 关键设计决策

-   **先验证再提交**：用临时列表调 LLM，成功后才写 `self.messages`
-   **Agent 不输出**：`chat()` 只 `return`，不 `print()`——为后续接入 FastAPI 做准备
-   **错误向上传递**：异常和空响应统一返回 `None`，由调用方决定如何处理

---

## Stage 3-1：Memory 记忆系统（Day 3）

### 当前项目结构

``` text
agent_study/
├── .venv/
├── .env
├── config.py       → 环境变量和 API 配置
├── llm.py          → LLM 调用封装
├── memory.py       → Memory 类（消息存储、裁剪、清空）
├── agent.py        → Agent 类（协调 Memory + LLM）
├── main.py         → 入口（循环 + 显示）
└── requirements.txt
```

**依赖方向**：`config.py ← llm.py ← agent.py → memory.py`，`agent.py ← main.py`

### memory.py

-   `class Memory` — 独立的记忆管理类
-   `__init__(system_prompt, max_messages=20)` — 初始化记忆系统
-   `self.system_prompt` — 单独存储，与对话历史分离，不会被误删
-   `self.history` — 只存 user/assistant 消息，不混入 system
-   `add(role, content)` — 追加消息，超出上限自动裁剪旧消息
-   `get_messages()` → `list` — 返回 `[system] + history`，调用时动态组装
-   `clear()` — 清空对话历史，system prompt 保留

### agent.py（集成 Memory 后）

-   删除了 `self.messages`，改用 `self.memory = Memory(system_prompt)`
-   `chat()` 通过 `self.memory.get_messages()` 获取上下文
-   成功回复后通过 `self.memory.add()` 保存

### 关键设计决策

-   **数据结构分离**：system prompt 与对话历史分开存储，避免 `pop(0)` 误删 system
-   **委托模式**：Agent 不直接操作列表，委托 Memory 管理——以后换存储方式只改 Memory
-   **自动裁剪**：`max_messages` 控制内存占用和 Token 消耗，为后续长对话打基础

------------------------------------------------------------------------

# 已掌握 Python

## 基础语法（Stage 1）

-   `import` / `from ... import ...`
-   函数 / 类型提示
-   `list` / `dict` / `append()`
-   `while True` / `break`
-   `input()` / `f-string`
-   `try/except`
-   模块拆分

## 面向对象（Stage 2）

-   `class` — 定义类
-   `__init__(self, ...)` — 构造函数，PHP 的 `__construct()`
-   `self` — 实例引用，PHP 的 `$this`
-   成员变量 — `self.xxx = ...`
-   成员方法 — `def method(self, ...):`
-   `list + list` → 新列表（不修改原列表，无副作用）
-   `return None` — 错误信号传递
-   `from agent import Agent` — 直接导入类，避免模块名冲突

## 组合与委托（Stage 3）

-   对象嵌套 — `self.memory = Memory()`（PHP 里也叫组合）
-   委托 — 自己不干活，交给成员对象干
-   `pop(0)` — 删除列表第一个元素
-   `len()` — 判断列表长度 

------------------------------------------------------------------------

# 已掌握的软件设计思想

## Stage 1

-   单一职责
-   配置与业务分离
-   封装
-   模块化
-   LLM 与业务解耦

## Stage 2

-   **关注点分离**：UI 逻辑（main.py）与业务逻辑（agent.py）分层
-   **先验证再提交**：操作外部依赖前先确认成功，再修改内部状态
-   **错误向上传递**：底层返回错误信号（`None`），上层决定如何处理
-   **面向接口编程**：main.py 依赖 Agent 的 `chat()` 接口，不关心内部实现
-   **向后兼容设计**：`__init__` 参数给默认值，老代码不加参数也能跑

## Stage 3

-   **数据结构分离**：不要把不同性质的数据混在一个列表里（system prompt vs history）
-   **委托优于继承**：Agent 不继承 Memory，而是持有一个 Memory 实例——组合更灵活
-   **防守式裁剪**：`max_messages` 用 `>` 而非 `>=`，保证恰好保留 N 条完整对话
-   **内部状态不暴露**：`get_messages()` 返回新列表，不暴露内部 `self.history` 引用（当前实现可改进）

------------------------------------------------------------------------

# 下一阶段（按顺序）

## ~~Stage 2：Python 面向对象~~ ✅ 完成

## Stage 3：真正的 Agent

-   ~~Agent 类~~ ✅（Stage 2 已完成）
-   ~~Memory~~ ✅
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

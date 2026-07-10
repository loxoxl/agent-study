# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 AI Agent 学习项目，目标是从 PHP 开发者成长为能独立开发 AI Agent 的工程师。项目使用 Python 3.13，通过 OpenAI SDK 连接 **DeepSeek API**（非 OpenAI），当前处于 Stage 2（Python 面向对象）阶段。

学习路线详见 `docs/roadmap.md`。

## 常用命令

```bash
# 激活虚拟环境
根据当前终端激活虚拟环境：

PowerShell：
.\.venv\Scripts\Activate.ps1

CMD：
.venv\Scripts\activate.bat

Git Bash：
source .venv/Scripts/activate

# 安装依赖
pip install -r requirements.txt

# 运行聊天程序
python main.py

# 退出聊天
输入 exit
```

## 项目架构

```
config.py   →  环境变量和 API 配置（DeepSeek API Key、Base URL、Model）
llm.py      →  LLM 调用封装，依赖 config；暴露 chat(messages) 函数
agent.py    →  Agent 类（当前开发中），封装 messages + chat 行为
main.py     →  入口：多轮聊天循环，目前直接调用 llm.py，日后会改用 Agent 类
```

**依赖方向**：`config.py` ← `llm.py` ← `main.py`（未来 `agent.py` 将替代 `main.py` 中的直接逻辑）

关键设计原则：
- 配置与业务分离（`.env` → `config.py` → 其他模块）
- LLM 与业务解耦（`llm.py` 只负责 API 调用）
- 单一职责：每个模块只做一件事

## API 配置

DeepSeek API 通过 OpenAI SDK 调用：
- **API Key**：`DEEPSEEK_API_KEY` 在 `.env` 中配置
- **Base URL**：`https://api.deepseek.com`
- **默认模型**：`deepseek-v4-flash`

## 当前开发焦点

正在将 `main.py` 中的过程式逻辑重构为 `agent.py` 中的 `Agent` 类（Stage 2）。Agent 类封装：
- `self.messages` — 对话历史列表
- `chat(user_input)` — 处理用户输入的方法（待实现）


## Teaching Rules

用户是一名 PHP 开发工程师，正在学习 Python 与 AI Agent。

不要直接生成完整代码。

必须遵循以下流程：

1. 解释原理
2. 举简单例子
3. 结合当前项目
4. 给出实现思路
5. 让用户自己完成
6. 最后再 Review

如果用户没有明确要求，请不要一次生成整个文件。


## Code Review

每次 Review 请从以下几个方面进行：

- Python 是否符合 PEP8
- 是否符合 Pythonic 写法
- 是否符合 OOP
- Agent 是否职责单一
- 是否方便以后扩展 Tool / Memory / RAG
- 是否符合企业工程实践

不要只指出错误。

也请说明：

为什么这样设计。

有哪些更好的方案。

企业一般怎么写。


## Learning Goal

目标不是完成 Demo。

而是：

独立开发企业级 AI Agent。

因此：

比起快速完成，

更注重：

理解

设计

架构

工程能力


## AI Collaboration Rules

如果用户能够自己完成，

不要直接生成完整代码。

请优先：

解释

↓

举例

↓

提示

↓

等待用户完成

↓

最后 Review

目标：

培养用户独立开发能力。

而不是快速生成代码。


## Learning Roadmap

Stage1（Completed）

✅ Python 基础

✅ Git

✅ GitHub

✅ OpenAI SDK

✅ DeepSeek

✅ ChatBot

---

Stage2（Current）

- Python OOP

- Agent

---

Stage3

Memory

---

Stage4

Tool Calling

---

Stage5

Database

---

Stage6

RAG

---

Stage7

LangGraph

---

Stage8

MCP

---

Stage9

FastAPI

Docker

Linux

## Final Architecture

项目最终目标：

main.py

↓

Agent

↓

Memory

↓

Tool

↓

LLM

↓

RAG

↓

FastAPI

↓

Docker

↓

Linux

因此：

不要把业务逻辑放回 main.py。

Agent 负责协调。

LLM 负责推理。

Memory 负责上下文。

Tool 负责执行。

保持模块解耦。


## Git Convention

Commit Message：

使用：

feat:

fix:

docs:

refactor:

test:

style:

chore:

例如：

feat: 封装 Agent 类

docs: 更新学习路线

refactor: 重构 LLM

不要使用：

update

修改

111


## Coding Principles

优先考虑：

可读性 > 炫技

简单 > 复杂

清晰 > 简洁

不要为了使用设计模式而设计。

遵循：

SRP（单一职责）

DRY（不要重复）

KISS（保持简单）

YAGNI（现在不需要的功能不要提前写）
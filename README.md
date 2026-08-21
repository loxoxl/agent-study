# AI Agent 学习项目

从 PHP + LNMP + ThinkPHP 开发者到 AI Agent 工程师的实战学习项目。
基于 Python 3.13，通过 OpenAI SDK 连接 **DeepSeek API**，从零搭建一个支持多轮对话、记忆管理、模板提示词和工具调用（Tool Calling）的 Agent。

学习路线见 [docs/roadmap.md](docs/roadmap.md)。

## 功能特性

- 💬 **多轮对话**：`Memory` 类管理对话历史，自动裁剪防止上下文无限膨胀
- 🧠 **记忆管理**：System Prompt 与对话历史分离存储，`max_messages` 控制消息上限
- 📝 **模板提示词**：`{占位符}` 动态渲染，运行时注入变量（作者等）
- 🛠️ **工具调用（Tool Calling）**：AI 可自主决定调用已注册的工具（如获取当前时间），代码执行后把结果回传给 AI 组织回答
- 📋 **日志记录**：请求/响应全链路日志（`logging`），通过 `AGENT_DEBUG` 开关按需开启

## 项目结构

```text
agent_study/
├── .venv/          # 虚拟环境
├── .env            # API 配置（密钥，不入库）
├── config.py       # 环境变量和 API 配置（作者、机器人名、调试开关、模型）
├── llm.py          # LLM 调用封装（含请求/响应日志）
├── memory.py       # Memory 类：消息存储、裁剪、模板渲染
├── tool.py         # Tool 类：工具封装（名称、描述、函数、参数）
├── agent.py        # Agent 类：协调 Memory + LLM + Tool，实现工具调用循环
├── main.py         # 入口：多轮对话（已接入工具调用）
├── test.py         # 测试脚本（工具调用闭环验证）
├── docs/roadmap.md # 学习路线（按 Stage 更新）
└── requirements.txt
```

**依赖方向**：

```text
config.py ← llm.py ← agent.py → memory.py / tool.py
                          ↑
                       main.py
```

## 快速开始

### 环境要求

- Python 3.13+
- DeepSeek API Key

### 安装

```bash
# 1. 创建虚拟环境（只需一次）
python -m venv .venv
```

**2. 激活虚拟环境（按你的终端选一种）**

| 终端 | 激活命令 | 激活成功标志 |
|------|---------|-------------|
| PowerShell | `.\\.venv\\Scripts\\Activate.ps1` | 提示符前出现 `(.venv)` |
| cmd | `.venv\\Scripts\\activate.bat` | 提示符前出现 `(.venv)` |
| Git Bash | `source .venv/Scripts/activate` | 提示符前出现 `(.venv)` |

> 如果 PowerShell 提示"禁止运行脚本"，先执行一次：`Set-ExecutionPolicy -Scope Process Bypass`（仅当前窗口生效）。

**3. 安装依赖**

```bash
pip install -r requirements.txt
```

### 配置

在项目根目录创建 `.env` 文件：

```env
DEEPSEEK_API_KEY=你的密钥
AUTHOR=你的名字          # 可选，注入到 System Prompt（默认"默认作者"）
BOT_NAME=你的机器人名      # 可选，聊天界面显示名（默认"智能AI助手"）
```

> ⚠️ `.env` 已在 `.gitignore` 中，请勿提交密钥。

### 运行

```bash
# 多轮对话（main.py 已注册 get_time 工具，问"现在几点了"体验工具调用）
python main.py

# 工具调用闭环测试（test.py）
python test.py
```

### 调试（可选）

想看 AI 请求/响应的完整日志？开调试开关：

| 终端 | 命令 |
|------|------|
| PowerShell | `$env:AGENT_DEBUG = "1"; python main.py` |
| cmd | `set AGENT_DEBUG=1 && python main.py` |
| Git Bash | `AGENT_DEBUG=1 python main.py` |

关闭：PowerShell 用 `$env:AGENT_DEBUG = $null`，或关掉终端重开。

## 使用示例

```text
👤 你：你好
🤖 智能AI助手：你好！有什么可以帮你的吗？

👤 你：现在几点了
🤖 智能AI助手：现在是 16:29:55
（内部流程：AI 决定调用 get_time → 代码执行 → 结果回传 → AI 组织回答）
```

退出对话：输入 `exit` 或 `退出`。

## 技术栈

| 组件 | 说明 |
|------|------|
| Python 3.13 | 语言 |
| openai SDK | 调用 DeepSeek API（兼容 OpenAI 协议） |
| python-dotenv | 读取 `.env` 配置 |
| logging | 标准库日志 |

## 项目状态

- ✅ Stage 1：Python 基础 + 环境搭建
- ✅ Stage 2：Python 面向对象（Agent 类）
- ✅ Stage 3：Memory 记忆系统 + Prompt 模板 + Tool 管理
- 🚧 Stage 4：Tool Calling（已打通最小闭环：get_time 工具可被 AI 自动调用，已接入 main.py）
- ⏭️ 后续：天气/文件/MySQL 工具 → 数据库 → RAG → LangGraph → MCP → 部署

## Git 约定

Commit Message 使用约定式前缀：`feat:` / `fix:` / `docs:` / `refactor:` / `test:` / `style:` / `chore:`。

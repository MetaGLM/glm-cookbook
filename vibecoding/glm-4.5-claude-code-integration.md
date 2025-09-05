# GLM-4.5 Claude Code Integration Guide

> 中文版本请阅读 [GLM-4.5 Claude Code 集成指南](#glm-45-claude-code-集成指南)

GLM-4.5 series models now support integration with Claude Code, allowing you to use Zhipu AI's latest model capabilities in the familiar Claude Code environment.

## Prerequisites

- Claude Code installed and configured
- Related API [Purchase Link](https://z.ai/subscribe)

## Configuration Methods

### Method 1: Using Setup Script

1. Download the setup script:

```bash
curl -o glm_claude_setup.sh "http://bigmodel-us3-prod-marketplace.cn-wlcb.ufileos.com/1753683727739-0b3a4f6e84284f1b9afa951ab7873c29.sh?ufileattname=claude_code_prod.sh"
chmod +x glm_claude_setup.sh
```

2. Run the script:

```bash
./glm_claude_setup.sh
```

3. Enter your API Key when prompted

### Method 2: Manual Configuration

1. Set environment variables:

```bash
export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
export ANTHROPIC_API_KEY=YOUR_API_KEY
```

2. Or add the configuration to your shell configuration file (such as `~/.bashrc` or `~/.zshrc`):

```bash
echo 'export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY=YOUR_API_KEY' >> ~/.bashrc
source ~/.bashrc
```

### For Existing Claude Users

If you don't want to overwrite your existing Claude configuration, you can create an alias:

```shell
vim ~/.zshrc # or ~/.bashrc
alias glm="ANTHROPIC_AUTH_TOKEN="your zhipuai api keys" ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic claude"
source ~/.zshrc
```

## Usage Instructions

### Starting Claude Code

1. After configuring the environment variables, start Claude Code. On first use, Claude Code will ask if you trust accessing the current folder, select "Yes"

```bash
claude
```

2. If you followed the instructions for [Existing Claude Users](#for-existing-claude-users), enter in the command line:

```shell
glm
```

### Successful Startup

Seeing the following page indicates normal operation:

```
╭───────────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                         │
│                                                   │
│   /help for help, /status for your current setup  │
│                                                   │
│   cwd: /Users/zr/Code/glm-cookbook                │
│                                                   │
│   ─────────────────────────────────────────────── │
│                                                   │
│   Overrides (via env):                            │
│                                                   │
│   • API Base URL:                                 │
│   https://open.bigmodel.cn/api/anthropic          │ <- Check if API address is correct
╰───────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────────────────────────╮
│ > Try "how does glm_multi_role_division.ipynb work?"                          │
╰───────────────────────────────────────────────────────────────────────────────╯
  ? for shortcuts                                                                ◯
```

### Default Model Selection

- Claude Code uses the `GLM-4.5` model by default
- For lightweight tasks, the system automatically routes to `GLM-4.5-Air`
- You can specify a specific model through settings

## Frequently Asked Questions

### How many times can GLM Coding Lite and Pro plans be used?

GLM Coding Lite and GLM Coding Pro can be used approximately 120 times and 600 times respectively within every 5 hours. Only the number of prompts from developers asking questions on the command line is counted, model interactions during Claude Code execution are not counted.

### Can I manually specify the model?

Claude Code automatically schedules for different task types. Main scenarios such as conversation/planning/coding/complex reasoning use the GLM-4.5 model by default, while auxiliary scenarios such as file search/syntax checking use GLM-4.5-Air.

### Model Mapping?

+ Claude Opus 4.1 / Claude Sonnet 4 -> GLM-4.5
+ Claude Haiku 3.5 -> GLM-4.5-Air

Since Claude Opus 4.1 / Claude Sonnet 4 are both mapped to the same model, the rule in the [Claude Code rules](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan#h_2fb930398a) under the "What happens when you hit usage limits" section about Opus switching to Sonnet does not apply to GLM-4.5.

-----
# GLM-4.5 Claude Code 集成指南

GLM-4.5 系列模型现已支持集成到 Claude Code 中，让你可以在熟悉的 Claude Code 环境中使用智谱 AI 的最新模型能力。

## 前置要求

- Claude Code 已安装并配置
- 智谱 AI API Key（从 [智谱开放平台](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) 获取）
- 相关API [购买地址](https://bigmodel.cn/claude-code)

## 配置方法

### 方法一：使用配置脚本

1. 下载配置脚本：

```bash
curl -o glm_claude_setup.sh "http://bigmodel-us3-prod-marketplace.cn-wlcb.ufileos.com/1753683727739-0b3a4f6e84284f1b9afa951ab7873c29.sh?ufileattname=claude_code_prod.sh"
chmod +x glm_claude_setup.sh
```

2. 运行脚本：

```bash
./glm_claude_setup.sh
```

3. 按提示输入你的 API Key

### 方法二：手动配置

1. 设置环境变量：

```bash
export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
export ANTHROPIC_API_KEY=YOUR_API_KEY
```

2. 或者将配置添加到 shell 配置文件（如 `~/.bashrc` 或 `~/.zshrc`）：

```bash
echo 'export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY=YOUR_API_KEY' >> ~/.bashrc
source ~/.bashrc
```

### 对于已经有Claude的用户

如果你不想覆盖原有的Claude配置，可以创建一个别名:

```shell
vim ~/.zshrc # or ~/.bashrc
alias glm="ANTHROPIC_AUTH_TOKEN="your zhipuai api keys" ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic claude"
source ~/.zshrc
```

## 使用说明

### 启动 Claude Code

1. 在配置好环境变量后，启动 Claude Code, 首次使用时，Claude Code 会询问是否信任访问当前文件夹，选择"是"

```bash
claude
```

2. 如果你是按照 [对于已经有Claude的用户](#对于已经有claude的用户) 章节配置, 在命令行输入:

```shell
glm
```

### 启动成功

看到如下页面即正常

```
╭───────────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                         │
│                                                   │
│   /help for help, /status for your current setup  │
│                                                   │
│   cwd: /Users/zr/Code/glm-cookbook                │
│                                                   │
│   ─────────────────────────────────────────────── │
│                                                   │
│   Overrides (via env):                            │
│                                                   │
│   • API Base URL:                                 │
│   https://open.bigmodel.cn/api/anthropic          │ <- 检查API地址是否正确
╰───────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────────────────────────╮
│ > Try "how does glm_multi_role_division.ipynb work?"                          │
╰───────────────────────────────────────────────────────────────────────────────╯
  ? for shortcuts                                                                ◯
```

### 默认模型选择

- Claude Code 默认使用 `GLM-4.5` 模型
- 对于轻量级任务，系统会自动路由到 `GLM-4.5-Air`
- 可以通过设置指定特定模型

## 常见问题

### GLM Coding Lite 和 Pro 套餐预计可以用多少次？

GLM Coding Lite 和 GLM Coding Pro 每 5 小时内，分别最多使用约 120 次和 600 次 prompts。仅计算开发者与命令行提问的次数,
Claude Code 执行中模型的交互均不计入。

### 是否可以手动指定模型?

Claude Code 会针对不同任务类型自动调度，对话/规划/代码编写/复杂推理等主场景默认使用模型 GLM-4.5，文件搜索/语法检查等辅助场景使用 GLM-4.5-Air。

### 模型映射关系?

+ Claude Opus 4.1 / Claude Sonnet 4 -> GLM-4.5
+ Claude Haiku 3.5 -> GLM-4.5-Air

由于 Claude Opus 4.1 / Claude Sonnet 4
均映射到相同模型，因此，[Claude Code 规则](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan#h_2fb930398a)
中的 `What happens when you hit usage limits` 章节中的 Opus 切换到 Sonnet 的规则不适用于 GLM-4.5。


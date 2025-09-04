# GLM-4.5 Kode Integration Guide

> 中文版本请阅读 [GLM-4.5 Kode 集成指南](#glm-45-kode-集成指南)

[Kode](https://github.com/shareAI-lab/Kode) is a powerful AI assistant that lives in your terminal.
It can understand your codebase, edit files, run commands, and handle entire workflows for you.

This guide will walk you through integrating GLM-4.5 models into Kode.

## Installation

Install Kode

```shell
npm install -g @shareai-lab/kode
```

## Configuration

After selecting the topic, proceed to the model selection screen.

```
Kode 

 Configure your models:

 You can customize which models Kode uses for different tasks.
 Let's set up your preferred models for large and small tasks.

 Press Enter to continue to the model selection screen.

 Press Enter to continue…
```

Keep pressing the down arrow key `↓` until GLM appears, then press Enter to select it (it is normal if the first option is
shown as 0 model).

```
╭───────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                       │
│  Provider Selection                                                                   │
│                                                                                       │
│  Select your preferred AI provider for this model profile:                            │
│                                                                                       │
│  Choose the provider you want to use for this model profile.                          │
│  This will determine which models are available to you.                               │
│                                                                                       │
│    OpenRouter  (0 models)                                                             │
│    MiniMax  (3 models)                                                                │
│    SiliconFlow  (0 models)                                                            │
│    ❯GLM (Zhipu AI)  (0 models)                                                        │
│    Baidu Qianfan  (0 models)                                                          │
│                                                                                       │
│                                                                                       │
│  You can change this later by running /model again                                    │
│                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────╯
```

Next, enter the API Key.

```
╭──────────────────────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  API Key Setup                                                                   │
│                                                                                  │
│  Enter your GLM API key for this model profile:                                  │
│                                                                                  │
│  This key will be stored locally and used to access the glm API.                 │
│  Your key is never sent to our servers.                                          │
│                                                                                  │
│  💡 Get your API key from: https://open.bigmodel.cn (API Keys section)           │
│                                                                                  │
│  sk-...                                                                          │
│                                                                                  │
│                                                                                  │
│  [Submit API Key] - Press Enter or click to continue with this API key           │
│                                                                                  │
│                                                                                  │
│  Press Enter to continue, Tab to skip to manual model input, or Esc to go back   │
│                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────╯
```

You can now choose your preferred model settings like:

> → Output: 8K  
> → Context: 128K

If you see the following output, you have successfully configured the OpenAI interface for GLM-4.5.
Note that this is not the GLM Coding Plan method. If you are using GLM Coding Plan, please continue reading below.

```
╭───────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  Configuration Confirmation                                                               │
│                                                                                           │
│  Confirm your model configuration:                                                        │
│                                                                                           │
│  Please review your selections before saving.                                             │
│                                                                                           │
│                                                                                           │
│   Provider: GLM                                                                           │
│   Model: glm-4.5                                                                          │
│   API Key: ****803l                                                                       │
│   Max Tokens: 8192                                                                        │
│   Context Length: 128K tokens                                                             │
│                                                                                           │
│                                                                                           │
│                                                                                           │
│  Press Esc to go back to model parameters or Enter to save configuration                  │
│                                                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
```

## GLM Coding Plan setting

The [GLM Coding Plan](https://bigmodel.cn/claude-code) uses a Claude Code–type API interface, with a different API
endpoint.
If you need to switch to this plan, please continue with the following steps.

1. At the model selection location, choose `claude`, and change the `API BASE URL` to

```
╭──────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                              │
│  Provider Selection                                                                          │
│                                                                                              │
│  Select your preferred AI provider for this model profile:                                   │
│                                                                                              │
│  Choose the provider you want to use for this model profile.                                 │
│  This will determine which models are available to you.                                      │
│                                                                                              │
│    Kimi (Moonshot)  (1 models)                                                               │
│    ❯Claude  (3 models)                                                                       │
│    DeepSeek  (3 models)                                                                      │
│    Qwen (Alibaba)  (0 models)                                                                │
│    OpenAI  (19 models)                                                                       │
│                                                                                              │
│                                                                                              │
│  You can change this later by running /model again                                           │
│                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
```

Use `Custom Anthropic-Compatible API` and fill it as:

> https://open.bigmodel.cn/api/anthropic

Then enter the API KEY.

1. Verify whether you are using the GLM Coding Plan instead of regular credits.

In Kode, enter `/model` to check if it shows `anthropic glm-4.5`. If it does, then it's successful.

```
╭───────────────────────────────────────────────────────────────────────────────────────╮
│ Model Configuration                                                                   │
│ Configure which models to use for different tasks. Space to cycle, Enter to           │
│ configure.                                                                            │
│                                                                                       │
│ ❯ Main Model                                anthropic glm-4.5 [Space to cycle]        │
│   Primary model for general tasks and conversations                                   │
│                                                                                       │
│   Task Model                                anthropic glm-4.5                         │
│   Reasoning Model                           anthropic glm-4.5                         │
│   Quick Model                               anthropic glm-4.5                         │
│   Manage Model List                                                                   │
│                                                                                       │
│                                                                                       │
│ Use ↑/↓ to navigate, Space to cycle models, Enter to configure, d to clear, Esc to    │
│ exit                                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────╯
```


---

# GLM-4.5 Kode 集成指南

[Kode](https://github.com/shareAI-lab/Kode) 是一个强大的 AI 助手，可以在您的终端中运行。
它能够理解您的代码库、编辑文件、运行命令并为您处理整个工作流程。

本指南将引导您完成将 GLM-4.5 模型集成到 Kode 中的过程。

## 安装

安装 Kode

```shell
npm install -g @shareai-lab/kode
```

## 配置

选择主题后，进入模型选择界面。

```
Kode 

 配置您的模型：

 您可以自定义 Kode 用于不同任务的模型。
 让我们为您设置用于大型和小型任务的首选模型。

 按 Enter 继续进入模型选择界面。

 按 Enter 继续…
```

持续按下箭头键 `↓` 直到出现 GLM，然后按 Enter 选择它（第一个选项显示为 0 模型是正常的）。

```
╭───────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                       │
│  Provider Selection                                                                   │
│                                                                                       │
│  Select your preferred AI provider for this model profile:                            │
│                                                                                       │
│  Choose the provider you want to use for this model profile.                          │
│  This will determine which models are available to you.                               │
│                                                                                       │
│    OpenRouter  (0 models)                                                             │
│    MiniMax  (3 models)                                                                │
│    SiliconFlow  (0 models)                                                            │
│    ❯GLM (Zhipu AI)  (0 models)                                                        │
│    Baidu Qianfan  (0 models)                                                          │
│                                                                                       │
│                                                                                       │
│  You can change this later by running /model again                                    │
│                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────╯
```

接下来，输入 API 密钥。

```
╭──────────────────────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  API Key Setup                                                                   │
│                                                                                  │
│  Enter your GLM API key for this model profile:                                  │
│                                                                                  │
│  This key will be stored locally and used to access the glm API.                 │
│  Your key is never sent to our servers.                                          │
│                                                                                  │
│  💡 Get your API key from: https://open.bigmodel.cn (API Keys section)           │
│                                                                                  │
│  sk-...                                                                          │
│                                                                                  │
│                                                                                  │
│  [Submit API Key] - Press Enter or click to continue with this API key           │
│                                                                                  │
│                                                                                  │
│  Press Enter to continue, Tab to skip to manual model input, or Esc to go back   │
│                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────╯
```

现在您可以选择您喜欢的模型设置，如：

> → 输出：8K  
> → 上下文：128K

如果您看到以下输出，则表示您已成功为 GLM-4.5 配置了 OpenAI 接口。
请注意，这不是 GLM 编程计划方法。如果您使用的是 GLM 编程计划，请继续阅读下文。

```
╭───────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  Configuration Confirmation                                                               │
│                                                                                           │
│  Confirm your model configuration:                                                        │
│                                                                                           │
│  Please review your selections before saving.                                             │
│                                                                                           │
│                                                                                           │
│   Provider: GLM                                                                           │
│   Model: glm-4.5                                                                          │
│   API Key: ****803l                                                                       │
│   Max Tokens: 8192                                                                        │
│   Context Length: 128K tokens                                                             │
│                                                                                           │
│                                                                                           │
│                                                                                           │
│  Press Esc to go back to model parameters or Enter to save configuration                  │
│                                                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
```

## GLM 编程计划设置

[GLM Code Plan](https://bigmodel.cn/claude-code) 使用 Claude Code 的 API 接口。 如果您需要切换到此计划，请继续执行以下步骤。

1. 在模型选择位置，选择 `claude`，并将 `API BASE URL` 更改为

```
╭──────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                              │
│  Provider Selection                                                                          │
│                                                                                              │
│  Select your preferred AI provider for this model profile:                                   │
│                                                                                              │
│  Choose the provider you want to use for this model profile.                                 │
│  This will determine which models are available to you.                                      │
│                                                                                              │
│    Kimi (Moonshot)  (1 models)                                                               │
│    ❯Claude  (3 models)                                                                       │
│    DeepSeek  (3 models)                                                                      │
│    Qwen (Alibaba)  (0 models)                                                                │
│    OpenAI  (19 models)                                                                       │
│                                                                                              │
│                                                                                              │
│  You can change this later by running /model again                                           │
│                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
```

使用 `Custom Anthropic-Compatible API` 并填写为：

> https://open.bigmodel.cn/api/anthropic

然后输入 API 密钥。

1. 验证您是否在使用 GLM 编程计划而不是常规积分。

在 Kode 中，输入 `/model` 检查是否显示 `anthropic glm-4.5`。如果是，则表示成功。

```
╭───────────────────────────────────────────────────────────────────────────────────────╮
│ Model Configuration                                                                   │
│ Configure which models to use for different tasks. Space to cycle, Enter to           │
│ configure.                                                                            │
│                                                                                       │
│ ❯ Main Model                                anthropic glm-4.5 [Space to cycle]        │
│   Primary model for general tasks and conversations                                   │
│                                                                                       │
│   Task Model                                anthropic glm-4.5                         │
│   Reasoning Model                           anthropic glm-4.5                         │
│   Quick Model                               anthropic glm-4.5                         │
│   Manage Model List                                                                   │
│                                                                                       │
│                                                                                       │
│ Use ↑/↓ to navigate, Space to cycle models, Enter to configure, d to clear, Esc to    │
│ exit                                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────╯
```
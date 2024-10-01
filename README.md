<h1>
  <img src="asset/glm.png" alt="glm" style="height: 1.5em; vertical-align: bottom;" />
  glm-cookbook
</h1>

[Read this in English](README_en.md)

欢迎来到 GLM API 模型入门仓库📘。这是一本开源的 GLM API 入门代码教材。

在这里，你会发现丰富的 **代码示例👨‍**、**实用指南🗺**️ 以及 **资源链接🔗**，或许能帮助你轻松掌握 GLM API 的使用！

## 更新情况 🔥

+ 🔥 2024-10-01: 本CookBook更新了 [多工具调用教程](basic/glm_multi_functions_call.ipynb)，清更新`requirments.txt`中的依赖，欢迎查看。 
+ 🔥 2024-09-26: 本CookBook更新了 [GraphRAG 教程](demo/graphrag)，欢迎查看。 
+ 🔥 2024-07-26: 本CookBook更新了 [CogVideoX 视频生成模型调用教程](vision/cogvideox_pysdk.ipynb)，欢迎查看。 
+ 🔥 2024-07-20: 本CookBook更新了 [CharacterGLM & Emohaa 调用教程](basic/character_glm_pysdk.ipynb) 和 [glm-4v小目标识别手册](vision/glm-v_small_text_recognition.ipynb)。
+ 🔥 2024-07-13: 本CookBook更新了 [LangChain-GLM](https://github.com/MetaGLM/langchain-glm)
  框架的[简单使用手册](glm_langchain_glm_framework.ipynb)。
+ 🔥 2024-06-25: 本CookBook更新了快速从 OpenAI API 切换成 GLM API 模型的适配 [教程](basic/openai2zhipu.ipynb), 欢迎查看。
+ 🔥 2024-05-25: Batch API 教程更新，您可以在[这里](basic/glm_batch_api.ipynb) 查看教程。
+ 🔥 2024-05-10: GLMs 智能体API基础调用教程更新, 您可以在 [这里](glms/glms_api_call.md) 查看教程。
+ 🔥 2024-04-28: ZhipuAI Pyton SDK 更新，请您更新SDK以适配最新教程。
+ 🔥 2024-04-23: GLM-4 已支持使用 OpenAI SDK 接入，大幅降低了开发替换成本！
+ 🔥 2024-03-18: 仓库开始更新 [智谱清言](glms) 基础开发者教学文档，基础提示词文档 和 智能体文档
  已经在 [技术文档](https://zhipu-ai.feishu.cn/wiki/SPyFwjSI7iOCoCksq2sc3Eb7nXd) 推出，欢迎体验和留言，我们将继续快速迭代！
+ 🔥 2024-03-06: 仓库所在组织 [MetaGLM](https://github.com/MetaGLM) 更新了4门语言 (Python, Java,C#,Node.js)
  的SDK，欢迎提出意见和对项目进行PR！

## 精选文章 💫

以下表格展现了本教程中有精选的 demo 文章地址，开发者可以在这里寻找到一些经典的案例和教程。

| 文章标题                  | 链接                                                |
|-----------------------|---------------------------------------------------|
| 智谱清言智能体 API 调用指南      | [查看教程](glms/glms_api_call.md)                     |
| 智谱清言智能体调用第三方 API 使用指南 | [查看教程](glms/glms_custom_api_plugin.md)            |
| GLM-4V 小目标识别          | [查看教程](vision/glm-v_small_text_recognition.ipynb) |
| 多角色模拟 Agent系统         | [查看教程](demo/agent/glm_multi_role_division.ipynb)  |
| Agent 数据集制作手册         | [查看教程](demo/generate_agent_dataset)               |
| 信息抽取示例                | [查看教程](demo/glm_infomation_extraction.ipynb)      |
| CSV 数据分析              | [查看教程](demo/glm_csv_data_analysis.ipynb)          |
| OCR + GLM 实现扫描文件对话    | [查看教程](demo/ppocr_glm.ipynb)                      |
| 梦境之旅心理体验              | [查看教程](demo/interpretationo_dreams)               |
| hugging face 每日论文解读   | [查看教程](demo/hf-daily-paper-newsletter-chinese)    |

## 快速开始 🚀

1. 要开始使用GLM API，你首先需要一个 GLM API 账户和相应的 API 密钥。
   如果你还没有账户，可以在 [这里](https://zhipuaishengchan.datasink.sensorsdata.cn/t/Q) 免费注册。

2. 我的代码以 **Python, Jupyter Note** 为主，但同样的概念也可以应用于其他编程语言（不过这可能要你们自己实现咯）。
   这些代码示例旨在帮助我（或许也能对你）如何高效地使用 GLM API 完成常见的简单任务。 推荐使用`Python 3.9 - 3.12`
   的版本（我自己是Python 3.10）。你需要安装必须的依赖，才能更好的使用 Demo。你可以使用以下命令来安装总的依赖：

```bash
pip install -r requirements.txt
```

## 仓库文件 📂

我已经分类好了多个文件夹，这些文件夹都有自己的内容，你可以根据自己的需求来查看！

+ 🌱`basic` 最基础的内容，帮助你熟悉基本的 API 调用。

+ 👁️`vision` 关于视觉模型和绘图模型的调用和基本应用。

+ 🔧`finetune` 或许可以来这里找找微调的内容？

+ 🎉`demo` 一些有趣的小项目，或许可以激发点灵感。
    + 🤖`agent` 看看发布会的智能体有多厉害！
    + 📚`data` 运行demo所需要的数据。

+ 📊`glms` 智能体 (智谱清言) 专区，即使你不会代码，也能快速上手！

+ 🏠`asset` 一些相关的图片资料

你可以通过以下图片快速了解本仓库构成, 我将尽快同步更新 Zhipu AI SDK的最新实验和教学内容。

![实现原理图](asset/plan.png)

## 开源SDK

GLM-4系列SDK已经开源，如果你想直接在我们的SDK上进行修改，可以按照以下地址进行需改：

+ [Python SDK](https://github.com/MetaGLM/zhipuai-sdk-python-v4)
+ [Java SDK](https://github.com/MetaGLM/zhipuai-sdk-java-v4)
+ [C# SDK](https://github.com/MetaGLM/zhipuai-sdk-csharp-v4)
+ [Node.js SDK](https://github.com/MetaGLM/zhipuai-sdk-nodejs-v4)
+ 如果你有其他语言的SDK想贡献到官方仓库，欢迎提出PR。

## 贡献指南 🤝

欢迎大家贡献自己的想法和代码！如果你有任何建议或想添加自己的代码，请随时提交 Pull Request 或开 Issue 讨论。
如果你喜欢这个仓库，欢迎给它一个 ⭐，这将对我有很大帮助！

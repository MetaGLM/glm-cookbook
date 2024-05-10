# 使用智谱清言提供的API调用自己制作的智能体

**This tutorial is Only in Chinese explanation**

智谱清言支持使用API来调用开发者自己创作的智能体（GLMs）。本教程将帮助你了解如何使用 API 来调用自己的GLMs。

## 1. 获取自己的API Key

首先，完成智谱清言的实名认证之后，进入 [开发者界面](https://chatglm.cn/developersPanel/apiSet)。在这里，你可以自己生成一个API Key。
你将会获得两个内容：`Key` 和 `Secret`。如图所示：

![API KEY](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/glms_api/1.png)


## 2. 获取自己的智能体ID

在调用之前，我们需要自己的智能体ID。您需要使用 网页版的智谱清言，进入自己的智能体，并复制浏览器中的ID，如图所示：

![GLMs ID](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/glms_api/2.png)

在这个案例中，`65f3dab425fab01c6821d461`是您的智能体ID。

虽然您可以在网页端访问他人的GLMs，但是，您无法通过API调用他人的智能体，仅仅只能调用自己的智能体。

## 3. 使用API Key 调用自己的GLMs

在这里，我们将使用 Python 代码来调用自己的GLMs。我们将会为大家提供简单的示例代码，您可以参考[智谱清言 智能体 API 调用示例](api)中的代码来进行调用。


## 4. 查看自己的统计用量

该功能暂时不可用，我们将会在后续版本中提供。



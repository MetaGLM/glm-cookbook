# 在GLMs 中插入自己的 API 作为一个插件

**This tutorial is Only in Chinese explanation**

GLMs 支持使用满足条件的 Open API 来添加额外的插件。本教程将帮助你了解如何使用 GLMs 的 API 来添加自己的插件。

与 GPTs Action 相同，使用 GLMs 也能自定义引入外部的API 作为信息参考来源，本教程展示如何配置并使用 Open API 的方式进行调用。

## 1. 使用 GLMs 自定义API 构建天气查询组件

我们将要点击图中的 `添加新API` 按钮来添加一个新的API。

![添加新API](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/build_outside_api/1.png)

我们使用 ```心知天气 API``` 作为示例，构建一个天气查询组件。首先，我们需要注册并获取 API 的 `appkey`。
假设你的API Key是：

```python
app_key = 'API_KEY'
```

## 2. 构建 Open API 格式的内容

如果你熟悉 Open API 的格式，你可以直接构建一个 Open API 的格式。
在这里，我们将根据 [知心天气官方请求示例](https://github.com/seniverse/seniverse-api-demos/blob/master/javascript/index.html)
直接转写一个 OpenAPI 格式。
我们根据将 API 请求转写为 Open API 的格式，以便 GLMs 能够识别和调用。下面是一个使用 yaml 格式的示例：

```yaml
openapi: 3.0.1
info:
  title: Simple Weather API
  description: API for retrieving weather data based on location.
  version: 1.0.0
servers:
  - url: https://api.seniverse.com/v3/weather
paths:
  /now.json:
    get:
      tags:
        - Weather Data Retrieval
      summary: Retrieve Current Weather Data
      operationId: getCurrentWeather
      description: 获得当前天气
      parameters:
        - name: location
          in: query
          description: Location for which the current weather data is needed.
          required: true
          schema:
            type: string
        - name: key
          in: query
          description: API key for authentication.
          required: true
          schema:
            type: string
            enum: [ **app_key** ]
        - name: language
          in: query
          description: Language for the weather information.
          schema:
            type: string
            default: zh-Hans
        - name: unit
          in: query
          description: Unit for temperature measurement.
          schema:
            type: string
            default: c
      responses:
        '200':
          description: Successful response with weather data
          content:
            application/json:
              schema:
                type: object
                properties:
                  location:
                    type: string
                  temperature:
                    type: string
                  conditions:
                    type: string
                  # Other relevant weather properties
        default:
          description: Error response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string

```

如果您不能很好的直接自己完成 Open API 文件的书写，您也可以选择使用我们提供的 `API 配置助手` 功能来生成 Open API
文件。在这里，我们将使用 `API 配置助手` 功能来生成 Open API 文件。
![智能体帮助](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/build_outside_api/2.png)

## 3.测试智能体

完成构建后，我们需要就是将这个 Open API 文件 上传到 GLMs
中。接着，我们就可以对智能体进行测试，我们将在如下界面中，点击 `测试` 按钮发送测试请求。
![测试智能体](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/build_outside_api/3.png)

<span style='color: red; font-weight: bold;'>请注意，如果在测试的过程中调用了 `代码生成`, `联网查询`
等功能，需要在测试前先关闭这两个功能。</span>

## 4. 使用调整好的智能体

测试通过之后，就可以返回上一级，此时，外部API功能就已经完成。智能体将会根据用户需求来请求天气信息。并返回用户天气情况。
![运行智能体](https://raw.githubusercontent.com/MetaGLM/glm-cookbook/main/glms/asset/build_outside_api/4.png)

## 常见问题

1. 如何获取API Key？

   A：通常，你需要注册并登录到API提供商的网站，然后在网站上创建一个新的应用程序，然后你将会得到一个API Key。
2. 一定要使用OpenAPI格式吗？

   A：一定的，但是可以使用 Json 或者 Yaml 格式，在智谱清言中，我们也为大家提供了两个固定的模板。
3. 能否使用具有 API Key 鉴权的方式？

   A：支持，你可以在配置处单独填写 API Key。支持`Basic`,`Bearer`,`Custom`三种模式。
4. 为什么我没有找到自定义API key的功能？

   A： 您没有完成实名认证。
5. 什么API都可以接入吗？

   A： 需要通过我们的白名单系统的API才能接入，同时，发布带有第三方API功能的智能体需要通过我们的审核。
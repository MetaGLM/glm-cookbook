import os
import json
from datetime import datetime, timedelta, timezone
from openai import OpenAI

# 获取当前UTC时间
current_utc_time = datetime.now(timezone.utc)
print(f"当前 UTC 日期和时间: {current_utc_time}")

# 将UTC时间转换为北京时间 (UTC+8)
beijing_timezone = timezone(timedelta(hours=8))
current_beijing_time = current_utc_time.astimezone(beijing_timezone)
print(f"当前北京时间和时间: {current_beijing_time}")

# 计算查询的日期(前一天)
yesterday_beijing = current_beijing_time - timedelta(days=1)
yesterday_str = yesterday_beijing.strftime('%Y-%m-%d')
print(f"查询的日期: {yesterday_str}")

# 文件名假设为 "YYYY-MM-DD.json"
filename = f"{yesterday_str}.json"

# 搜索文件的根目录（可根据需要修改）
root_directory = '.'

# 搜索文件
file_path = None
for dirpath, dirnames, filenames in os.walk(root_directory):
    if filename in filenames:
        file_path = os.path.join(dirpath, filename)
        break

if file_path:
    # 读取JSON文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # 将文件内容转换为字符串
    user_content = json.dumps(data, ensure_ascii=False)
else:
    user_content = f"文件 {filename} 不存在"

try:
    # 在环境变量中设置OPENAI_API_BASE为您部署的zhipuai-agent-to-openai服务地址
    BASE_URL = os.getenv("OPENAI_API_BASE", "http://8.130.209.127:8000/v1")
    # 在环境变量中设置OPENAI_API_KEY为第一步拼接获得的API Key或者直接填写
    API_KEY = "51d5350a075931c7.fa2eab916c0705fd6b120434ddd98e96"

    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    # 调用对话补全接口
    result = client.chat.completions.create(
        # 必须填写您自己创建的智能体ID，否则无法调用成功
        model="660d7a0614c0acd012a10dc4",
        # 目前多轮对话基于消息合并实现，某些场景可能导致能力下降且受单轮最大token数限制
        # 如果您想获得原生的多轮对话体验，可以传入首轮消息获得的id，来接续上下文
        # "conversation_id": "65f6c28546bae1f0fbb532de",
        messages=[
            {"role": "system", "content": "你是一个论文结构化助手，你的任务是将user部分的其他无关内容去除，只输出每篇文章的题目的中文翻译和id"},
            {"role": "user", "content": user_content},
        ],
        # 如果使用SSE流请设置为true，默认false
        stream=False
    )

    # 初始化用于保存结果的列表
    structured_data = []
    for choice in result.choices:
        structured_data.append(choice.message.content)

    # 创建保存文件夹
    output_folder = 'HF-day-paper+GLMs-api-clean'
    os.makedirs(output_folder, exist_ok=True)

    # 生成新的文件名并保存到指定文件夹
    clean_filename = os.path.join(output_folder, f"{yesterday_str}_clean.json")

    # 将结构化数据写入新的JSON文件
    with open(clean_filename, 'w', encoding='utf-8') as clean_file:
        json.dump(structured_data, clean_file, ensure_ascii=False, indent=4)

    print(f"结构化数据已保存到 {clean_filename}")

except ValueError as e:
    print(f"发生错误: {e}")
except Exception as e:
    print(f"发生异常: {e}")










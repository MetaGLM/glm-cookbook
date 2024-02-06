
### 介绍

- 关于角色标签卡
```text

通过`爱情语义学`符号系统运作，角色被赋予了更加真实，更加有说服力的形象
每个角色都有一个标签卡，这个标签卡是一个角色的基本信息，
包括角色的性格、经历、目的、行为,对一些问题的看法
通过langchain代码的形式存储，本项目设计了一个存储系统，用于存储这些标签卡
您可以导出langchain代码来单独运行这个角色信息
```

- 导出langchain代码角色标签卡

persist_dir参数是存储路径 ，可从下方[抖音数据分析整理角色标签卡](#抖音数据分析整理角色标签卡)获取

代码如下
```python
from dreamsboard.engine.loading import load_store_from_storage
from dreamsboard.engine.storage.storage_context import StorageContext
storage_context = StorageContext.from_defaults(persist_dir="./storage")
code_gen_builder = load_store_from_storage(storage_context)
executor = code_gen_builder.build_executor()
print(executor.executor_code)
```

##### 抖音数据分析整理角色标签卡

- [01_宝今天煮饺子把皮煮开了原来是喜欢你露馅儿了_阿七.md](coplay_analysis%2F01_%E5%AE%9D%E4%BB%8A%E5%A4%A9%E7%85%AE%E9%A5%BA%E5%AD%90%E6%8A%8A%E7%9A%AE%E7%85%AE%E5%BC%80%E4%BA%86%E5%8E%9F%E6%9D%A5%E6%98%AF%E5%96%9C%E6%AC%A2%E4%BD%A0%E9%9C%B2%E9%A6%85%E5%84%BF%E4%BA%86_%E9%98%BF%E4%B8%83.md)
- [02_尊嘟假嘟呀_今天要吃三碗饭.md](coplay_analysis%2F02_%E5%B0%8A%E5%98%9F%E5%81%87%E5%98%9F%E5%91%80_%E4%BB%8A%E5%A4%A9%E8%A6%81%E5%90%83%E4%B8%89%E7%A2%97%E9%A5%AD.md)
- [03_报备式恋爱请查收_澈洌.md](coplay_analysis%2F03_%E6%8A%A5%E5%A4%87%E5%BC%8F%E6%81%8B%E7%88%B1%E8%AF%B7%E6%9F%A5%E6%94%B6_%E6%BE%88%E6%B4%8C.md)
- [04_心里闷闷的可能就是有点想你_辰夕.md](coplay_analysis%2F04_%E5%BF%83%E9%87%8C%E9%97%B7%E9%97%B7%E7%9A%84%E5%8F%AF%E8%83%BD%E5%B0%B1%E6%98%AF%E6%9C%89%E7%82%B9%E6%83%B3%E4%BD%A0_%E8%BE%B0%E5%A4%95.md)
- [05_报告今天是香香的姐姐_阿七.md](coplay_analysis%2F05_%E6%8A%A5%E5%91%8A%E4%BB%8A%E5%A4%A9%E6%98%AF%E9%A6%99%E9%A6%99%E7%9A%84%E5%A7%90%E5%A7%90_%E9%98%BF%E4%B8%83.md)
- [06_今日的温柔报告_兔兔没有牙.md](coplay_analysis%2F06_%E4%BB%8A%E6%97%A5%E7%9A%84%E6%B8%A9%E6%9F%94%E6%8A%A5%E5%91%8A_%E5%85%94%E5%85%94%E6%B2%A1%E6%9C%89%E7%89%99.md)
- [07_报告今天发工资啦啦啦啦_阿七.md](coplay_analysis%2F07_%E6%8A%A5%E5%91%8A%E4%BB%8A%E5%A4%A9%E5%8F%91%E5%B7%A5%E8%B5%84%E5%95%A6%E5%95%A6%E5%95%A6%E5%95%A6_%E9%98%BF%E4%B8%83.md)
- [08_78块的冰淇淋掉地上了呜呜呜呜_阿七.md](coplay_analysis%2F08_78%E5%9D%97%E7%9A%84%E5%86%B0%E6%B7%87%E6%B7%8B%E6%8E%89%E5%9C%B0%E4%B8%8A%E4%BA%86%E5%91%9C%E5%91%9C%E5%91%9C%E5%91%9C_%E9%98%BF%E4%B8%83.md)

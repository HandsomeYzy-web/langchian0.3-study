import asyncio
import os
import time
from os import stat_result

import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

dotenv.load_dotenv()

# 初始化聊天模型
chat_model = ChatOpenAI(
    model="qwen3-max",
    temperature=0,
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    streaming=True,
)

# 同步调用（对比组）
def sync_test():
    messages1 = [
        SystemMessage(content="你是一个有帮助的助手。"),
        HumanMessage(content="请简要介绍一下人工智能的发展历史。"),
    ]
    start_time = time.time()
    response = chat_model.invoke(messages1) #同步调用
    duration = time.time() - start_time
    print(f"同步调用响应时间: {duration:.2f}秒")
    return response, duration

# 异步调用（实验组）
async def async_test():
    messages2 = [
        SystemMessage(content="你是一个有帮助的助手。"),
        HumanMessage(content="请简要介绍一下机器学习的基本概念。"),
    ]
    start_time = time.time()
    response = await chat_model.ainvoke(messages2) #异步调用
    duration = time.time() - start_time
    print(f"异步调用响应时间: {duration:.2f}秒")
    return response, duration

# 运行测试
if __name__ == "__main__":
    # 同步测试
    sync_response, sync_duration = sync_test()
    print("同步响应内容:", sync_response.content)

    # 异步测试
    async_response, async_duration = asyncio.run(async_test())
    print("异步响应内容:", async_response.content)

    # 并发测试 - 修复版本
    print("\n开始并发异步调用测试...")
    stat_time = time.time()

    async def run_concurrent_tests():
        # 创建多个异步任务
        tasks = [async_test() for _ in range(5)]
        # 并发执行任务
        return await asyncio.gather(*tasks)

    # 运行并发测试
    results = asyncio.run(run_concurrent_tests())

    total_duration = time.time() - stat_time
    print(f"并发异步调用总响应时间: {total_duration:.2f}秒")
    for i, (response, duration) in enumerate(results):
        print(f"任务 {i+1} 响应时间: {duration:.2f}秒, 内容: {response.content}")
import dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

llm = ChatOpenAI(
    model="qwen3-max",
    temperature=0,
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

response = llm.invoke("什么是大模型？")
print(response)

#使用提示词模板

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "你是世界级的技术文档编写者"},
    {"role": "user", "content": "{input}"}
])

chain = prompt | llm
message = chain.invoke({"input": "大模型中的langchain是什么？"})
print(message)

#使用输出解析器

# output_parser = StrOutputParser()
output_parser = JsonOutputParser()

chain = prompt | llm | output_parser
message = chain.invoke({"input": "用json格式描述大模型的三个应用场景"})
print(message)

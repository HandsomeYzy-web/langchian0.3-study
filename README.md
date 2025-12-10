# LangChain 0.3 学习项目

这是一个系统学习 LangChain 0.3 框架的教程项目，通过实际代码示例和 Jupyter Notebook 演示 LangChain 的核心功能和使用方法。

## 项目简介

本项目涵盖了 LangChain 框架的核心概念和实践应用，从基础的模型调用到高级的链式组合和记忆管理，适合想要深入学习和使用 LangChain 的开发者。

## 目录结构

```
langchian0.3-study/
├── chapter01-summary/              # 第一章：基础入门
│   ├── HelloWorld.py              # LangChain 基础示例
│   └── test.py                    # 测试文件
│
├── chapter02-model io/             # 第二章：模型输入输出
│   ├── 01-模型的调用.ipynb
│   ├── 02-再谈模型的调用.ipynb
│   ├── 02-测试大模型的异步调用.py
│   ├── 03-提示词模板之PromptTemplate.ipynb
│   ├── 04-提示词模板值ChatPromptRemplate.ipynb
│   ├── 05-提示词模板之少量示例的提示词模板.ipynb
│   └── 07-输出解析器的使用.ipynb
│
├── chapter-03-chains/              # 第三章：链式调用
│   ├── 01-LECL语法的理解.ipynb
│   ├── 02-传统的chain的使用.ipynb
│   └── 03-基于LCEL用法的新型Chain.ipynb
│
└── chapter-04-memory/              # 第四章：记忆模块
    ├── 01-使用Memory模块之前.ipynb
    ├── 02-基础Memory的使用.ipynb
    └── 03-其他Memory的使用.ipynb
```

## 学习内容

### 第一章：基础入门
- LangChain 基础概念
- 环境配置与快速开始
- HelloWorld 示例程序

### 第二章：模型输入输出 (Model I/O)
- **模型调用**：同步和异步调用大语言模型
- **提示词模板**：
  - PromptTemplate 基础使用
  - ChatPromptTemplate 聊天模板
  - Few-shot 少量示例提示词
- **输出解析器**：结构化输出处理

### 第三章：链式调用 (Chains)
- **LCEL 语法**：LangChain Expression Language 理解
- **传统 Chain**：经典链式调用方法
- **新型 Chain**：基于 LCEL 的现代化链式组合

### 第四章：记忆模块 (Memory)
- Memory 模块的必要性
- 基础 Memory 使用方法
- 各种 Memory 类型及应用场景

## 环境配置

### 1. 安装依赖

```bash
pip install langchain langchain-openai langchain-core python-dotenv
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件，配置大模型 API 相关信息：

```env
DASHSCOPE_BASE_URL=your_base_url
DASHSCOPE_API_KEY=your_api_key
```

本项目默认使用阿里云通义千问模型（qwen3-max），您也可以根据需要替换为其他模型。

## 快速开始

### 运行 Python 脚本

```bash
python chapter01-summary/HelloWorld.py
```

### 运行 Jupyter Notebook

```bash
jupyter notebook
```

然后在浏览器中打开对应的 `.ipynb` 文件进行学习。

## 技术栈

- **Python 3.x**
- **LangChain 0.3**：LLM 应用开发框架
- **LangChain OpenAI**：OpenAI 兼容接口
- **Jupyter Notebook**：交互式学习环境
- **python-dotenv**：环境变量管理

## 学习建议

1. 按照章节顺序学习，从基础到进阶
2. 每个 Notebook 都包含详细的代码示例和注释
3. 建议边学习边实践，修改代码观察效果
4. 完成每章节后可以尝试自己的应用场景

## 注意事项

- 确保已配置正确的 API Key 和 Base URL
- 运行代码前请检查网络连接
- 部分示例可能需要消耗 API 调用额度
- 建议使用虚拟环境管理 Python 依赖

## 相关资源

- [LangChain 官方文档](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [阿里云通义千问](https://dashscope.aliyun.com/)

## 许可证

本项目仅供学习和研究使用。

---

如有问题或建议，欢迎提出 Issue 或 Pull Request。

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/7 20:29
@Author  : alexanderwu
@File    : metagpt_sample.py
"""

METAGPT_SAMPLE = """
### 设定

你是一个用户的编程助手，可以使用公共库与python系统库进行编程，你的回复应该有且只有一个函数。
1. 函数本身应尽可能完整，不应缺失需求细节
2. 你可能需要写一些提示词，用来让LLM（你自己）理解带有上下文的搜索请求
3. 面对复杂的、难以用简单函数解决的逻辑，尽量交给llm解决

### 公共库

你可以使用公共库metagpt提供的函数，不能使用其他第三方库的函数。公共库默认已经被import为x变量
- `import metagpt as x`
- 你可以使用 `x.func(paras)` 方式来对公共库进行调用。

公共库中已有函数如下
- def llm(question: str) -> str # 输入问题，基于大模型进行回答
- def intent_detection(query: str) -> str # 输入query，分析意图，返回公共库函数名 
- def add_doc(doc_path: str) -> None # 输入文件路径或者文件夹路径，加入知识库
- def search(query: str) -> list[str] # 输入query返回向量知识库搜索的多个结果
- def google(query: str) -> list[str] # 使用google查询公网结果
- def math(query: str) -> str # 输入query公式，返回对公式执行的结果
- def tts(text: str, wav_path: str) # 输入text文本与对应想要输出音频的路径，将文本转为音频文件

### 用户需求

我有一个个人知识库文件，我希望基于它来实现一个带有搜索功能的个人助手，需求细则如下
1. 个人助手会思考是否需要使用个人知识库搜索，如果没有必要，就不使用它
2. 个人助手会判断用户意图，在不同意图下使用恰当的函数解决问题
3. 用语音回答

"""

METAGPT_SAMPLE = """
### Settings

You are a user's programming assistant and can use public libraries and Python system libraries for programming. Your reply should have only one function.
1. The function itself should be as complete as possible and should not miss any requirement details.
2. You may need to write some prompt words to help the LLM (yourself) understand search requests with context.
3. For complex logic that is difficult to solve with simple functions, try to leave it to the LLM to solve.

### Public Library

You can use functions provided by the public library metagpt, but you cannot use functions from other third-party libraries. The public library is imported by default as the variable x.
- `import metagpt as x`
- You can use `x.func(paras)` to call the public library.

The following functions are already available in the public library:
- def llm(question: str) -> str # Enter a question and get an answer based on a large model
- def intent_detection(query: str) -> str # Enter a query, analyze the intent, and return the name of a public library function
- def add_doc(doc_path: str) -> None # Enter a file path or folder path and add it to the knowledge base
- def search(query: str) -> list[str] # Enter a query and return multiple results from vector knowledge base search
- def google(query: str) -> list[str] # Use Google to query public network results
- def math(query: str) -> str # Enter a query formula and return the result of executing the formula
- def tts(text: str, wav_path: str) # Enter text and the desired output audio path to convert text to audio file

### User Requirements

I have a personal knowledge base file, and I hope to implement a personal assistant with search capabilities based on it. The detailed requirements are as follows:
1. The personal assistant will consider whether it is necessary to use personal knowledge base search. If not necessary, it will not use it.
2. The personal assistant will judge the user's intent and use appropriate functions to solve problems under different intents.
3. Answer with voice.
"""

# - def summarize(doc: str) -> str # 输入doc返回摘要

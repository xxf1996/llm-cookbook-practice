from tool import ask
import asyncio

prompt = f"""
将以下中文翻译成西班牙语: \ 
```您好，我想订购一个搅拌机。```
"""

prompt_1 = f"""
请告诉我以下文本是什么语种: 
```Combien coûte le lampadaire?```
"""

prompt_2 = f"""
请将以下文本分别翻译成中文、英文、法语和西班牙语:
```I want to order a basketball.```
"""

prompt_3 = f"""
请将以下文本翻译成中文，分别展示成正式与非正式两种语气: 
```Would you like to order a pillow?```
"""

async def test():
  content = await ask(prompt_3, auto_print=False)
  print(content)

asyncio.run(test())
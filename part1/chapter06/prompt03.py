from tool import ask
import asyncio

prompt = f"""
将以下文本翻译成商务信函的格式（注意首尾格式不要有重复和冗余的部分）:
```小老弟，我小羊，上回你说咱部门要采购的显示器是多少寸来着？```
"""

asyncio.run(ask(prompt))
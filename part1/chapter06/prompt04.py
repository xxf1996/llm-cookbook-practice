from tool import ask
import asyncio

data_json = { "resturant employees" :[
  {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
  {"name":"Bob", "email":"bob32@gmail.com"},
  {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
将以下Python字典从JSON转换为HTML表格，保留表格标题和列名：{data_json}

不要使用代码，输出最终的HTML表格及表格的标题。
"""

asyncio.run(ask(prompt))

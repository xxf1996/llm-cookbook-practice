import openai
from openai import AsyncOpenAI

openai.base_url = 'http://localhost:8000/v1'

client = AsyncOpenAI(
  base_url='http://localhost:8000/v1',
  api_key='free',
)

async def ask(content: str):
  print(client.base_url)
  stream = await client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}],
    stream=True,
    temperature=0.3
  )
  async for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

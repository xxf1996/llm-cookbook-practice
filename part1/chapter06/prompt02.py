from tool import ask
import asyncio

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                             # My screen is flashing
]

async def translation():
  for message in user_messages:
    prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号: ```{message}```"
    lang = await ask(prompt, auto_print=False)
    print(f"原始消息 ({lang}): {message}\n")

    prompt_1 = f"""
    将以下消息分别翻译成英文和中文，并写成
    中文翻译：xxx
    英文翻译：yyy
    的格式：
    ```{message}```
    """

    await ask(prompt_1)

    print("\n=========================================\n")

asyncio.run(translation())

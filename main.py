import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("X_A_R4")
    await user.join_chat("X_A_R0")
    await user.join_chat("X_A_R3")
    await idle()
    print("[INFO]: STOPPING BOT & fi0nabot")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

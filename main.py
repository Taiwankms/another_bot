import logging
from aiogram import Bot, Dispatcher, types
import asyncio

from aiogram.filters import Text
from aiogram.types import BotCommand, BotCommandScopeDefault

token = "6036003975:AAHLAnkY1_6Z-TXCgIVYowIm2towOAhpTvs"
admin_id = 683197836
logger = logging.getLogger(__name__)


async def commandos(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='заставляет этого бота работать',
        ),
        BotCommand(
            command='help',
            description='ща помогу',
        )
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())


async def send_mess_on(bot: Bot):
    await commandos(bot)
    await bot.send_message(admin_id, text="Бот делает вид что работает!")


async def send_mess_off(bot: Bot):
    await bot.send_message(admin_id, text="Бот отдыхает!")


async def text(message: types.Message):
    await message.answer("Никто уже давным давно не говорит " + message.text + ", ты что старпер?")


async def echo(message: types.Message):
    print("Полученное сообщение в боте: " + message.text)
    await message.answer(message.text)


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")
    bots = Bot(token)
    dp = Dispatcher()

    dp.message.register(text, Text(text='Салют'))
    dp.message.register(echo)

    dp.startup.register(send_mess_on)
    dp.shutdown.register(send_mess_off)
    await dp.start_polling(bots)


if __name__ == "__main__":
    asyncio.run(start())

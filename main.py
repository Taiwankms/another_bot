import logging
from aiogram import Bot, Dispatcher, types, F
import asyncio

from aiogram.filters import Text, Command
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


async def hi_admin(message: types.Message):
    await message.answer("Ну что, Админ, погнали?")


async def picture(message: types.Message):
    await message.answer("Ну и к чему ты мне это отправил?")


async def say_start(message: types.Message):
    await message.reply("Ну что, погнали?")


async def say_help(message: types.Message):
    await message.reply("Думаешь я смогу тебе помочь?")


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

    dp.startup.register(send_mess_on)
    dp.shutdown.register(send_mess_off)

    dp.message.register(picture, F.content_type == 'photo')
    dp.message.register(picture, F.content_type == 'sticker')
    dp.message.register(picture, F.content_type == 'animation')
    dp.message.register(hi_admin, F.from_user.id == admin_id, F.text == 'Привет')
    dp.message.register(say_start, Command(commands=['start', 'go']))
    dp.message.register(say_help, Command(commands='help'))
    dp.message.register(text, Text(text='Салют'))
    dp.message.register(echo)


    await dp.start_polling(bots)


if __name__ == "__main__":
    asyncio.run(start())

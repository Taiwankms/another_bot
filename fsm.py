import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import BotCommand, BotCommandScopeDefault


class States(StatesGroup):
    first_name = State()
    last_name = State()
    telephone = State()
    complete = State()


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


async def say_start(message: types.Message, state: FSMContext):
    await message.reply("Введите то сё, ну вы понели. \nВведите имя:")
    await state.set_state(States.first_name)


async def first_name(message: types.Message, state: FSMContext):
    await message.answer("Ну и имя у тебя, сочувствую: " + message.text + "\nВводи фамилию: ")
    await state.update_data(first_name=message.text)
    await state.set_state(States.last_name)


async def last_name(message: types.Message, state: FSMContext):
    await message.answer("Фамилия еще лучше, как ты живешь вообще?: " + message.text + "\nВводи телефон: ")
    await state.update_data(last_name=message.text)
    await state.set_state(States.telephone)


async def telephone(message: types.Message, state: FSMContext):
    await message.answer("Ну хоть номер норм: " + message.text)
    await state.update_data(telephone=message.text)
    await state.set_state(States.complete)
    data = await state.get_data()
    await message.answer("Введенные данные: \n"
                         f"Имя - {data['first_name']}\n"
                         f"Фамилия - {data['last_name']}\n"
                         f"Телефон - {data['telephone']}\n"
                         f"Подтверди или нет, мне пох")


async def complete(message: types.Message, state: FSMContext):
    await message.answer("Данные приняты ")
    await state.clear()


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Все херня, давай по новой ")
    await state.clear()


async def say_help(message: types.Message):
    await message.answer("Думаешь я смогу тебе помочь?")


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")
    bots = Bot(token)
    dp = Dispatcher()

    dp.startup.register(send_mess_on)
    dp.shutdown.register(send_mess_off)

    dp.message.register(cancel, Text(text='cancel', ignore_case=True))
    dp.message.register(say_start, Command(commands=['start', 'go']))
    dp.message.register(say_help, Command(commands='help'))
    dp.message.register(first_name, States.first_name)
    dp.message.register(last_name, States.last_name)
    dp.message.register(telephone, States.telephone)
    dp.message.register(complete, States.complete, Text(text='finish', ignore_case=True))

    await dp.start_polling(bots)


if __name__ == "__main__":
    asyncio.run(start())

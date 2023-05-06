from aiogram import Bot, types, F, Dispatcher
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import BotCommand, BotCommandScopeDefault, CallbackQuery

from DraftBot.keyboard.inline import kb_confirm

admin_id = 683197836


class States(StatesGroup):
    first_name = State()
    last_name = State()
    telephone = State()
    complete = State()


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


async def send_mess_on1(bot: Bot):
    await commandos(bot)
    await bot.send_message(admin_id, text="Hello world!")


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
                         f"Подтверди или нет, мне пох",
                         reply_markup=kb_confirm)


async def confirm(call: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    await call.answer("Данные приняты ")
    await bot.answer_callback_query(call.id, 'ok', show_alert=True)
    await state.clear()


async def cancel(call: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    await call.answer("Все херня, давай по новой ")
    await state.clear()


async def say_help(message: types.Message):
    await message.answer("Думаешь я смогу тебе помочь?")


async def picture(message: types.Message):
    if message.photo:
        await message.answer('Ну и нахер ты мне это прислал?')


def register_fsm(dp: Dispatcher):
    dp.callback_query.register(confirm, States.complete, F.data == 'confirm')
    dp.callback_query.register(cancel, States.complete, F.data == 'cancel')
    dp.message.register(cancel, Text(text='cancel', ignore_case=True))
    dp.message.register(say_start, Command(commands=['start', 'go']))
    dp.message.register(say_help, Command(commands='help'))
    # dp.message.register(picture)
    dp.message.register(first_name, States.first_name)
    dp.message.register(last_name, States.last_name)
    dp.message.register(telephone, States.telephone)


from aiogram import types, Dispatcher


async def echo(message: types.Message):
    print("Получено новое сообщение" + message.text)
    await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.message.register(echo)


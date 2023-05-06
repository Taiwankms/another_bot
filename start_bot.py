import asyncio
import logging

from aiogram import Bot, Dispatcher

from DraftBot.handlers.echo import register_echo
from DraftBot.handlers.fsm import send_mess_on, send_mess_off, register_fsm, send_mess_on1

logger = logging.getLogger(__name__)


def handlers(dp):
    register_fsm(dp)
    register_echo(dp)


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")
    bots = Bot("6036003975:AAHLAnkY1_6Z-TXCgIVYowIm2towOAhpTvs")
    dp = Dispatcher()

    dp.startup.register(send_mess_on)
    dp.startup.register(send_mess_on1)
    dp.shutdown.register(send_mess_off)

    handlers(dp)

    try:
        await dp.start_polling(bots)
    except:
        pass


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except:
        pass

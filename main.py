import asyncio
import logging
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from bot.dispetcher import router
from bot.handler import *

dp = Dispatcher()
TOKEN = "7686147968:AAGkFbSlzB1edNECe4hc_rbtwGKm0wvtLJ0"


async def main() -> None:
    i18n = I18n(path='locales')
    dp.include_router(router)
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.utils import executor

from app import utils, config
from app import handlers, middlewares


async def on_startup(dispatcher: Dispatcher):
    handlers.setup(dp)
    middlewares.setup(dp)
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(config.SUPERUSER_IDS)


if __name__ == '__main__':
    utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = JSONStorage(config.WORK_PATH / 'app' / 'storage.json')
    dp = Dispatcher(bot=bot, storage=storage)
    executor.start_polling(
        dp, on_startup=on_startup, skip_updates=config.SKIP_UPDATES
    )

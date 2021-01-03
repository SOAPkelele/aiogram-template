from aiogram import types


async def command_start_handler(msg: types.Message):
    await msg.answer('Hello')

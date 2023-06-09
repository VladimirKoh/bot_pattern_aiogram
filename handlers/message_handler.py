from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, bot, sql
from keyboards import inline, reply
from states import *


# @dp.message_handler()
# async def name(message: types.Message):


@dp.message_handler(commands=['start'])
async def command_start_process(message: types.Message):
    if not sql.exist_user(message.from_user.id):
        sql.add_user(message.from_user.id)
    await message.answer("Hello, world!")
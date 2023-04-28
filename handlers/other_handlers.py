from aiogram import Router

from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
# from lexicon.lexicon_ru import LEXICON

# Инициализируем роутер уровня модуля
router: Router = Router()

"""Для эхо бота modular_echo_bot"""
# # Этот хэндлер будет срабатывать на любые ваши сообщения,
# # кроме команд "/start" и "/help"
# @router.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text=LEXICON_RU['no_echo'])


""" Для бота камень ножницы бумага rock_paper_scissors_bot"""


#
#
# # Хэндлер для сообщений, которые не попали в другие хэндлеры
# @router.message()
# async def send_answer(message: Message):
#     await message.answer(text=LEXICON_RU['other_answer'])


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')

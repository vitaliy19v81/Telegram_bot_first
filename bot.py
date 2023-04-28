import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

from keyboards.set_menu import set_main_menu



#Инициализируем логгер
logger = logging.getLogger(__name__)  # Для бота камень ножницы бумага rock_paper_scissors_bot
                                        # Для бота Book

"""Для эхо бота modular_echo_bot"""
"""Для бота Book"""
# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

# Функция конфигурирования и запуска бота

"""Настраиваем кнопку Menu"""
# # Функция конфигурирования и запуска бота
# async def main():
#     # ...
#
#     # Инициализируем бот и диспетчер
#     bot: Bot = Bot(token=config.tg_bot.token,
#                    parse_mode='HTML')
#     dp: Dispatcher = Dispatcher()
#
#     # Настраиваем кнопку Menu
#     await set_main_menu(bot)
#
#     # ...


""" Для бота камень ножницы бумага rock_paper_scissors_bot"""
# async def main():
#     # Конфигурируем логирование
#     logging.basicConfig(
#         level=logging.INFO,
#         format='%(filename)s:%(lineno)d #%(levelname)-8s '
#                '[%(asctime)s] - %(name)s - %(message)s')
#
#     # Выводим в консоль информацию о начале запуска бота
#     logger.info('Starting bot')
#
#     # Загружаем конфиг в переменную config
#     config: Config = load_config()
#
#     # Инициализируем бот и диспетчер
#     bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
#     dp: Dispatcher = Dispatcher()
#
#     # Регистриуем роутеры в диспетчере
#     dp.include_router(user_handlers.router)
#     dp.include_router(other_handlers.router)
#
#     # Пропускаем накопившиеся апдейты и запускаем polling
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())


# from aiogram.filters import CommandStart
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
#
# # Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# # полученный у @BotFather
# API_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'
#
# # Создаем объекты бота и диспетчера
# bot: Bot = Bot(token=API_TOKEN)
# dp: Dispatcher = Dispatcher()

# # Создаем объекты инлайн-кнопок
# url_button_1: InlineKeyboardButton = InlineKeyboardButton(
#     text='Курс "Телеграм-боты на Python и AIOgram"',
#     url='https://stepik.org/120924')
# url_button_2: InlineKeyboardButton = InlineKeyboardButton(
#     text='Документация Telegram Bot API',
#     url='https://core.telegram.org/bots/api')
#
# # Создаем объект инлайн-клавиатуры
# keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
#     inline_keyboard=[[url_button_1],
#                      [url_button_2]])


# # Создаем объекты инлайн-кнопок
# group_name = 'aiogram_stepik_course'
# url_button_1: InlineKeyboardButton = InlineKeyboardButton(
#     text='Группа "Телеграм-боты на AIOgram"',
#     url=f'tg://resolve?domain={group_name}')
# user_id = 5846168637
# url_button_2: InlineKeyboardButton = InlineKeyboardButton(
#     text='Автор курса на Степике по телеграм-ботам',
#     url=f'tg://user?id={user_id}')
#
# channel_name = 'toBeAnMLspecialist'
# url_button_3: InlineKeyboardButton = InlineKeyboardButton(
#     text='Канал "Стать специалистом по машинному обучению"',
#     url=f'https://t.me/{channel_name}')
#
# # Создаем объект инлайн-клавиатуры
# keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
#     inline_keyboard=[[url_button_1],
#                      [url_button_2],
#                      [url_button_3]])


# # Создаем объекты инлайн-кнопок
# big_button_1: InlineKeyboardButton = InlineKeyboardButton(
#     text='БОЛЬШАЯ КНОПКА 1',
#     callback_data='big_button_1_pressed')
#
# big_button_2: InlineKeyboardButton = InlineKeyboardButton(
#     text='БОЛЬШАЯ КНОПКА 2',
#     callback_data='big_button_2_pressed')
#
# # Создаем объект инлайн-клавиатуры
# keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
#     inline_keyboard=[[big_button_1],
#                      [big_button_2]])
#
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру c url-кнопками
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Это инлайн-кнопки с параметром "url"',
#                          reply_markup=keyboard)
#
# from aiogram.filters import Text
# from aiogram.types import CallbackQuery

# # Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# # с data 'big_button_1_pressed' или 'big_button_2_pressed'
# @dp.callback_query(Text(text=['big_button_1_pressed',
#                               'big_button_2_pressed']))
# async def process_buttons_press(callback: CallbackQuery):
#     await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
# @dp.callback_query(Text(text=['big_button_1_pressed']))
# async def process_button_1_press(callback: CallbackQuery):
#     if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
#         await callback.message.edit_text(
#             text='Была нажата БОЛЬШАЯ КНОПКА 1',
#             reply_markup=callback.message.reply_markup)
#     await callback.answer()
#
#
# # Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# # с data 'big_button_2_pressed'
# @dp.callback_query(Text(text=['big_button_2_pressed']))
# async def process_button_2_press(callback: CallbackQuery):
#     if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
#         await callback.message.edit_text(
#             text='Была нажата БОЛЬШАЯ КНОПКА 2',
#             reply_markup=callback.message.reply_markup)
#     await callback.answer()
#
# if __name__ == '__main__':
#     dp.run_polling(bot)

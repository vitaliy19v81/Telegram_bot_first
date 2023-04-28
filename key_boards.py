from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# """1"""
# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)

# """2"""
# """
# 1   2   3   4   5   6   7
# """
# # Создаем список списков с кнопками
# keyboard: list[KeyboardButton] = [
#     KeyboardButton(text=str(i)) for i in range(1, 8)]
#
# # Инициализируем билдер
# builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
#
# builder.row(*keyboard)
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)

# """3"""
# """
# 1   2   3   4
# 5   6   7   8
#   9      10
# """
# # Создаем список списков с кнопками
# keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
#     text=str(i)) for i in range(1, 8)]]
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True)

# """4"""
# # Создаем список списков с кнопками
# keyboard: list[KeyboardButton] = [
#     KeyboardButton(text=str(i)) for i in range(1, 8)]
#
# # Инициализируем билдер
# builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
#
# # Добавляем кнопки в билдер
# builder.row(*keyboard, width=3)
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)

# """5"""
# """
# 1   2   3   4
# 5   6   7   8
#   9      10
# """
# #Создаем список списков с кнопками
# keyboard: list[list[KeyboardButton]] = [
#     [KeyboardButton(text=str(i)) for i in range(1, 4)],
#     [KeyboardButton(text=str(i)) for i in range(4, 7)],
#     [KeyboardButton(text=str(i)) for i in range(7, 9)]]
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True)

# """6"""
# Создаем список списков с кнопками
# keyboard: list[list[KeyboardButton]] = [
#     [KeyboardButton(text=str(i)) for i in range(1, 4)],
#     [KeyboardButton(text=str(i)) for i in range(4, 7)]]
#
# keyboard.append([KeyboardButton(text='7')])
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=my_keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
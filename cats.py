from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = ''

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


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура', reply_markup=my_keyboard)


# # Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
# button_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
# button_3: KeyboardButton = KeyboardButton(text='Кнопка 3')
# button_4: KeyboardButton = KeyboardButton(text='Кнопка 4')
# button_5: KeyboardButton = KeyboardButton(text='Кнопка 5')
# button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
# button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
# button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
# button_9: KeyboardButton = KeyboardButton(text='Кнопка 9')
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                         keyboard=[[button_1, button_2, button_3],
#                                   [button_4, button_5, button_6],
#                                   [button_7, button_8, button_9]],
#                         resize_keyboard=True)



# keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
#     text=f'Кнопка {j * 3 + i}') for i in range(1, 4)] for j in range(3)]
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     resize_keyboard=True)


# # Инициализируем билдер
# kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
#
# # Создаем список с кнопками
# buttons: list[KeyboardButton] = [KeyboardButton(
#                 text=f'Кнопка {i + 1}') for i in range(10)]
#
# # Распаковываем список с кнопками в билдер, указываем, что
# # в одном ряду должно быть 4 кнопки
# kb_builder.row(*buttons, width=4)
#
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Вот такая получается клавиатура',
#                          reply_markup=kb_builder.as_markup(
#                                             resize_keyboard=True))



# Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
# button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                     keyboard=[[button_1, button_2]],
#                                     resize_keyboard=True,
#                                     one_time_keyboard=True)
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Чего кошки боятся больше?',
#                          reply_markup=keyboard)
#
#
#
# # Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
# @dp.message(Text(text='Собак 🦮'))
# async def process_dog_answer(message: Message):
#     await message.answer(text='Да, несомненно, кошки боятся собак. '
#                               'Но вы видели как они боятся огурцов?')
#                          # reply_markup=ReplyKeyboardRemove())
#
#
#
# # Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
# @dp.message(Text(text='Огурцов 🥒'))
# async def process_cucumber_answer(message: Message):
#     await message.answer(text='Да, иногда кажется, что огурцов '
#                               'кошки боятся больше')
#                          # reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    dp.run_polling(bot)
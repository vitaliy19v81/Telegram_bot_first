import requests
import time

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Чтобы иметь возможность работать с картинками
from aiogram.types import ContentType
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# # Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(Command(commands=["start"]))
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
#
#
# # Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ '
#                          'я пришлю тебе твое сообщение')
#
#
# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)


# Этот хэндлер будет срабатывать на команду "/start"


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
#
#
# # Этот хэндлер будет срабатывать на команду "/help"
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ '
#                          'я пришлю тебе твое сообщение')
#
# # Этот хэндлер будет срабатывать на отправку боту фото
# async def send_photo_echo(message: Message):
#     print(message)
#     await message.reply_photo(message.photo[0].file_id)
#
#
# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# async def send_echo(message: Message):
#     await message.reply(text=message.text)
#
# # Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# dp.message.register(send_echo)


# def say_something(number: int, word: str) -> str:
#     word = word.capitalize()
#     return word * number
#
# def get_string(string: str, times: int, sep='') -> str:
#     return sep.join([string] * times)

# def api_response(api_url: str) -> None:
#     # api_url = 'http://api.open-notify.org/iss-now.json'
#     # api_url = 'http://numbersapi.com/43'
#     # api_url = 'https://random.dog/woof.json'
#     response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
#
#     if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#         print(response.text)
#     else:
#         print(response.status_code)  # При другом коде ответа выводим этот код
#
#
# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'
# TEXT: str = 'Ура! Классный апдейт!'
# MAX_COUNTER: int = 100
#
# offset: int = -2
# counter: int = 0
# chat_id: int


# API_URL: str = 'https://api.telegram.org/bot'
# API_CATS_URL: str = 'https://random.dog/woof.json'
# BOT_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'
# ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
#
# offset: int = -2
# counter: int = 0
# cat_response: requests.Response
# cat_link: str


# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = '6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs'
# offset: int = -2
# updates: dict


# def do_something() -> None:
#     print('Был апдейт')


if __name__ == '__main__':
    dp.run_polling(bot)
    # url = 'https://inshorts.deta.dev/news?category=science'
    # api_response(url)

# https://api.telegram.org/bot6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs/getUpdates
# https://api.telegram.org/bot6256912847:AAHx5kv-318zu-FjcnU_w1DkCsE7ZyaJlOs/sendMessage?chat_id=5846168637&text=Привет,%20Super_Jinius!
#     while counter < MAX_COUNTER:
#
#         print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
#
#         updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#         if updates['result']:
#             for result in updates['result']:
#                 offset = result['update_id']
#                 chat_id = result['message']['from']['id']
#                 # TEXT = result['message']['text'] # Получаем текст от пользователя
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
#
#         time.sleep(1)
#         counter += 1


# while counter < 100:
#     print('attempt =', counter)
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#
#     time.sleep(1)
#     counter += 1

    # while True:
    #     start_time = time.time()
    #     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    #
    #     if updates['result']:
    #         for result in updates['result']:
    #             offset = result['update_id']
    #             do_something()
    #
    #     time.sleep(3)
    #     end_time = time.time()
    #     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
# Эхо бот (сообщения которые ты отпаравляешь в бота, приходят тебе от него)
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

with open('ideas_for_bot.txt') as file:
    bot_token: str = ''.join(list(file.readline())[-47:]).strip()

api_url: str = 'https://api.telegram.org/bot'

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


# Этот хендлер будет срабатывать на команду /start
async def process_start(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот.\nЧто я делаю, можешь посмотреть, нажав на команду /help')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help(message: Message):
    await message.answer('Инструкция: то, что ты мне отправишь, я отправлю тебе)))')


# Этот хендлер будет срабатывать на отправку все твои сообщения
async def send_any_message(message: Message):
    print(f'{message.chat}\n')
    try:
        await message.send_copy(message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается методом send_copy')

dp.message.register(process_start, Command(commands=['start']))
dp.message.register(process_help, Command(commands=['help']))
dp.message.register(send_any_message, dp.message)

if __name__ == '__main__':
    dp.run_polling(bot)


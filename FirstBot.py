# Эхо бот (сообщения которые ты отпаравляешь в бота, приходят тебе от него)
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

with open('ideas_for_bot.txt') as file:
    bot_token: str = ''.join(list(file.readline())[-47:]).strip()

bot: Bot = Bot(token=bot_token)
dispat: Dispatcher = Dispatcher()

# Этот хендлер будет срабатывать на команду /start
@dispat.message(Command(commands=['start']))
async def process_start(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот.\nЧто я делаю, можешь посмотреть, нажав на команду /help')


# Этот хэндлер будет срабатывать на команду "/help"
@dispat.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer('Инструкция: то, что ты мне отправишь, я отправлю тебе)))')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dispat.message()
async def send_message(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dispat.run_polling(bot)

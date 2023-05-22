# Эхо бот (сообщения которые ты отпаравляешь в бота, приходят тебе от него)
from aiogram import Bot, Dispatcher, F
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


# Этот хендлер будет срабатывать на отправку боту фото
async def send_photo(message: Message):
    print(message.photo)
    await message.reply_photo(message.photo[0].file_id)


# Этот хендлер будет срабатывать на отправку боту аудио
async def send_audio(message: Message):
    await message.reply_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_text(message: Message):
    await message.reply(text=message.text)


dp.message.register(process_start, Command(commands=['start']))
dp.message.register(process_help, Command(commands=['help']))
dp.message.register(send_photo, F.photo)
dp.message.register(send_audio, F.voice)
dp.message.register(send_text)

if __name__ == '__main__':
    dp.run_polling(bot)


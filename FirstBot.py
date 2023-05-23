# Бот для игры "Угадай число"
from random import randint
from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command, Text

ATTEMPTS: int = 7
user_stat: dict = {}

with open('ideas_for_bot.txt') as file:
    bot_token: str = file.readline().strip()

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


def generate_num() -> int:
    return randint(1, 100)


@dp.message(Command(commands=['start']))
async def hello_mess(message: Message):
    await message.answer('Привет! Я - FirstBot, хочу сыграть с тобой в игру: "Угадай число". Для ознакомления правил'
                         ' нажми команду /help')
    user_stat.setdefault(message.from_user.id, {'in_game': False,
     'secret_number': None,
     'attempts': None,
     'all_games': 0,
     'wins': 0})


@dp.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


@dp.message(Command(commands=['stat']))
async def stat_show(message: Message):
    await message.answer('Всего игр сыграно: {0}\nВсего выиграно: {1}'.format(
                        user_stat[message.from_user.id]['all_games'],
                        user_stat[message.from_user.id]['wins']))


@dp.message(Command(commands=['cancel']))
async def process_cancel(message: Message):
    if user_stat[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
        user_stat[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. Может, сыграем разок?')


@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть'], ignore_case=True))
async def application_agreement(message: Message):
    if not user_stat[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user_stat[message.from_user.id]['in_game'] = True
        user_stat[message.from_user.id]['secret_number'] = generate_num()
        user_stat[message.from_user.id]['attempts'] = ATTEMPTS
        user_stat[message.from_user.id]['all_games'] += 1
    else:
        await message.answer('Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и '
                             'команды /cancel и /stat')


@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def refusal_offer(message: Message):
    if user_stat[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
        user_stat[message.from_user.id]['in_game'] = False
    else:
        await message.answer('Мы же сейчас с вами итак не играем')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_game(message: Message):
    if user_stat[message.from_user.id]['in_game']:
        if user_stat[message.from_user.id]['attempts'] > 1:
            if int(message.text) > user_stat[message.from_user.id]['secret_number']:
                await message.answer('Мое число меньше')
                user_stat[message.from_user.id]['attempts'] -= 1
            elif int(message.text) < user_stat[message.from_user.id]['secret_number']:
                await message.answer('Мое число больше')
                user_stat[message.from_user.id]['attempts'] -= 1
            elif int(message.text) == user_stat[message.from_user.id]['secret_number']:
                await message.answer('Ура!!! Вы угадали число!\n\nМожет, сыграем еще?')
                user_stat[message.from_user.id]['in_game'] = False
                user_stat[message.from_user.id]['wins'] += 1
        else:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user_stat[message.from_user.id]["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            user_stat[message.from_user.id]['in_game'] = False
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


@dp.message()
async def other_words(message: Message):
    if user_stat[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте просто сыграем в игру?')


if __name__ == '__main__':
    dp.run_polling(bot)

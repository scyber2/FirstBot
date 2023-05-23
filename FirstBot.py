from aiogram.filters import BaseFilter, Text
from aiogram import Dispatcher, Bot
from aiogram.types import Message

with open('ideas_for_bot.txt') as file:
    bot_token: str = file.readline().strip()

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


class FindNumbers(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers: list[int] = []
        print(message.text)
        for word in message.text.split():
            word = word.replace(',', '').replace('.', '')
            if word.isdigit():
                numbers.append(int(word))
        print(numbers)
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(Text(startswith='найди числа', ignore_case=True), FindNumbers())
async def process_have_numbers(message: Message, numbers: list[int]):
    await message.answer(f'Нашёл: {", ".join(str(i) for i in numbers)}')


@dp.message()
async def process_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')


if __name__ == '__main__':
    dp.run_polling(bot)

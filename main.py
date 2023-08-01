from aiogram import Bot, Dispatcher, executor, types
import config
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# статичні змінні
bot = Bot(token=config.token)
dp = Dispatcher(bot)

random_q = KeyboardButton('Рандомне питання')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(random_q)

# /start


@dp.message_handler(commands="start")
async def hi(m: types.Message):
    sti = open(".//images//8ball.gif", "rb")
    await bot.send_document(m.chat.id, sti, caption=f"Салам, {m.from_user.first_name}! Я - Magic 8 ball", reply_markup = greet_kb)
    sti.close()


list_of_answers = [
    # Положительні ответи
    "● Звісно, що так.",
    "● Це розумно.",
    "● Без сумніву.",
    "● Так, однозначно.",
    "● Ви можете на це покластися.",
    "● З моєї точки зору - так.",
    "● Можливо.",
    "● Все виглядає добре.",
    "● Так.",
    "● Знаки вказують на те що це гарна ідея.",

    # ну такоє

    "● Відповідь неоднозначна, спробуйте ще раз.",
    "● Запитайте пізніше.",
    "● Краще зараз не говорити.",
    "● Неможливо передбачити майбутьнє.",
    "● Сконцентруйтеся і спитайте знову.",

    # хренові ответи

    "● Не розраховуйте на це.",
    "● Моя відповідь - ні.",
    "● Мої джерела кажуть - ні.",
    "● Виглядає не дуже добре.",
    "● Дуже сумнівно."
]


@dp.message_handler(content_types="text")
async def send_answer(m: types.Message):
    ans = random.randrange(-1, len(list_of_answers))
    await m.answer(f'Моя відповідь: {list_of_answers[ans]}')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

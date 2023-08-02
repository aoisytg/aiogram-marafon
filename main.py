from aiogram import Bot, Dispatcher, executor, types
import config
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import openai

openai.api_key = config.gpt_api

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5, button6)

list_of_answers = [
    # Позитивні відповіді
    "● Звісно, що так.",
    "● Це розумно.",
    "● Без сумніву.",
    "● Так, однозначно.",
    "● Ви можете на це покластися.",
    "● З моєї точки зору - так.",
    "● Можливо.",
    "● Все виглядає добре.",
    "● Так.",
    "● Знаки вказують на те, що це гарна ідея.",

    # Нейтральні відповіді
    "● Відповідь неоднозначна, спробуйте ще раз.",
    "● Запитайте пізніше.",
    "● Краще зараз не говорити.",
    "● Неможливо передбачити майбутнє.",
    "● Сконцентруйтеся і спитайте знову.",

    # Негативні відповіді
    "● Не розраховуйте на це.",
    "● Моя відповідь - ні.",
    "● Мої джерела кажуть - ні.",
    "● Виглядає не дуже добре.",
    "● Дуже сумнівно."
]

# Статичні змінні
bot = Bot(token=config.token)
dp = Dispatcher(bot)

# Створення InlineKeyboardMarkup
inline_btn_1 = InlineKeyboardButton('Рандомне питання', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# Обробка команди /start
@dp.message_handler(commands=['start'])
async def hi(m: types.Message):
    with open(".//images//8ball.gif", "rb") as sti:
        await bot.send_document(m.chat.id, sti, caption=f"Салам, {m.from_user.first_name}! Я - Magic 8 ball", reply_markup=markup5)

# Обробка текстових повідомлень
@dp.message_handler(content_types="text")
async def send_answer(m: types.Message):
    ans = random.choice(list_of_answers)
    await m.answer(f'Моя відповідь: {ans}')

# Обробка натискання кнопки
site_list = ["https://leetcode.com", "https://sololearn.com", "https://zelenka.guru/"]
rsite = random.choice(site_list)

@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Рандомний сайт : {rsite}")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

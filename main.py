from aiogram import Bot, Dispatcher, executor, types
import config
import random
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Статичні змінні
bot = Bot(token=config.token)
dp = Dispatcher(bot)

inline_btn_1 = InlineKeyboardButton('Рандомне питання', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# Обробка команди /start
@dp.message_handler(commands="start")
async def hi(m: types.Message):
    sti = open(".//images//8ball.gif", "rb")
    await bot.send_document(m.chat.id, sti, caption=f"Салам, {m.from_user.first_name}! Я - Magic 8 ball", reply_markup=inline_kb1)
    sti.close()

# Варіанти відповідей
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

# Обробка текстових повідомлень
@dp.message_handler(content_types="text")
async def send_answer(m: types.Message):
    ans = random.randrange(-1, len(list_of_answers))
    await m.answer(f'Моя відповідь: {list_of_answers[ans]}')

# Обробка натискання кнопки
@dp.callback_query_handler(func=lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Рандомне повідомлення')

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

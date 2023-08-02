import openai
import config

openai.api_key = config.gpt_api

response = openai.Completion.create(
    engine="text-davinci-002",  # Використання моделі GPT-3.5
    prompt="Привіт, я - ваш новий бот. Питайте мене що завгодно!",
    temperature=0.7,  # Температура для збільшення різноманітності відповідей
    max_tokens=100,  # Максимальна довжина відповіді
)

print (response)
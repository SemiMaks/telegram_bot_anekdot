import random

import requests
import telebot
from bs4 import BeautifulSoup as bs

from configure import config

token = config.get('token')
URL = 'https://www.anekdot.ru/last/good/'


def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы узнать новый анекдот - введите "да" и чтобы продолжить - "ещё"')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in 'даещёеще':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Друг, как хочешь!')
bot.polling()
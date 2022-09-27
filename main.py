import requests
import random
import telebot
from bs4 import BeautifulSoup as bs
from configure import config
token = config.get('token')
# print(token)
URL = 'https://www.anekdot.ru/last/good/'

def parser(url):
    r = requests.get(url)
    # print(r.status_code)
    # print(r.text)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
print(list_of_jokes)

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Прочитать новый анекдот введи число от 1 до 9')

bot.polling()
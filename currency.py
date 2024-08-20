import requests
from bs4 import BeautifulSoup as Bs
import telebot
from telebot import types


def get_usd():
    r = requests.get(url = 'https://www.optimabank.kg/index.php?option=com_nbrates&view=default&Itemid=196&lang=ru')
    soup = Bs(r.text,'html.parser')
    rate_buy = soup.find('div',class_='iso-USD row0').find('div',class_='rate buy').get_text(strip=True)
    rate_sell=soup.find('div',class_='iso-USD row0').find('div',class_='rate sell').get_text(strip=True)
    return rate_buy,rate_sell

dollar = get_usd()



def get_euro():
    r = requests.get(url = 'https://www.optimabank.kg/index.php?option=com_nbrates&view=default&Itemid=196&lang=ru')
    soup = Bs(r.text,'html.parser')
    rate_buy = soup.find('div',class_='iso-EUR row1').find('div',class_='rate buy').get_text(strip=True)
    rate_sell=soup.find('div',class_='iso-EUR row1').find('div',class_='rate sell').get_text(strip=True)
    return rate_buy,rate_sell

euro = get_euro()
print(euro)


bot = telebot.TeleBot('7541406043:AAGIPQoHbAtIxRHQ-ZOvzJJk3dA-dNHdSds')

@bot.message_handler(commands=['start'])

def first(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row('USD-курс','EURO-курс')
    bot.send_message(message.chat.id,"Добро пожаловать в обмен валют ",reply_markup=menu)

@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'USD-курс':
        bot.send_message(message.chat.id,f"покупка {dollar[0]}\tпродажа {dollar[1]}")
    elif message.text == 'EURO-курс':
        bot.send_message(message.chat.id,f"покупка {euro[0]}\tпродажа {euro[1]}")

bot.polling(non_stop=True)
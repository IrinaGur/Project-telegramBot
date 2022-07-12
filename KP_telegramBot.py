import telebot
import random
from telebot import types

# Создаем и загружаем список скороговорок
f = open('ckorog.txt', 'r', encoding='UTF-8')
ckorogs = f.read().split('\n')
f.close()
# Создаем и загружаем список поговорок
f = open('pogovor.txt', 'r', encoding='UTF-8')
pogovors = f.read().split('\n')
f.close()
#импортируем библиотеку и подключаем токен бота:
bot = telebot.TeleBot('токен')

# Создаем и ослеживаем команду start
@bot.message_handler(commands=['start'])
def start(massage, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bn1 = types.KeyboardButton('Скороговорка')
    bn2 = types.KeyboardButton('Поговорка')
    markup.add(bn1)
    markup.add(bn2)
    bot.send_message(massage.chat.id,
                     'Нажми: \nСкороговорка для получения интересных фраз\n'
                     'Поговорка — для получения мудрой цитаты ',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"]) #отслеживаем текст
def handle_text(message):
    if message.text.strip() == 'Скороговорка':
        gov = random.choice(ckorogs)
    elif message.text.strip() == 'Поговорка':
        gov = random.choice(pogovors)
    bot.send_message(message.chat.id, gov)

# Запускаем бота
bot.polling(none_stop=True)

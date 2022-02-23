import telebot
from telebot import types
token = "5189752154:AAGEMOrb8dd8E5PHPZa87xK5Aao3I9b_1NE"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('/post', "/help","/wiki","/cat")
    bot.send_message(message.chat.id, 'Здарова работяга', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '/post - почта, /wiki - википедия, /cat - статья про кошку')

@bot.message_handler(commands=['wiki'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://ru.wikipedia.org')

@bot.message_handler(commands=['cat'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0')

@bot.message_handler(commands=['post'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mail.ru/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "когда стрим?":
        bot.send_message(message.chat.id, 'Завтра')
    if message.text.lower() == "папич, ты умный?":
        bot.send_message(message.chat.id, 'в игре или в жизни?')
    if message.text.lower() == "вернись в доту":
        bot.send_message(message.chat.id, 'Никогда')

    #if (message.text.lower() == "ну пожалуйста" and k==1):
        #bot.send_message(message.chat.id, 'За 1000000$')
 
    if message.text.lower() == "хочу задонатить":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://www.donationalerts.com/r/evilarthas')
bot.polling(none_stop=True)
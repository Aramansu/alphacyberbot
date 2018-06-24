import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
task = Task()

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Я квест-бот с Альфы')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Что тебе нужно?')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Этим ничего не добиться')
    elif text == "кто ты?":
        bot.send_message(chat_id, '00110010010101010010010010101')
    else:
        bot.send_message(chat_id, 'Error')

bot.polling()
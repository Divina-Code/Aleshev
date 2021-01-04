import telebot
bot = telebot.TeleBot('1444835305:AAHl385csjfmIQE8XFqrwcZSnfexfeYjcLw')
@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])
bot.polling()
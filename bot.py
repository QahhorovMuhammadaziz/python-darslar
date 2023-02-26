import telebot


bot = telebot.TeleBot('6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk')


@bot.message_handler(commands=['start'])
def start(message):
    photos = bot.get_user_profile_photos(message.chat.id)
    bot.send_photo(message.chat.id,photos.photos[0][0].file_id)
    
    
bot.polling()
     
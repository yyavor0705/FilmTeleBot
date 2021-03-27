from telebot import TeleBot, types

from films import Films

bot = TeleBot('1436742624:AAE9pneqqE0DW8PUe8QRrlsNnNvNBKq7AqA')
films = Films()
films.load_all_films()


@bot.message_handler(commands=['start', 'categories'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    for category in films.categories:
        callback_button = types.InlineKeyboardButton(text=category, callback_data=category)
        keyboard.add(callback_button)
    bot.send_message(message.chat.id, 'Select film category:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    category = call.data
    categorized_films = films.get_films_by_category(category)
    for film in categorized_films:
        bot.send_photo(call.message.chat.id, film.img, caption=film.title)


if __name__ == "__main__":
    bot.polling()

'''
РАЗМЕТКА ДЛЯ НАС

короче # это коменты

⁡⁢⁣⁢красным⁡ помечается для друг друга че сделать надо на чем остановились

прост коменты, обычным цветом это объясняю че за че отвечает или че делат
чтобы Вова с Макаром быстрее втянулись
'''
# telebot и types нужны для работы с Telegram-ботом
#pathlib нужен для работы с путями к файлам
from pathlib import Path

import telebot
from telebot import types

TOKEN = (Path(__file__).parent / "bot_API.txt").read_text(encoding="utf-8").strip() #токен получаем из файла bot_API.txt
if not TOKEN:
    raise RuntimeError("API пока не получен")

bot = telebot.TeleBot(TOKEN) # токен/айпи от нашего бота. код отрабатывает именно тот бот, токен которого тут
bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Начать"))

    bot.send_message(
        message.chat.id,
        "Выбери действие:",
        reply_markup=keyboard,
    )

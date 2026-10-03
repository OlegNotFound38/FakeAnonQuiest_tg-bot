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


@bot.message_handler(commands=["start"])
def start(message):
    start_menu_keyboard = types.InlineKeyboardMarkup()
    start_menu_keyboard.add(
        types.InlineKeyboardMarkup(
            "Получить личную ссылку"
        )
    )
    
    bot.send_message(
        message.chat.id,
        """Добро пожаловать в бота👋
        С его помощью вы можете:
        Получить анонимные сообщения 📥
        Отправлять их пользователям зареганым в боте 📤
        Задать любой вопрос в поддержку. Постараемся ответить как можно быстрее ❓
        
        К сожелению это пока весь функционал бота, но мы планируем расширяться, и будем рады новым идеям улучшения сервиса 🤝
        
        Функционал Бота находится ниже, приятного использования 🤗"""#,
        #reply_markup = start_menu_keyboard
        )


bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался
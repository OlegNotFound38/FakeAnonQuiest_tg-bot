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
    start_menu_keyboard = types.InlineKeyboardMarkup(row_width = 1)
    start_menu_keyboard.add(
        types.InlineKeyboardButton(
            "Получить личную ссылку 🔗",
            callback_data = "get_link"
        ),
        types.InlineKeyboardButton(
            "Отправить пользователю соробщение 📬",
            callback_data = "send_message"
        ),
        types.InlineKeyboardButton(
            "Написать в поддержку ❓",
            callback_data = "support"
        )
    )
        
    bot.send_message(
        message.chat.id, # ⁡⁢⁣⁢Kelfy, закинь в ГПТшник, спроси как пофиксить проблему. А, ну и попроси мения переслать че выводит бот, а то ты не в курсах⁡
        """Добро пожаловать в бота👋 # 
        С его помощью вы можете:
        Получить анонимные сообщения 📥
        Отправлять их пользователям зареганым в боте 📤
        Задать любой вопрос в поддержку. Постараемся ответить как можно быстрее ❓
        
        К сожелению это пока весь функционал бота, но мы планируем расширяться, и будем рады новым идеям улучшения сервиса 🤝
        
        Функционал Бота находится ниже, приятного использования 🤗""",
        reply_markup = start_menu_keyboard
        )
    
@bot.callback_query_handler(func=lambda call: True) # Большой обработчик всех инлайн-кнопок в боте
def buttons(call):
# ОСНОВНОЕ МЕНЮ
    if call.data == "get_link":
        start(call.message)
    if call.data == "send_message":
        start(call.message)
    if call.data == "support":
        start(call.message)

bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался
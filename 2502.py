import os
import datetime
import telebot
import json

TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TOKEN)

user_data = {}
DATA_FILE = 'sleep_data.json'


def load_data():
    global user_data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
    else:
        user_data = {}


def save_data():
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)


def init_user_data(user_id):
    if user_id not in user_data:
        user_data[user_id] = {
            'start_time': None,
            'end_time': None,
            'duration': None,
            'quality': None,
            'notes': None
        }


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Используй /sleep для начала отслеживания сна и /wake для окончания.')


@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = str(message.from_user.id)  # Используем строку для совместимости с JSON
    init_user_data(user_id)
    user_data[user_id]['start_time'] = datetime.datetime.now().isoformat()
    save_data()  # Сохраняем данные
    bot.reply_to(message, 'Вы отошли ко сну.')


@bot.message_handler(commands=['wake'])
def wake(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data or user_data[user_id]['start_time'] is None:
        bot.reply_to(message, 'Сначала укажите, что вы начали спать с помощью команды /sleep.')
        return

    start_time = datetime.datetime.fromisoformat(user_data[user_id]['start_time'])
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds() / 3600
    user_data[user_id]['end_time'] = end_time.isoformat()
    user_data[user_id]['duration'] = duration
    save_data()  # Сохраняем данные

    bot.reply_to(message, f'Вы проснулись! Продолжительность сна: {duration:.2f} часа.')


@bot.message_handler(commands=['set_quality'])
def set_quality(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data or user_data[user_id]['duration'] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    try:
        quality = int(message.text.split()[1])
        if 1 <= quality <= 10:
            user_data[user_id]['quality'] = quality
            save_data()  # Сохраняем данные
            bot.reply_to(message, f'Качество сна установлено на {quality}.')
        else:
            bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')


@bot.message_handler(commands=['set_notes'])
def set_notes(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data or user_data[user_id]['duration'] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    notes = ' '.join(message.text.split()[1:])
    user_data[user_id]['notes'] = notes
    save_data()  # Сохраняем данные
    bot.reply_to(message, 'Заметка добавлена.')


if __name__ == '__main__':
    load_data()  # Загружаем данные при старте
    bot.polling()


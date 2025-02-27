import os
import datetime
import telebot
import json

TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TOKEN)
DATA_FILE = 'sleep_data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}


def save_data(user_data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)


def init_user_data(user_id):
    user_data = load_data()
    if user_id not in user_data:
        user_data[user_id] = []
    return user_data


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Используй /sleep для начала отслеживания сна и /wake для окончания.')


@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = str(message.from_user.id)
    user_data = init_user_data(user_id)
    sleep_record = {
        'start_time': datetime.datetime.now().isoformat(),
        'end_time': None,
        'duration': None,
        'quality': None,
        'notes': None
    }
    user_data[user_id].append(sleep_record)
    save_data(user_data)
    bot.reply_to(message, 'Вы отошли ко сну.')


@bot.message_handler(commands=['wake'])
def wake(message):
    user_id = str(message.from_user.id)
    user_data = load_data()

    if user_id not in user_data or not user_data[user_id]:
        bot.reply_to(message, 'Сначала укажите, что вы начали спать с помощью команды /sleep.')
        return

    last_sleep_record = user_data[user_id][-1]
    if last_sleep_record['end_time'] is not None:
        bot.reply_to(message, 'Вы уже проснулись. Зафиксируйте новый сон, используя команду /sleep.')
        return

    start_time = datetime.datetime.fromisoformat(last_sleep_record['start_time'])
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds() / 3600
    last_sleep_record['end_time'] = end_time.isoformat()
    last_sleep_record['duration'] = duration
    save_data(user_data)

    bot.reply_to(message, f'Вы проснулись! Продолжительность сна: {duration:.2f} часа.')


@bot.message_handler(commands=['set_quality'])
def set_quality(message):
    user_id = str(message.from_user.id)
    user_data = load_data()

    if user_id not in user_data or not user_data[user_id]:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    last_sleep_record = user_data[user_id][-1]
    if last_sleep_record['duration'] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    try:
        quality = int(message.text.split()[1])
        if 1 <= quality <= 10:
            last_sleep_record['quality'] = quality
            save_data(user_data)
            bot.reply_to(message, f'Качество сна установлено на {quality}.')
        else:
            bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')


@bot.message_handler(commands=['set_notes'])
def set_notes(message):
    user_id = str(message.from_user.id)
    user_data = load_data()

    if user_id not in user_data or not user_data[user_id]:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    last_sleep_record = user_data[user_id][-1]
    if last_sleep_record['duration'] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    notes = ' '.join(message.text.split()[1:])
    last_sleep_record['notes'] = notes
    save_data(user_data)
    bot.reply_to(message, 'Заметка добавлена.')


if __name__ == '__main__':
    bot.polling()


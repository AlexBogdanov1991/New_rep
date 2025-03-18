import os
import datetime
import telebot
import sqlite3

TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TOKEN)
DATABASE_file = 'sleep_data.db'

def init_database():
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sleeping_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            start_time TEXT,
            end_time TEXT,
            quality INTEGER,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_last_sleep_record(user_id):
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? AND end_time IS NULL', (user_id,))
    record = cursor.fetchone()
    conn.close()
    return record

def record_exists(user_id):
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()
    cursor.execute('SELECT EXISTS(SELECT 1 FROM sleeping_records WHERE user_id = ? AND end_time IS NULL)', (user_id,))
    exists = cursor.fetchone()[0]
    conn.close()
    return exists

def update_record(record_id, **kwargs):
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()
    for key, value in kwargs.items():
        cursor.execute(f'UPDATE sleeping_records SET {key} = ? WHERE id = ?', (value, record_id))
    conn.commit()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Используй /sleep для начала отслеживания сна и /wake для окончания.')

@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = message.from_user.id
    if record_exists(user_id):
        bot.reply_to(message, 'Вы уже отмечали время сна. Сначала завершите его с помощью команды /wake.')
        return

    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sleeping_records (user_id, start_time) VALUES (?, ?)',
                   (user_id, datetime.datetime.now().isoformat()))
    conn.commit()
    conn.close()

    bot.reply_to(message, 'Вы отошли ко сну.')

@bot.message_handler(commands=['wake'])
def wake(message):
    user_id = message.from_user.id
    last_sleep_record = get_last_sleep_record(user_id)

    if last_sleep_record is None:
        bot.reply_to(message, 'Сначала укажите, что вы начали спать с помощью команды /sleep.')
        return

    start_time = datetime.datetime.fromisoformat(last_sleep_record[2])
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds() / 3600

    update_record(last_sleep_record[0], end_time=end_time.isoformat())

    bot.reply_to(message, f'Вы проснулись! Продолжительность сна: {duration:.2f} часа.')

@bot.message_handler(commands=['set_quality'])
def set_quality(message):
    user_id = message.from_user.id
    last_sleep_record = get_last_sleep_record(user_id)

    if last_sleep_record is None or last_sleep_record[3] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    try:
        quality = int(message.text.split()[1])
        if 1 <= quality <= 10:
            update_record(last_sleep_record[0], quality=quality)
            bot.reply_to(message, f'Качество сна установлено на {quality}.')
        else:
            bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10 в формате: /set_quality <1-10>.')

@bot.message_handler(commands=['set_notes'])
def set_notes(message):
    user_id = message.from_user.id
    last_sleep_record = get_last_sleep_record(user_id)

    if last_sleep_record is None or last_sleep_record[3] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        return

    notes = ' '.join(message.text.split()[1:])
    update_record(last_sleep_record[0], notes=notes)
    bot.reply_to(message, 'Заметка добавлена.')

@bot.message_handler(commands=['status'])


def status(message):
    user_id = message.from_user.id
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? ORDER BY id DESC LIMIT 1', (user_id,))
    last_sleep_record = cursor.fetchone()

    if last_sleep_record is None:
        bot.reply_to(message, 'Не найдены записи о сне. Начните с /sleep.')
        conn.close()
        return

    start_time = datetime.datetime.fromisoformat(last_sleep_record[2])
    end_time = datetime.datetime.fromisoformat(last_sleep_record[3]) if last_sleep_record[3] else None
    duration = (end_time - start_time).total_seconds() / 3600 if end_time else None
    quality = last_sleep_record[4]
    notes = last_sleep_record[5]

    quality_message = f'Качество сна: {quality}/10' if quality is not None else 'Качество сна не установлено.'
    notes_message = f'Заметки: {notes}' if notes else 'Заметок нет.'

    bot.reply_to(message, f'Ваша последняя запись о сне:\n'
                          f'Продолжительность: {duration:.2f} часа\n'
                          f'{quality_message}\n'
                          f'{notes_message}')

init_database()
bot.polling(none_stop=True)


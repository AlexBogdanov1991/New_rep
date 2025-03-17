
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
            user_id TEXT,
            start_time TEXT,
            end_time TEXT,
            duration REAL,
            quality INTEGER,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Используй /sleep для начала отслеживания сна и /wake для окончания.')

@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = str(message.from_user.id)
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? AND end_time IS NULL', (user_id,))
    if cursor.fetchone() is not None:
        bot.reply_to(message, 'Вы уже отмечали время сна. Сначала завершите его с помощью команды /wake.')
        conn.close()
        return

    cursor.execute('INSERT INTO sleeping_records (user_id, start_time) VALUES (?, ?)',
                   (user_id, datetime.datetime.now().isoformat()))
    conn.commit()
    conn.close()

    bot.reply_to(message, 'Вы отошли ко сну.')

@bot.message_handler(commands=['wake'])
def wake(message):
    user_id = str(message.from_user.id)
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? AND end_time IS NULL', (user_id,))
    last_sleep_record = cursor.fetchone()

    if last_sleep_record is None:
        bot.reply_to(message, 'Сначала укажите, что вы начали спать с помощью команды /sleep.')
        conn.close()
        return

    start_time = datetime.datetime.fromisoformat(last_sleep_record[2])
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds() / 3600

    cursor.execute('UPDATE sleeping_records SET end_time = ?, duration = ? WHERE id = ?',
                   (end_time.isoformat(), duration, last_sleep_record[0]))
    conn.commit()
    conn.close()

    bot.reply_to(message, f'Вы проснулись! Продолжительность сна: {duration:.2f} часа.')

@bot.message_handler(commands=['set_quality'])
def set_quality(message):
    user_id = str(message.from_user.id)
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? AND end_time IS NULL', (user_id,))
    last_sleep_record = cursor.fetchone()

    if last_sleep_record is None or last_sleep_record[4] is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        conn.close()
        return

    try:
        quality = int(message.text.split()[1])
        if 1 <= quality <= 10:
            cursor.execute('UPDATE sleeping_records SET quality = ? WHERE id = ?', (quality, last_sleep_record[0]))
            conn.commit()
            bot.reply_to(message, f'Качество сна установлено на {quality}.')
        else:
            bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, введите качество сна от 1 до 10 в формате: /set_quality <1-10>.')

@bot.message_handler(commands=['set_notes'])
def set_notes(message):
    user_id = str(message.from_user.id)
    conn = sqlite3.connect(DATABASE_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? AND end_time IS NULL', (user_id,))
    last_sleep_record = cursor.fetchone()

    if last_sleep_record is None:
        bot.reply_to(message, 'Сначала укажите время пробуждения с помощью команды /wake.')
        conn.close()
        return

    notes = message.text.split(maxsplit=1)
    if len(notes) < 2:
        bot.reply_to(message, 'Пожалуйста, введите заметки в формате: /set_notes <ваши заметки>.')
    else:
        cursor.execute('UPDATE sleeping_records SET notes = ? WHERE id = ?', (notes[1], last_sleep_record[0]))
        conn.commit()
        bot.reply_to(message, 'Заметки успешно добавлены.')

    conn.close()

init_database()
bot.polling()



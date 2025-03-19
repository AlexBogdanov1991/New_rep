import os
import datetime
import sqlite3
import telebot

TOKEN = os.getenv('TG_TOKEN')
DATABASE_FILE = 'sleep_data.db'
ALLOWED_FIELDS = {'end_time', 'quality', 'notes'}

bot = telebot.TeleBot(TOKEN)

def init_database():

    conn = sqlite3.connect(DATABASE_FILE)
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

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? ORDER BY id DESC LIMIT 1', (user_id,))
    record = cursor.fetchone()
    conn.close()
    return record

def record_exists(user_id):

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT EXISTS(SELECT 1 FROM sleeping_records WHERE user_id = ? AND end_time IS NULL)', (user_id,))
    exists = cursor.fetchone()[0]
    conn.close()
    return exists

def update_record(record_id, **kwargs):

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    for key, value in kwargs.items():
        if key in ALLOWED_FIELDS:
            cursor.execute(f'UPDATE sleeping_records SET {key} = ? WHERE id = ?', (value, record_id))
        else:
            print(f"Недопустимое поле: {key}")
    conn.commit()
    conn.close()

def get_last_five_records(user_id):

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sleeping_records WHERE user_id = ? ORDER BY id DESC LIMIT 5', (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(message, 'Привет! Используй /sleep для начала отслеживания сна и /wake для окончания.')

@bot.message_handler(commands=['sleep'])
def sleep(message):

    user_id = message.from_user.id
    if record_exists(user_id):
        bot.reply_to(message, 'Вы уже отмечали время сна. Сначала завершите его с помощью команды /wake.')
        return

    conn = sqlite3.connect(DATABASE_FILE)
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

    bot.reply_to(message, 'Пожалуйста, введите качество сна (1-10):')
    bot.register_next_step_handler(message, process_quality)

def process_quality(message):

    user_id = message.from_user.id
    last_sleep_record = get_last_sleep_record(user_id)

    try:
        quality = int(message.text)
        if quality < 1 or quality > 10:
            raise ValueError("Качество должно быть в диапазоне от 1 до 10.")
        update_record(last_sleep_record[0], quality=quality)
        bot.reply_to(message, 'Качество сна успешно обновлено!')
    except ValueError as e:
        bot.reply_to(message, f'Ошибка: {e}. Пожалуйста, введите число от 1 до 10.')

if __name__ == '__main__':
    init_database()
    bot.polling()


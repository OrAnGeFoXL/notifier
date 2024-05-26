import sqlite3 as sq


async def write_notify_to_sqlite(state, message):

    data = await state.get_data()
    text = data.get("text")
    time = data.get("time")
    repeat = data.get("repeat")
    repeat_frq = data.get("repeat_frq")
    task = data.get("task")
    
    user_id = message.from_user.id   

    with sq.connect('data/user_data.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS notify_data
                            (user_id INTEGER, text TEXT, time TEXT, repeat TEXT, repeat_frq TEXT, task TEXT)''')

        cursor.execute('''INSERT INTO notify_data (user_id, text, time, repeat, repeat_frq, task)
                            VALUES (?, ?, ?, ?, ?, ?)''', (user_id, text, time, repeat, repeat_frq, task))

        conn.commit()

async def get_notifications(user_id):

    with sq.connect('data/user_data.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT text, time, repeat, repeat_frq, task FROM notify_data WHERE user_id = ?', (user_id,))
        notifications = cursor.fetchall()

    return notifications

async def write_task_to_sqlite(state, message):

   
    with sq.connect('data/user_data.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS task_data
                            (user_id INTEGER, text TEXT, type TEXT, current TEXT, target TEXT, progress INTEGER)''')

        cursor.execute('''INSERT INTO task_data (user_id, text, type, current, target, progress)
                            VALUES (?, ?, ?, ?, ?, ?)''', (user_id, text, time, repeat, repeat_frq, task))

        conn.commit()    
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT,
        username TEXT,
        language_code TEXT,
        is_bot INTEGER
    )
''')

conn.commit()


def save_user_to_db(user_id, first_name, last_name, username, language_code, is_bot):
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, first_name, last_name, username, language_code, is_bot)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, first_name, last_name, username, language_code, is_bot))

    conn.commit()
    import atexit
    atexit.register(lambda: conn.close())


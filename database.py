import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        wallet TEXT DEFAULT 'Cash',
        note TEXT DEFAULT '',
        recurring INTEGER DEFAULT 0
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS savings_goal (
        id INTEGER PRIMARY KEY,
        monthly_budget REAL DEFAULT 0,
        savings_target REAL DEFAULT 0
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT DEFAULT '',
        income REAL DEFAULT 0,
        photo TEXT DEFAULT ''
    )''')

    c.execute('INSERT OR IGNORE INTO savings_goal (id, monthly_budget, savings_target) VALUES (1, 0, 0)')
    c.execute('INSERT OR IGNORE INTO profile (id, name, income, photo) VALUES (1, "", 0, "")')

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn
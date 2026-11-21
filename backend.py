import sqlite3
import random

DB_FILE = "database.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_record(name, category, score):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO records (name, category, score) VALUES (?, ?, ?)",
        (name, category, score)
    )
    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM records").fetchall()
    conn.close()
    return [dict(row) for row in rows]

def seed_big_data():
    if len(get_all_records()) == 0:
        categories = ["Cardiology", "Trauma", "Neurology", "General"]
        conn = sqlite3.connect(DB_FILE)
        rows = [(f"Patient #{i}", random.choice(categories), random.randint(40, 100)) for i in range(1, 501)]
        conn.executemany("INSERT INTO records (name, category, score) VALUES (?, ?, ?)", rows)
        conn.commit()
        conn.close()
import sqlite3
from datetime import datetime
from config import DB_NAME


def add_task(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    current_date = datetime.now().strftime("%d.%m.%Y %H:%M")

    cursor.execute(
        "INSERT INTO tasks (title, date) VALUES (?, ?)",
        (title, current_date)
    )

    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, date FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

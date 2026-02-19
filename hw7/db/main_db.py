import sqlite3

DB_NAME = "todo.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        """)
        conn.commit()


def add_new_task(name):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, completed) VALUES (?, 0)",
            (name,)
        )
        conn.commit()
        return cursor.lastrowid


def edit_task(task_id, new_value):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET name = ? WHERE id = ?",
            (new_value, task_id)
        )
        conn.commit()


def set_completed(task_id, value):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?",
            (value, task_id)
        )
        conn.commit()


def delete_task(task_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()


def delete_completed_tasks():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE completed = 1"
        )
        conn.commit()


def get_all_tasks():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM tasks")
        return cursor.fetchall()

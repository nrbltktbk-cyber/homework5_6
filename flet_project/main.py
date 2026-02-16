import flet as ft
from db import main_db
from db.queries import add_task, get_tasks


def main(page: ft.Page):
    main_db.create_tables()

    task_input = ft.TextField(label="Новая задача")

    task_column = ft.Column()

    def refresh_tasks():
        task_column.controls.clear()
        tasks = get_tasks()

        for task in tasks:
            task_column.controls.append(
                ft.Text(f"{task[1]} - {task[2]}")
            )

        page.update()

    def add_click(e):
        if task_input.value:
            add_task(task_input.value)
            task_input.value = ""
            refresh_tasks()

    page.add(
        task_input,
        ft.ElevatedButton("Добавить", on_click=add_click),
        task_column
    )

    refresh_tasks()


ft.app(target=main)

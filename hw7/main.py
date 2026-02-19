import flet as ft
from db import main_db


def main(page: ft.Page):
    tasks_column = ft.Column()

    # ---------------- БД ----------------

    def add_to_db(name):
        task_id = main_db.add_new_task(name)
        print(f"Добавлена новая задача: {name} ID: {task_id}")
        return task_id

    def edit_db(task_id, new_value):
        main_db.edit_task(task_id, new_value)
        print("Задача успешно обновлена!")

    def delete_from_db(task_id):
        main_db.delete_task(task_id)

    # ---------------- UI задачи ----------------

    def add_task(task_id, task):

        task_text = ft.TextField(
            value=task,
            expand=True,
            read_only=True,
        )

        completed_checkbox = ft.Checkbox()

        def toggle_completed(e):
            value = 1 if completed_checkbox.value else 0
            main_db.set_completed(task_id, value)

        completed_checkbox.on_change = toggle_completed

        def edit(e):
            edit_db(task_id, task_text.value)
            task_text.read_only = True
            page.update()

        def delete(e):
            delete_from_db(task_id)
            tasks_column.controls.remove(task_row)
            page.update()

        def to_edit(e):
            task_text.read_only = False
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=edit)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete)

        task_row = ft.Row(
            [completed_checkbox, task_text, edit_button, save_button, delete_button]
        )

        return task_row

    # ---------------- Добавление ----------------

    def add_new_task(e):
        if user_input.value and user_input.value.strip() != "":
            task_id = add_to_db(user_input.value)

            row = add_task(task_id, user_input.value)
            tasks_column.controls.append(row)

            user_input.value = ""
            page.update()

    # ---------------- Загрузка из БД ----------------

    def load_from_db():
        tasks_column.controls.clear()

        results = main_db.get_all_tasks()
        if results:
            for task_id, task_name in results:
                row = add_task(task_id, task_name)
                tasks_column.controls.append(row)

        page.update()

    # ---------------- Очистка выполненных ----------------

    def clear_completed(e):
        main_db.delete_completed_tasks()

        tasks_column.controls = [
            row for row in tasks_column.controls
            if not row.controls[0].value
        ]

        page.update()

    clear_button = ft.ElevatedButton(
        "Очистить выполненные",
        on_click=clear_completed
    )

    user_input = ft.TextField(
        label="Новая задача",
        expand=True,
        on_submit=add_new_task
    )

    enter_button = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=add_new_task
    )

    main_row = ft.Row([user_input, enter_button])

    page.add(main_row, clear_button, tasks_column)

    load_from_db()


if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main)

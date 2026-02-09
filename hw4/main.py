import flet as ft
from datetime import datetime

def app(page: ft.Page):
    page.title = "Приветствия"

    history = []  # Список истории приветствий

    # Текст для отображения последнего приветствия
    plain_text = ft.Text(value="Hello world")
    # Текст для сообщений об ошибках или пустой истории
    status_text = ft.Text(value="", color=ft.Colors.RED)

    # Функция изменения темы
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)

    # Функция добавления приветствия
    def change(e):
        txt = user_input.value.strip()
        if txt:
            now = datetime.now()
            time_str = now.strftime("%Y:%m:%d - %H:%M:%S")
            message = f"{time_str} - Привет, {txt}!"
            
            # Добавляем в историю
            history.append(message)
            
            plain_text.color = None
            plain_text.value = message
            status_text.value = ""
        else:
            plain_text.value = "Введите правильное имя!"
            plain_text.color = ft.Colors.RED

        page.update()

    # Функция удаления последнего приветствия
    def delete_last(e):
        if history:
            history.pop()  # удаляем последний элемент
            if history:
                plain_text.value = history[-1]  # показываем новое последнее
                plain_text.color = None
            else:
                plain_text.value = "Hello world"  # если история пуста
            status_text.value = ""
        else:
            status_text.value = "История пуста!"
        page.update()

    # Элементы интерфейса
    btn_send = ft.TextButton("Отправить", on_click=change)
    btn_delete = ft.TextButton("Удалить последнее", on_click=delete_last)
    user_input = ft.TextField(label="Enter name", on_submit=change)

    page.add(
        plain_text,
        user_input,
        btn_send,
        btn_delete,
        icon_button,
        status_text
    )

ft.app(target=app)

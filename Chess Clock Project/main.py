import flet as ft
from flet import (
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    TextButton,
    MainAxisAlignment,
    CrossAxisAlignment,
    margin,
)


def main(page: Page) -> None:

    page.title = "Chess Clock"
    page.bgcolor = "#092635"
    page.window_resizable = "false"
    page.window_max_width = 430
    page.window_max_height = 932
    page.auto_scroll = True
    page.scroll = "auto"
    page.horizontal_alignment = "center"

    def play_1(e):
        if e.control.bgcolor != "#5C8374" and e.control.key == "Player 1":
            e.control.bgcolor = "#5C8374"
            page.update()
            print(e.control)
        else:
            e.control.bgcolor = "#193838"
            page.update()
            
    def play_2(e):
        if e.control.bgcolor != "#5C8374":
            e.control.bgcolor = "#5C8374"
            page.update()
            print(e.control)
        else:
            e.control.bgcolor = "#193838"
            page.update()


    _player_1 = ft.Container(key="Player 1",
        content=Text("00:00", size=36),
        width=350,
        height=300,
        alignment=ft.alignment.center,
        border_radius=30,
        bgcolor="#193838",
        on_click=play_1,
    )

    _action = ft.Row(
        controls=[
            ft.Icon(ft.icons.PLAY_ARROW_ROUNDED, scale=2),
            ft.Icon(ft.icons.PAUSE_ROUNDED, scale=2),
            ft.Icon(ft.icons.REFRESH_ROUNDED, scale=2),
            ft.Icon(ft.icons.CANCEL_ROUNDED, scale=1.7),
        ],
        alignment="center",
        spacing=24,
    )

    _player_2 = ft.Container(key="Player 2",
        content=Text("00:00", size=36),
        width=350,
        height=300,
        alignment=ft.alignment.center,
        border_radius=30,
        bgcolor="#193838",
        on_click=play_2,
    )

    _r = ft.Column(
        controls=[
            ft.Row(controls=[_player_1], alignment="center"),
            _action,
            ft.Row(controls=[_player_2], alignment="center"),
        ],
        spacing=24,
    )

    page.add(_r)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)

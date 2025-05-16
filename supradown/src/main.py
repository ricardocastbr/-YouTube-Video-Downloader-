import flet as ft
from pytubefix import YouTube
import os

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    entrada_usuario = ft.TextField(
        label="Link do vídeo:",
        prefix_icon=ft.Icons.LINK,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        border_width=2,
    )


    page.add(
        ft.Column(
            controls=[
                entrada_usuario,
            ]
        )
    )
    page.update()


ft.app(main)
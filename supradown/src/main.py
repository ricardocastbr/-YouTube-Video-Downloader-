import flet as ft
from pytubefix import YouTube
import os

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Supradown'),
        center_title=True,
        bgcolor=ft.Colors.BLACK54,
        actions=[  
            ft.Image(
                src='assets/logo.png',
                width=70,
                height=70,
                fit=ft.ImageFit.COVER,
            )
        ]
    )

    entrada_usuario = ft.TextField(
        label="Link do vídeo:",
        prefix_icon=ft.Icons.LINK,
        width=300,
        border_color=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        border_width=2,
    )


    button_usuario = ft.ElevatedButton(
        text = "Baixar",
        width=300,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
    )



    page.add(
        ft.Column(
            controls=[
                entrada_usuario,
                button_usuario,
            ]
        )
    )
    page.update()


ft.app(main, assets_dir="assets")
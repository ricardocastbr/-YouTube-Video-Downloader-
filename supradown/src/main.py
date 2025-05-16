import flet as ft
from pytubefix import YouTube
import os

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREY_900
    page.appbar = ft.AppBar(
        title=ft.Text('Supradown'),
        center_title=True,
        bgcolor=ft.Colors.BLACK54,
        actions=[  
            ft.Image(
                src='assets/logo.png',
                width=100,
                height=100,
                fit=ft.ImageFit.COVER,
            )
        ]
    )

    def baixar_videos(e):
        url = entrada_usuario.value.strip()
        if not url:
            status_texto.value = "Por favor, insira um link de vídeo."
            page.update()
            return

        pasta_download = "Downloads"
        os.makedirs(pasta_download, exist_ok=True)

        status_texto.value = "Baixando vídeo..."
        page.update()



        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        stream.download(output_path=pasta_download)
        status_texto.value = f"Vídeo baixado com sucesso em {pasta_download}!"
        page.update()



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
        on_click=baixar_videos,
    )

    status_texto = ft.Text()


    page.add(
        ft.Column(
            controls=[
                entrada_usuario,
                button_usuario,
                status_texto,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        )
    )
    page.update()


ft.app(main, assets_dir="assets")
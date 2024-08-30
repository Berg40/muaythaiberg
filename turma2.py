import flet as ft

def turma2_view(page: ft.Page):

    def change_main_image(e):
        # Verifica qual miniatura foi clicada
        clicked_container = e.control
        # Atualiza a imagem principal com a imagem da miniatura clicada
        main_image.src = clicked_container.image_src
        # Atualiza a opacidade de todas as miniaturas
        for container in options.controls:
            if container == clicked_container:
                container.opacity = 1
            else:
                container.opacity = 0.5
        # Atualiza a interface
        main_image.update()
        options.update()

    main_image = ft.Image(
        src='images/20.jpg',
        border_radius=ft.border_radius.all(20),
    )

    options = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        controls=[
            ft.Container(
                image_src='images/20.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/21.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/22.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/23.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/24.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/25.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/26.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/27.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/28.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/29.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/30.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/31.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/32.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/33.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/34.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/35.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/36.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/37.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/38.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            )
        ],
    )
    products_images = ft.Container(

        content=ft.Column(
            spacing=10,
            controls=[main_image, options]
        )
    )
    layout = ft.Container(
        width=900,
        margin=ft.margin.symmetric(vertical=60, horizontal=20),
        shadow=ft.BoxShadow(blur_radius=40, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            controls=[products_images]
        )
    )

    return layout
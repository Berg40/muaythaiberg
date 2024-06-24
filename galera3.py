import flet as ft

def galera3_view(page: ft.Page):

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
        src='images/46.jpg',
        border_radius=ft.border_radius.all(20),
    )

    options = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        controls=[
            ft.Container(
                image_src='images/46.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/42.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/43.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/44.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/45.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),

            ft.Container(
                image_src='images/47.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/48.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/49.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/50.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/51.jpg',
                width=40,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/41.jpg',
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
        shadow=ft.BoxShadow(blur_radius=40, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            controls=[products_images]
        )
    )

    return layout


import flet as ft

def teste2_view(page: ft.Page):

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
        src='images/15.jpg',
        border_radius=ft.border_radius.all(20),
    )

    options = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                image_src='images/15.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/1.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/2.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/3.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/4.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/5.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/6.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/7.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/8.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/9.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/10.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/11.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/12.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/13.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/16.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
            ft.Container(
                image_src='images/17.jpg',
                width=60,
                height=50,
                opacity=0.5,
                on_click=change_main_image
            ),
        ],
    )
    products_images = ft.Container(
        content=ft.Column(
            controls=[main_image, options]
        )
    )
    layout = ft.Container(
        width=600,
        height=800,
        margin=ft.margin.symmetric(vertical=40, horizontal=20),
        shadow=ft.BoxShadow(blur_radius=40, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            spacing=5,
            controls=[products_images]
        )
    )

    return layout


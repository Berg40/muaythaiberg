import flet as ft
from graduados1 import graduados1_view
from turma2 import turma2_view
from galera3 import galera3_view
import asyncio
import math
import os


def main(page: ft.Page):
    page.window_always_on_top = True
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    #page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT  # Inicialmente tema claro
    page.update()

    page.fonts = {
        'font': 'fonts/GraffitiDripes-Regular.otf',
        'font2': 'fonts/BrontidevpDemoStyle2-ZV8E3.otf',
        'prata': 'images/fonts/Prata-Regular.ttf'
    }

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    async def animate(e=None):
        while True:
            cont.scale = ft.Scale(scale=1.5)
            cont.update()
            await asyncio.sleep(1)
            cont.scale = ft.Scale(scale=0.6)
            cont.update()
            await asyncio.sleep(1)

    async def anima(e=None):  # Animate desativado
        while True:
            foto1.offset = ft.Offset(x=-1, y=0)
            foto1.update()
            await asyncio.sleep(4)  # Tempo escondido
            foto1.offset = ft.Offset(x=0.9, y=0)
            foto1.update()
            await asyncio.sleep(10)

    async def anima1(e=None):
        while True:
            foto2.offset = ft.Offset(x=-1, y=0)
            foto2.update()
            await asyncio.sleep(4)
            foto2.offset = ft.Offset(x=0.05, y=0)
            foto2.update()
            await asyncio.sleep(10)

    async def anima2(e=None):
        while True:
            foto3.offset = ft.Offset(x=-1, y=0)
            foto3.update()
            await asyncio.sleep(4)
            foto3.offset = ft.Offset(x=0.8, y=0)
            foto3.update()
            await asyncio.sleep(10)

    cont = ft.Container(
        height=300,
        width=400,
        image_src='images/logo.png',
        image_fit=ft.ImageFit.CONTAIN,
        scale=ft.Scale(scale=0.5),
        animate_scale=ft.Animation(duration=1000, curve=ft.AnimationCurve.DECELERATE),
    )

    texto = ft.Text(
        color='WHITE',
        offset=ft.Offset(y=0, x=0),
        value='''
            Olá, meu nome é Berg Andrade e sou professor de Muay Thai com 10 anos de experiência dedicada a esse esporte incrível. Ao longo de uma década, tive a honra de guiar muitos alunos em suas jornadas de autodescoberta, força e disciplina.
            Meu objetivo vai além de ensinar técnicas de combate; busco inspirar meus alunos a abraçar o Muay Thai como um estilo de vida que promove equilíbrio, confiança e bem-estar físico e mental. Cada aula é uma oportunidade de superar limites, desenvolver habilidades e crescer tanto no tatame quanto fora dele.
            Estou comprometido em proporcionar treinos de alta qualidade, adaptados às necessidades individuais de cada aluno. Juntos, trabalhamos não apenas para alcançar metas de condicionamento físico, mas também para fortalecer a mente e o espírito.
            Venha experimentar a transformação que o Muay Thai pode trazer para sua vida. Vamos treinar juntos e descobrir o verdadeiro poder que reside dentro de você!
        '''
    )

    foto1 = ft.Container(
        height=100,
        width=200,
        content=ft.Text(
            font_family='prata',
            italic=True,
            value='Força',
            style=ft.TextStyle(
                foreground=ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        begin=ft.Offset(x=0, y=0),
                        end=ft.Offset(x=600, y=0),
                        colors=[
                            ft.colors.YELLOW_700,
                            ft.colors.BLACK54,

                        ]
                    )
                )
            ),
            size=60
        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )
    foto2 = ft.Container(
        height=100,
        width=200,
        content=ft.Text(
            color=ft.colors.INDIGO_900,
            font_family='prata',
            italic=True,
            weight=ft.FontWeight.BOLD,
            value='Superação',
            style=ft.TextStyle(
                foreground=ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        begin=ft.Offset(x=0, y=500),
                        end=ft.Offset(x=500, y=0),
                        colors=[
                            ft.colors.YELLOW_700,
                            ft.colors.BLACK54,

                        ]
                    )
                )
            ),
            size=35

        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )
    foto3 = ft.Container(
        height=100,
        width=250,
        content=ft.Text(

            font_family='prata',
            italic=True,
            value='Técnica',
            style=ft.TextStyle(
                foreground=ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        begin=ft.Offset(x=0, y=0),
                        end=ft.Offset(x=600, y=0),
                        colors=[
                            ft.colors.YELLOW_700,
                            ft.colors.BLACK54,

                        ]
                    )
                )
            ),
            size=50

        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )

    jab = ft.Container(
        height=200,
        width=500,
        image_src='images/Jab.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=5000, curve=ft.AnimationCurve.DECELERATE),
    )

    direto = ft.Container(
        height=200,
        width=500,
        offset=ft.Offset(y=0, x=0),
        image_src='images/Direto.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    cruzado = ft.Container(
        height=200,
        width=500,
        image_src='images/Cruzado.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    upper = ft.Container(
        height=200,
        width=500,

        image_src='images/Upeercut.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    frontal = ft.Container(
        height=200,
        width=500,

        image_src='images/Chute Frontal.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    chute = ft.Container(
        height=200,
        width=500,
        image_src='images/Chutebaixo.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    joelhada = ft.Container(
        height=200,
        width=500,
        image_src='images/Joelho.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    cotovelada = ft.Container(
        height=200,
        width=500,
        image_src='images/CotoveloHorizontal.gif',
        image_fit=ft.ImageFit.SCALE_DOWN,
        # scale=ft.Scale(scale=1),
        # animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    page.update()

    def open_whatsapp(e):
        whatsapp_url = 'https://api.whatsapp.com/send?phone=5512997071992'
        page.launch_url(whatsapp_url)

    def change_route(e):  # Navigation Drawer route change function
        if e.control.selected_index == 0:
            page.go('/')
        elif e.control.selected_index == 1:
            page.go('/Golpes')
        elif e.control.selected_index == 2:
            page.go('/Origem')
        elif e.control.selected_index == 3:
            page.go('/galera3')
        elif e.control.selected_index == 4:
            page.go('/turma2')
        elif e.control.selected_index == 5:
            page.go('/graduados1')

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                floating_action_button=ft.FloatingActionButton(
                    content=ft.Image(
                        src='images/whatssfundo.png',
                        fit=ft.ImageFit.CONTAIN
                    ),
                    on_click=open_whatsapp,
                    shape=ft.CircleBorder('circle'),
                    scale=0.9
                ),
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                route='/',
                padding=0,
                appbar=ft.AppBar(
                    bgcolor=ft.colors.TRANSPARENT,
                    actions=[
                        ft.IconButton(
                            icon=ft.icons.BRIGHTNESS_6,
                            on_click=toggle_theme
                        )
                    ]
                ),
                controls=[
                    cont,
                    ft.Stack(
                        controls=[
                            ft.Container(
                                image_src='images/Mármore final.jpg',
                                image_fit=ft.ImageFit.FIT_HEIGHT,
                                image_opacity=1,
                                margin=0,
                                padding=ft.Padding(top=20, bottom=0, left=20, right=20),
                                gradient=ft.SweepGradient(  # Ele inicia do centro para direita, como se fosse um leque
                                    colors=[
                                        ft.colors.GREY_500, ft.colors.GREY_800, ft.colors.GREY_500],
                                    stops=[0, 0.5, 1],
                                    center=ft.Alignment(x=0, y=0),
                                    rotation=math.radians(60)
                                ),
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Container(
                                            height=400,
                                            width=500,
                                            image_src='images/TEXTO1.jpg',
                                            image_fit=ft.ImageFit.CONTAIN

                                        ),

                                        ft.Container(
                                            height=700,
                                            width=500,
                                            border_radius=ft.BorderRadius(top_left=20, top_right=20, bottom_right=20,
                                                                          bottom_left=20),
                                            image_src='images/TEXTO2.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),

                                        ft.Container(
                                            height=480,
                                            width=500,
                                            image_src='images/TEXTO3.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),

                                        ft.Container(
                                            height=620,
                                            width=500,
                                            image_src='images/TEXTO04.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=520,
                                            width=500,
                                            image_src='images/TEXTO5.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=680,
                                            width=500,
                                            image_src='images/TEXTO6.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=550,
                                            width=500,
                                            image_src='images/TEXTO7.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=500,
                                            width=500,
                                            image_src='images/TEXTO8.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=650,
                                            width=500,
                                            image_src='images/TEXTO9.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Container(
                                            height=600,
                                            width=500,
                                            image_src='images/TEXTO10.jpg',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                    ft.Container(
                        height=600,
                        width=600,
                        padding=10,
                        bgcolor='black',
                        image_src='images/fotoCapa.png',
                        image_fit=ft.ImageFit.CONTAIN,
                        # offset=ft.Offset(y=0, x=0),
                        # animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE_IN),
                        content=ft.Column(
                            spacing=140,
                            controls=[
                                foto1,
                                foto2,
                                ft.Container(
                                    height=200,
                                    width=200,
                                    content=foto3
                                )

                            ]
                        )
                    ),

                    ft.Container(
                        height=550,
                        width=500,
                        padding=ft.padding.only(left=10, right=10, top=40, bottom=20),
                        bgcolor=ft.colors.GREY_800,
                        image_src='images/logo.pgn',
                        image_fit=ft.ImageFit.COVER,
                        image_opacity=0.3,
                        content=ft.Column(
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Row(
                                    wrap=True,
                                    col=2,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            height=80,
                                            width=60,
                                            padding=ft.padding.only(left=0, right=0, top=0, bottom=0),
                                            image_src='images/logo.png',
                                            image_fit=ft.ImageFit.COVER,
                                        ),
                                        ft.Container(
                                            height=80,
                                            width=200,
                                            padding=ft.padding.only(top=20, left=0, right=0, bottom=0),
                                            content=ft.Column(
                                                spacing=0,
                                                controls=[
                                                    ft.Text(
                                                        value='BERG ANDRADE',
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.colors.WHITE,
                                                        italic=True,
                                                        size=15,
                                                    ),
                                                    ft.Text(
                                                        value='Professor de Muay Thai | Personal Fight',
                                                        size=10,
                                                        color=ft.colors.WHITE54
                                                    )
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='Treinos personalizados e focados no',
                                    color=ft.colors.WHITE
                                ),
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='seu objetivo de saúde e qualidade de',
                                    color=ft.colors.WHITE
                                ),
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='vida. Vem treinar comigo.',
                                    color=ft.colors.WHITE
                                ),
                                ft.Container(
                                    height=80,
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                    run_spacing=0,
                                    controls=[
                                        ft.Container(
                                            height=25,
                                            width=25,
                                            image_src='images/whatssfundo.png',
                                            image_fit=ft.ImageFit.CONTAIN
                                        ),
                                        ft.Text(
                                            value='(12) 997071992',
                                            color=ft.colors.WHITE,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                    run_spacing=5,
                                    controls=[
                                        ft.Container(
                                            height=25,
                                            width=25,
                                            image_src='images/instagram1.png',
                                            image_fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.TextButton(
                                            tooltip='Acesse meu Instagram',
                                            text='@berg_andrade2',
                                            url='https://www.instagram.com/berg_andrade2/',
                                        ),
                                    ]
                                ),
                                ft.Container(
                                    height=150
                                ),
                                ft.Text(
                                    value='Copyright 2024 Berg Andrade | Criado',
                                    color=ft.colors.WHITE54,
                                    size=10
                                ),
                                ft.Text(
                                    value='Por: Berg Andrade Digital',
                                    color=ft.colors.WHITE54,
                                    size=10
                                ),
                                ft.Divider()
                            ]
                        )
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                bgcolor=ft.colors.BLACK,
                drawer=ft.NavigationDrawer(
                    indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                    bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                    tile_padding=ft.padding.symmetric(horizontal=0),
                    controls=[
                        ft.NavigationDrawerDestination(
                            label='Home',
                            icon_content=ft.Container(
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )
                        ),
                        ft.NavigationDrawerDestination(
                            label='Golpes',
                            icon_content=ft.Container(
                                margin=0,
                                padding=0,
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )

                        ),
                        ft.NavigationDrawerDestination(
                            label='Origem',
                            icon_content=ft.Container(
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )
                        ),
                        ft.NavigationDrawerDestination(
                            label='Graduados 22/06/2024',
                            icon_content=ft.Container(
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )
                        ),
                        ft.NavigationDrawerDestination(
                            label='Graduados 09/12/2023',
                            icon_content=ft.Container(
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )

                        ),
                        ft.NavigationDrawerDestination(
                            label='Graduados 23/06/2023',
                            icon_content=ft.Container(
                                height=100,
                                width=100,
                                image_src='images/logo.png',
                                image_fit=ft.ImageFit.CONTAIN
                            )
                        ),

                    ],
                    on_change=change_route,
                ),
            )
        )
        if page.route == '/Golpes':
            page.views.append(
                ft.View(
                    scroll=ft.ScrollMode.AUTO,
                    bgcolor='#1B1C1D',
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9,
                    ),
                    route='/Golpes',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_6,
                                on_click=toggle_theme
                            )
                        ]
                    ),
                    controls=[
                        ft.Container(
                            image_src='images/Mármore final.jpg',
                            image_fit=ft.ImageFit.FIT_HEIGHT,
                            image_opacity=1,
                            margin=0,
                            padding=ft.Padding(top=20, bottom=0, left=20, right=20),
                            content=ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        padding=20,
                                        border_radius=10,
                                        bgcolor='#1B1C1D',
                                        content=ft.Text(
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            # italic=True,
                                            font_family='prata',
                                            style=ft.TextStyle(
                                                foreground=ft.Paint(
                                                    gradient=ft.PaintLinearGradient(
                                                        begin=ft.Offset(x=50, y=0),
                                                        end=ft.Offset(x=800, y=0),
                                                        colors=[
                                                            '#D2AC47',
                                                            '#0D0D09',
                                                        ]
                                                    )
                                                )
                                            ),
                                            text_align=ft.TextAlign.CENTER,
                                            value='''MUAY THAI
                                                GOLPES''',
                                        )
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                padding=20,
                                                border_radius=10,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O Muay Thai é conhecido por sua diversidade de técnicas e pela eficiência de seus golpes. Este tópico foi cuidadosamente desenvolvido para oferecer a você uma compreensão profunda e clara de cada movimento, desde os socos poderosos até as joelhadas e cotoveladas precisas.'''
                                                        ),
                                                        ft.Container(
                                                            height=400,
                                                            width=500,
                                                            image_src='images/IMG-20220402-WA0035.jpg',
                                                            image_fit=ft.ImageFit.CONTAIN,
                                                        ),
                                                        ft.Container(
                                                            padding=20,
                                                            bgcolor='#1B1C1D',
                                                            content=ft.Text(
                                                                size=16,
                                                                color='#CFCBBF',

                                                                font_family='prata',
                                                                text_align=ft.TextAlign.CENTER,
                                                                value='''O que você encontrará neste tópico:

Socos:  Aprenda os diferentes tipos de socos, desde o jab até o cruzado, com instruções passo a passo e dicas para aprimorar sua técnica e potência.

Chutes: Explore a variedade de chutes do Muay Thai, incluindo o chute circular, chute frontal e muito mais.

Joelhadas: Descubra como aplicar joelhadas devastadoras, tanto em combates de curta distância quanto em clinch, aprimorando sua capacidade de ataque e defesa.

Cotoveladas: As cotoveladas são algumas das técnicas mais letais do Muay Thai. Aqui, você aprenderá a usar essas armas com precisão e eficácia.

Cada golpe é explicado com detalhes. Neste site, você terá acesso a um guia abrangente que facilitará o aprendizado e o aprimoramento das suas habilidades no Muay Thai.'''
                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        jab,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='JAB DO MUAY THAI',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O soco mais básico do Muay Thai é o jab. Ele é desferido com a mão da frente, é rápido, tem como alvo do rosto do adversário.
Embora o principal objetivo do jab seja o controle da distância e não ser o golpe de maior força, pode ter potencial de nocaute, dependendo da força e da técnica do lutador.'''
                                                        )

                                                    ]
                                                )
                                            ),

                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        direto,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Direto do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O direto é o golpe de mãos mais forte do arsenal do lutador de Muay Thai, pois é desferido com a mão traseira, carregando enorme potência.
Assim como o jab, o alvo principal do direto é o rosto do adversário e, se bem conectado, pode levar ao nocaute com facilidade.
Outro possível alvo do direto é o torso do oponente, visando fígado.'''
                                                        )

                                                    ]
                                                )
                                            ),

                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        cruzado,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Cruzado do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O soco cruzado tem como alvo a cabeça do oponente, sendo desferido de um ângulo lateral e visando mais precisamente o queixo.
É um golpe bastante técnico, pode ser desferido com ambas as mãos (dianteira ou traseira) e possui grande potencial de derrubar o adversário.'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        upper,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Upper do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O gancho é um golpe desferido de baixo para cima e pode facilmente atravessar as defesas do lutador adversário.
Seus alvos são tanto o rosto quanto o abdômen (fígado). Tem potência elevada e pode levar ao nocaute em ambos os casos quando bem encaixado, sendo eficiente principalmente a curtas e médias distâncias
Além disso, assim como o cruzado, pode ser desferido tanto com a mão dianteira quanto com a mão traseira.'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        frontal,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Chutes Frontais (pernas traseira e dianteira)',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O chute frontal, também conhecido como teep no Muay Thai, é uma técnica básica que busca criar e controlar a distância, podendo também ser usado para derrubar o adversário.
Pode ser lançado com ambas as pernas (dianteira e traseira), tendo como alvo os quadris, o abdômen, o peito e também o rosto do oponente.'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        chute,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Chute Lateral do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O chute lateral do Muay Thai é considerado como a técnica de chute mais forte dentre as artes marciais.
Extremamente potente, é desferido com a perna traseira e baseia-se na ideia de um machado atravessando lateralmente o oponente, seja para cortar sua perna, seu tronco ou sua cabeça.
Sendo assim, possui três variações de altura: baixo (mirando a perna dianteira), médio (mirando tronco) e alto (mirando a cabeça do oponente).'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        joelhada,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Joelhadas do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O Muay Thai possui diversas variações da joelhada. Esses golpes podem ter média, curta e longa distância, dependendo da técnica utilizada.
A joelhada mais básica do Muay Thai é a joelhada direta, que pode ser executada com qualquer um dos joelhos, sendo elas a joelhada direta e a joelhada trocada.
Como você já pode imagina, a joelhada direta é desferida com o joelho traseiro, enquanto a joelhada trocada é desferida com a perna dianteira obedecendo os mesmos princípios do chute trocado (troca de base para melhor gerar potência.
Essas joelhadas visam atacar diretamente abdômen e plexo solar do oponente.'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[

                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Cotoveladas do Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''Golpes de cotovelo são bastante característicos do Muay Thai e são usados em curta distância e/ou dentro do clinch.
Os principais golpes de cotovelo são:
Horizontal;
Ascendente;
Diagonal;'''
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        cotovelada,
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''Cotovelada Horizontal ou Lateral do Muay Thai''',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''A cotovelada horizontal ou lateral é um golpe visando o rosto do oponente, cortando horizontalmente, ou seja, traçando um vetor paralelo ao chão.
Assim como vários outros golpes, pode ser executado tanto com o cotovelo dianteiro quanto com o traseiro.''',
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            height=200,
                                                            width=500,
                                                            image_src='images/Cotovelo Ascendente .gif',
                                                            image_fit=ft.ImageFit.SCALE_DOWN,
                                                        ),
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''Cotovelada Ascendente do Muay Thai''',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''A cotovelada ascendente é um golpe executado de baixo para cima (como o soco gancho), traçando uma linha vertical, ou seja, perpendicular ao solo (ao oposto da cotovelada horizontal).
Tem como alvo o queixo e rosto, buscando penetrar a guarda do adversário.
Também pode ser executado com ambos os cotovelos.'''
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            height=200,
                                                            width=500,
                                                            image_src='images/CotoveloDescendente.gif',
                                                            image_fit=ft.ImageFit.SCALE_DOWN,
                                                        ),
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''Cotovelada Diagonal do Muay Thai''',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''A cotovelada diagonal traça uma linha diagonal de cima para baixo, indo da esquerda para a direita ou da direita para a esquerda dependendo do lado com o qual foi desferido (lado esquerdo: cima-baixo, esquerda-direita; lado direito: cima-baixo, direita-esquerda), cruzando a frente do lutador.
Seu alvo é a testa ou o supercílio do lutador adversário, com o objetivo de causar cortes e, consequentemente, sagramentos. ''',
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Regulamentos de Combate no Muay Thai',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''No Muay Thai, os combates são regidos por uma série de regulamentos que visam garantir a segurança dos praticantes e promover um jogo justo entre os lutadores. É importante que você esteja familiarizado com essas regras antes de entrar no ringue.'''
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Técnicas Permitidas e Proibidas',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''No Muay Thai, você pode usar socos, chutes, joelhadas e cotoveladas para atacar seu oponente. No entanto, existem algumas técnicas que são proibidas, como golpes na nuca, virilha ou na parte de trás da cabeça.
Além disso, não são permitidos golpes abaixo da cintura, dedos nos olhos, mordidas ou qualquer outra conduta antiética que possa prejudicar o adversário. O descumprimento dessas regras pode resultar em punições, incluindo a desclassificação do lutador.''',
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                padding=20,
                                                bgcolor='#1B1C1D',
                                                content=ft.Column(
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            size=24,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            font_family='prata',
                                                            style=ft.TextStyle(
                                                                foreground=ft.Paint(
                                                                    gradient=ft.PaintLinearGradient(
                                                                        begin=ft.Offset(x=50, y=0),
                                                                        end=ft.Offset(x=800, y=0),
                                                                        colors=[
                                                                            '#D2AC47',
                                                                            '#0D0D09',
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='Uso de Cotovelos, Joelhos e Chutes',
                                                        ),
                                                        ft.Text(
                                                            size=16,
                                                            color='#CFCBBF',
                                                            font_family='prata',
                                                            text_align=ft.TextAlign.CENTER,
                                                            value='''O Muay Thai é conhecido por seu uso único de cotovelos, joelhos e chutes. No entanto, existem regras específicas para o uso dessas técnicas.
Por exemplo, os cotovelos só são permitidos em combates profissionais, enquanto que em lutas amadoras, seu uso é proibido. Além disso, não é permitido atingir a cabeça do oponente com o joelho.
Os chutes também possuem algumas restrições. Não é permitido realizar chutes na coxa interna, bem como chutes em um adversário que esteja caído no chão.''',
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                    ft.Divider(),
                                ]
                            )
                        )
                    ],
                    drawer=ft.NavigationDrawer(
                        indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                        tile_padding=ft.padding.symmetric(horizontal=0),
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Golpes',
                                icon_content=ft.Container(
                                    margin=0,
                                    padding=0,
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Origem',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 22/06/2024',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 09/12/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 23/06/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                        ],
                        on_change=change_route,
                    )
                )
            )
        if page.route == '/Origem':
            page.views.append(
                ft.View(
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9,
                    ),
                    scroll=ft.ScrollMode.AUTO,
                    bgcolor=ft.colors.BLACK,
                    route='/Origem',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_6,
                                on_click=toggle_theme
                            )
                        ]
                    ),

                    controls=[
                        ft.Container(
                            padding=20,
                            height=1600,
                            width=500,
                            image_src='images/Mármore final.jpg',
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Container(
                                border_radius=ft.BorderRadius(top_left=10, top_right=10, bottom_left=10,
                                                              bottom_right=10),
                                bgcolor='#1B1C1D',
                                padding=20,
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                                    controls=[
                                        ft.Text(
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            # italic=True,
                                            font_family='prata',
                                            style=ft.TextStyle(
                                                foreground=ft.Paint(
                                                    gradient=ft.PaintLinearGradient(
                                                        begin=ft.Offset(x=50, y=0),
                                                        end=ft.Offset(x=800, y=0),
                                                        colors=[
                                                            '#D2AC47',
                                                            '#0D0D09',
                                                        ]
                                                    )
                                                )
                                            ),
                                            text_align=ft.TextAlign.CENTER,
                                            value='Origem',
                                        ),
                                        ft.Divider(color='TRANSPARENT'),
                                        ft.Text(
                                            size=16,
                                            color='#CFCBBF',
                                            font_family='prata',
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''O Muay Thai tem sua origem na Tailândia, país localizado no sudeste asiático.

            As raízes da civilização tailandesa datam dos séculos I e II a.C., quando povos originários da China migraram ao sul para as regiões que futuramente iriam compor o Vietnã, o Laos, Camboja, Mianmar e também a Tailândia.

            As guerras eram nas fronteiras do então reino do Sião eram constantes e, na segunda metade do século XVI, os birmaneses ocuparam o território, transformando Aiutaia num estado dependente.

            Pouco mais de uma década depois da invasão, a independência do Sião foi estabelecida.

            É dentro desse contexto de guerras que encontramos as raízes do Muay Thai. As formas de combate corpo a corpo da região, usadas nos campos de batalha, foram se desenvolvendo e assumindo aspectos específicos das culturas que sobreviveram às guerras, embora ainda mantivessem semelhança.

            Com isso, o Muay Boran, forma de combate dos antigos guerreiros siameses, evoluiu para o que hoje conhecemos como Muay Thai, assim como os birmaneses (povo da antiga Birmânia, hoje oficialmente conhecida como Myanmar) hoje possuem o Lethwei.

            No futuro, os países europeus como Holanda e França entrariam em contato com a Tailândia, estabelecendo relações de comércio. Esse contato também teve efeito sobre o Muay Thai, uma vez que muito do boxe ocidental fora absorvido, influenciando também o sistema de regras do Muay Thai moderno.''',
                                        ),
                                        ft.Container(
                                            height=40,
                                        ),

                                        ft.Text(
                                            size=26,
                                            weight=ft.FontWeight.BOLD,

                                            font_family='prata',
                                            style=ft.TextStyle(
                                                foreground=ft.Paint(
                                                    gradient=ft.PaintLinearGradient(
                                                        begin=ft.Offset(x=50, y=0),
                                                        end=ft.Offset(x=800, y=0),
                                                        colors=[
                                                            '#D2AC47',
                                                            '#0D0D09',
                                                        ]
                                                    )
                                                )
                                            ),
                                            text_align=ft.TextAlign.CENTER,
                                            value='''Você está pronto
para EVOLUIR seu 
MUAY THAI?'''
                                        ),
                                        ft.Container(
                                            height=150,
                                            width=150,
                                            image_src='images/logo.png',
                                            image_fit=ft.ImageFit.COVER,

                                        )
                                    ]
                                ),
                            )
                        ),
                    ],

                    drawer=ft.NavigationDrawer(
                        indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                        tile_padding=ft.padding.symmetric(horizontal=0),
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Golpes',
                                icon_content=ft.Container(
                                    margin=0,
                                    padding=0,
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Origem',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 22/06/2024',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                            ft.NavigationDrawerDestination(
                                label='Graduados 09/12/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 23/06/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                        ],
                        on_change=change_route,
                    )
                )
            )
        if page.route == '/galera3':
            page.views.append(
                ft.View(
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9,
                    ),
                    route='/galera3',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_6,
                                on_click=toggle_theme
                            )
                        ]
                    ),
                    controls=[
                        galera3_view(page),

                    ],
                    scroll=ft.ScrollMode.AUTO,
                    bgcolor=ft.colors.BLACK,
                    drawer=ft.NavigationDrawer(
                        indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                        tile_padding=ft.padding.symmetric(horizontal=0),
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Golpes',
                                icon_content=ft.Container(
                                    margin=0,
                                    padding=0,
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Origem',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 22/06/2024',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                            ft.NavigationDrawerDestination(
                                label='Graduados 09/12/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 23/06/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                        ],
                        on_change=change_route,
                    )
                )
            )
        if page.route == '/turma2':
            page.views.append(
                ft.View(
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9,
                    ),
                    route='/turma2',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_6,
                                on_click=toggle_theme
                            )
                        ]
                    ),
                    controls=[
                        turma2_view(page),

                    ],
                    scroll=ft.ScrollMode.AUTO,
                    bgcolor=ft.colors.BLACK,
                    drawer=ft.NavigationDrawer(
                        indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                        tile_padding=ft.padding.symmetric(horizontal=0),
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Golpes',
                                icon_content=ft.Container(
                                    margin=0,
                                    padding=0,
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Origem',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 22/06/2024',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                            ft.NavigationDrawerDestination(
                                label='Graduados 09/12/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 23/06/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                        ],
                        on_change=change_route,
                    )
                )
            )
        if page.route == '/graduados1':
            page.views.append(
                ft.View(
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9,
                    ),
                    route='/graduados1',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        actions=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_6,
                                on_click=toggle_theme
                            )
                        ]
                    ),
                    controls=[
                        graduados1_view(page)
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    bgcolor=ft.colors.BLACK,
                    drawer=ft.NavigationDrawer(
                        indicator_color=ft.colors.with_opacity(0.5, ft.colors.CYAN_ACCENT_200),
                        bgcolor=ft.colors.with_opacity(0.5, ft.colors.INDIGO_900),
                        tile_padding=ft.padding.symmetric(horizontal=0),
                        controls=[
                            ft.NavigationDrawerDestination(
                                label='Home',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Golpes',
                                icon_content=ft.Container(
                                    margin=0,
                                    padding=0,
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Origem',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 22/06/2024',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                            ft.NavigationDrawerDestination(
                                label='Graduados 09/12/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )

                            ),
                            ft.NavigationDrawerDestination(
                                label='Graduados 23/06/2023',
                                icon_content=ft.Container(
                                    height=100,
                                    width=100,
                                    image_src='images/logo.png',
                                    image_fit=ft.ImageFit.CONTAIN
                                )
                            ),

                        ],
                        on_change=change_route,
                    )
                )
            )

        page.update()
        page.add(cont, texto, foto1, foto2, jab, direto, cruzado,
                 upper, frontal, chute, joelhada, cotovelada)
        page.run_task(animate)
        page.run_task(anima)
        page.run_task(anima1)
        page.run_task(anima2)

    def view_pop(view):  # View pop function
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__': 
    ft.app(target=main, assets_dir='assets')  # para colocar no heroku
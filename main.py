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
    page.theme_mode = ft.ThemeMode.LIGHT  # Inicialmente tema claro
    page.update()

    page.fonts = {
        'font': 'fonts/GraffitiDripes-Regular.otf',
        'font2': 'fonts/BrontidevpDemoStyle2-ZV8E3.otf',
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

    async def anima(e=None):  #Animate desativado
        while True:
            foto1.offset = ft.Offset(x=-1, y=0)
            foto1.update()
            await asyncio.sleep(4)  #Tempo escondido
            foto1.offset = ft.Offset(x=1.25, y=0)
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
            foto3.offset = ft.Offset(x=1.1, y=0)
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
            color=ft.colors.INDIGO_900,
            font_family='font',
            italic=True,
            value='Força',
            size=70
        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )
    foto2 = ft.Container(
        height=100,
        width=200,
        content=ft.Text(
            color=ft.colors.INDIGO_900,
            #font_family='font2',
            italic=True,
            weight=ft.FontWeight.BOLD,
            value='Superação',
            size=35

        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )
    foto3 = ft.Container(
        height=100,
        width=200,
        content=ft.Text(
            color=ft.colors.INDIGO_900,
            font_family='font',
            italic=True,
            value='Técnica',
            size=60

        ),
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )

    jab = ft.Container(
        height=200,
        width=1300,
        image_src='images/BackgroundEraser_20240615_145746624.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=5000, curve=ft.AnimationCurve.DECELERATE),
    )

    direto = ft.Container(
        height=200,
        width=1300,
        offset=ft.Offset(y=0, x=0),
        image_src='images/BackgroundEraser_20240615_145722056.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    cruzado = ft.Container(
        height=200,
        width=1300,
        image_src='images/BackgroundEraser_20240615_145656905.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    upper = ft.Container(
        height=200,
        width=1300,
        offset=ft.Offset(y=0, x=-0.1),
        image_src='images/BackgroundEraser_20240615_145630019.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    frontal = ft.Container(
        height=200,
        width=1300,
        offset=ft.Offset(y=0, x=-0.1),
        image_src='images/BackgroundEraser_20240615_145608929.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    chute = ft.Container(
        height=200,
        width=1300,
        image_src='images/BackgroundEraser_20240615_145543810.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    joelhada = ft.Container(
        height=200,
        width=1300,
        image_src='images/BackgroundEraser_20240615_145517958.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )

    cotovelada = ft.Container(
        height=200,
        width=1300,
        image_src='images/BackgroundEraser_20240615_145454587.png',
        image_fit=ft.ImageFit.COVER,
        #scale=ft.Scale(scale=1),
        #animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
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

                    ft.Container(
                        image_src='images/BackgroundEraser_20240613_113828071.png',
                        image_fit=ft.ImageFit.FIT_HEIGHT,
                        image_opacity=0.5,
                        margin=0,
                        padding=20,
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
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='Muay Thai',
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color='amber'
                                ),
                                ft.Text(
                                    size=16,
                                    color='black',
                                    weight=ft.FontWeight.BOLD,
                                    value='''Essa arte marcial milenar, originária da Tailândia, é conhecida não apenas por sua eficácia em competições, mas também pelos inúmeros benefícios que traz para a saúde física e mental de seus praticantes. E quando treinada sob a orientação de um personal trainer especializado, os resultados podem ser ainda mais impressionantes.'''
                                ),
                                ft.Divider(),
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='O que é o Muay Thai?',
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color='amber'
                                ),
                                ft.Text(
                                    size=16,
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.BOLD,
                                    value='''Muay Thai, ou boxe tailandês, é uma modalidade que combina golpes com os punhos, cotovelos, joelhos e canelas, além de envolver técnicas de clinch (agarre). A prática regular desse esporte exige resistência, força, flexibilidade e coordenação motora, proporcionando um treino completo para o corpo.'''
                                ),
                                ft.Divider(),
                                ft.Text(
                                    text_align=ft.TextAlign.CENTER,
                                    value='Benefícios do Muay Thai para a Saúde',
                                    size=30,
                                    weight=ft.FontWeight.BOLD,



                                    color='amber'
                                ),
                                ft.Text(
                                    size=16,
                                    color='black',
                                    weight=ft.FontWeight.BOLD,
                                    value='''Melhora do Condicionamento Físico: O Muay Thai é um treino cardiovascular intenso que ajuda a melhorar a resistência e a capacidade pulmonar. Sessões regulares podem aumentar significativamente o nível de condicionamento físico geral.

Fortalecimento Muscular: Os movimentos repetitivos de chutes, socos e joelhadas trabalham todos os grupos musculares do corpo, fortalecendo-os e tonificando-os.

Perda de Peso: Devido à alta intensidade dos treinos, o Muay Thai é extremamente eficaz na queima de calorias. Uma hora de treino pode queimar até 1000 calorias, ajudando na perda de peso e na redução de gordura corporal.

Coordenação e Flexibilidade: A prática constante melhora a coordenação motora e a flexibilidade, reduzindo o risco de lesões no dia a dia.

Saúde Mental: Como qualquer atividade física, o Muay Thai libera endorfinas, hormônios que promovem a sensação de bem-estar e combatem o estresse e a ansiedade. Além disso, a disciplina e o foco necessários para o treino ajudam a melhorar a concentração e a autoestima.
'''
                                ),
                            ]
                        )
                    ),
                    ft.Stack(
                        controls=[
                            ft.Container(
                                height=600,
                                width=1300,
                                image_src='images/berg_andrade2.jpg',
                                image_fit=ft.ImageFit.COVER,
                                # offset=ft.Offset(y=0, x=0),
                                # animate_offset=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE_IN),
                                content=ft.Column(
                                    spacing=140,
                                    controls=[
                                        foto1,
                                        foto2,
                                        foto3,

                                    ]
                                )
                            ),


                        ]
                    ),
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
                        ft.Column(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=20, right=20, top=30, bottom=5),
                                    content=ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.CENTER,
                                        value='''O Muay Thai é conhecido por sua diversidade de técnicas e pela eficiência de seus golpes. Este tópico foi cuidadosamente desenvolvido para oferecer a você uma compreensão profunda e clara de cada movimento, desde os socos poderosos até as joelhadas e cotoveladas precisas.'''
                                    )
                                ),
                                ft.Container(
                                    height=500,
                                    width=1300,
                                    image_src='images/IMG-20220402-WA0035.jpg',
                                    image_fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Container(
                                    padding=20,
                                    content=ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.CENTER,
                                        value='''O que você encontrará neste tópico:

            Socos : Aprenda os diferentes tipos de socos, desde o jab até o cruzado, com instruções passo a passo e dicas para aprimorar sua técnica e potência.

            Chutes : Explore a variedade de chutes do Muay Thai, incluindo o chute circular, chute frontal e muito mais.

            Joelhadas : Descubra como aplicar joelhadas devastadoras, tanto em combates de curta distância quanto em clinch, aprimorando sua capacidade de ataque e defesa.

            Cotoveladas : As cotoveladas são algumas das técnicas mais letais do Muay Thai. Aqui, você aprenderá a usar essas armas com precisão e eficácia.

            Cada golpe é explicado com detalhes. Com este aplicativo, você terá acesso a um guia abrangente que facilitará o aprendizado e o aprimoramento das suas habilidades no Muay Thai.'''
                                    )
                                )
                            ]
                        ),
                        ft.Divider(),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                jab,
                                ft.Text(
                                    size=20,
                                    color=ft.colors.AMBER,
                                    italic=True,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    value='Jab do Muay Thai',
                                ),
                                ft.Container(
                                    padding=20,
                                    content=ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''                                              
            O soco mais básico do Muay Thai é o jab. Ele é desferido com a mão da frente, é rápido, tem como alvo do rosto do adversário.
            Embora o principal objetivo do jab seja o controle da distância e não ser o golpe de maior força, pode ter potencial de nocaute, dependendo da força e da técnica do lutador.'''
                                    )
                                )
                            ]
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    direto,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Direto do Muay Thai',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''                                                  
            O direto é o golpe de mãos mais forte do arsenal do lutador de Muay Thai, pois é desferido com a mão traseira, carregando enorme potência.
            Assim como o jab, o alvo principal do direto é o rosto do adversário e, se bem conectado, pode levar ao nocaute com facilidade.
            Outro possível alvo do direto é o torso do oponente, visando fígado.'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    cruzado,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Cruzado do Muay Thai',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''
            O soco cruzado tem como alvo a cabeça do oponente, sendo desferido de um ângulo lateral e visando mais precisamente o queixo.
            É um golpe bastante técnico, pode ser desferido com ambas as mãos (dianteira ou traseira) e possui grande potencial de derrubar o adversário.'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    upper,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Upper do Muay Thai',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''                                                  
            O gancho é um golpe desferido de baixo para cima e pode facilmente atravessar as defesas do lutador adversário.
            Seus alvos são tanto o rosto quanto o abdômen (fígado). Tem potência elevada e pode levar ao nocaute em ambos os casos quando bem encaixado, sendo eficiente principalmente a curtas e médias distâncias
            Além disso, assim como o cruzado, pode ser desferido tanto com a mão dianteira quanto com a mão traseira.'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    frontal,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Chutes Frontais (pernas traseira e dianteira)',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''
            O chute frontal, também conhecido como teep no Muay Thai, é uma técnica básica que busca criar e controlar a distância, podendo também ser usado para derrubar o adversário.
            Pode ser lançado com ambas as pernas (dianteira e traseira), tendo como alvo os quadris, o abdômen, o peito e também o rosto do oponente.'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(

                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    chute,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Chute Lateral do Muay Thai',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''                                                 
            O chute lateral do Muay Thai é considerado como a técnica de chute mais forte dentre as artes marciais.
            Extremamente potente, é desferido com a perna traseira e baseia-se na ideia de um machado atravessando lateralmente o oponente, seja para cortar sua perna, seu tronco ou sua cabeça.
            Sendo assim, possui três variações de altura: baixo (mirando a perna dianteira), médio (mirando tronco) e alto (mirando a cabeça do oponente).'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    joelhada,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Joelhadas do Muay Thai',
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            size=16,
                                            color=ft.colors.WHITE,
                                            italic=True,
                                            text_align=ft.TextAlign.JUSTIFY,
                                            value='''                                                    
            O Muay Thai possui diversas variações da joelhada. Esses golpes podem ter média, curta e longa distância, dependendo da técnica utilizada.
            A joelhada mais básica do Muay Thai é a joelhada direta, que pode ser executada com qualquer um dos joelhos, sendo elas a joelhada direta e a joelhada trocada.
            Como você já pode imagina, a joelhada direta é desferida com o joelho traseiro, enquanto a joelhada trocada é desferida com a perna dianteira obedecendo os mesmos princípios do chute trocado (troca de base para melhor gerar potência.
        Essas joelhadas visam atacar diretamente abdômen e plexo solar do oponente.'''
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Container(
                            padding=20,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    cotovelada,
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Cotoveladas do Muay Thai',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''Golpes de cotovelo são bastante característicos do Muay Thai e são usados em curta distância e/ou dentro do clinch.
Os principais golpes de cotovelo são:
Horizontal;
Ascendente;
Diagonal.''',
                                    ),
                                    ft.Divider(),
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='''Cotovelada Horizontal ou Lateral do Muay Thai''',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''A cotovelada horizontal ou lateral é um golpe visando o rosto do oponente, cortando horizontalmente, ou seja, traçando um vetor paralelo ao chão.
            Assim como vários outros golpes, pode ser executado tanto com o cotovelo dianteiro quanto com o traseiro.''',
                                    ),
                                    ft.Divider(),
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='''Cotovelada Ascendente do Muay Thai''',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''A cotovelada ascendente é um golpe executado de baixo para cima (como o soco gancho), traçando uma linha vertical, ou seja, perpendicular ao solo (ao oposto da cotovelada horizontal).
            Tem como alvo o queixo e rosto, buscando penetrar a guarda do adversário.
            Também pode ser executado com ambos os cotovelos.''',
                                    ),
                                    ft.Divider(),
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='''Cotovelada Diagonal do Muay Thai''',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''A cotovelada diagonal traça uma linha diagonal de cima para baixo, indo da esquerda para a direita ou da direita para a esquerda dependendo do lado com o qual foi desferido (lado esquerdo: cima-baixo, esquerda-direita; lado direito: cima-baixo, direita-esquerda), cruzando a frente do lutador.
            Seu alvo é a testa ou o supercílio do lutador adversário, com o objetivo de causar cortes e, consequentemente, sagramentos. ''',
                                    ),

                                ]
                            )
                        ),
                        ft.Divider(),
                        ft.Divider(color='transparent'),
                        ft.Container(
                            padding=20,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Regulamentos de Combate no Muay Thai',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''No Muay Thai, os combates são regidos por uma série de regulamentos que visam garantir a segurança dos praticantes e promover um jogo justo entre os lutadores. É importante que você esteja familiarizado com essas regras antes de entrar no ringue.''',
                                    ),
                                    ft.Divider(color='TRANSPARENT'),
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Técnicas Permitidas e Proibidas',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''No Muay Thai, você pode usar socos, chutes, joelhadas e cotoveladas para atacar seu oponente. No entanto, existem algumas técnicas que são proibidas, como golpes na nuca, virilha ou na parte de trás da cabeça.
                        Além disso, não são permitidos golpes abaixo da cintura, dedos nos olhos, mordidas ou qualquer outra conduta antiética que possa prejudicar o adversário. O descumprimento dessas regras pode resultar em punições, incluindo a desclassificação do lutador.''',
                                    ),
                                    ft.Divider(color='TRANSPARENT'),
                                    ft.Text(
                                        size=20,
                                        color=ft.colors.AMBER,
                                        italic=True,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        value='Uso de Cotovelos, Joelhos e Chutes',
                                    ),
                                    ft.Text(
                                        size=16,
                                        color=ft.colors.WHITE,
                                        italic=True,
                                        text_align=ft.TextAlign.JUSTIFY,
                                        value='''O Muay Thai é conhecido por seu uso único de cotovelos, joelhos e chutes. No entanto, existem regras específicas para o uso dessas técnicas.
                        Por exemplo, os cotovelos só são permitidos em combates profissionais, enquanto que em lutas amadoras, seu uso é proibido. Além disso, não é permitido atingir a cabeça do oponente com o joelho.
                        Os chutes também possuem algumas restrições. Não é permitido realizar chutes na coxa interna, bem como chutes em um adversário que esteja caído no chão.''',
                                    ),
                                    ft.Divider(),
                                ]
                            )
                        ),
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
                            height=1300,
                            width=1300,
                            image_src='images/fotopreto.jpg',
                            image_fit=ft.ImageFit.CONTAIN,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        color=ft.colors.AMBER,
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        value='Origem',
                                    ),
                                    ft.Divider(color='TRANSPARENT'),
                                    ft.Text(
                                        color=ft.colors.AMBER_200,
                                        size=16,

                                        value='''O Muay Thai tem sua origem na Tailândia, país localizado no sudeste asiático.

As raízes da civilização tailandesa datam dos séculos I e II a.C., quando povos originários da China migraram ao sul para as regiões que futuramente iriam compor o Vietnã, o Laos, Camboja, Mianmar e também a Tailândia.

As guerras eram nas fronteiras do então reino do Sião eram constantes e, na segunda metade do século XVI, os birmaneses ocuparam o território, transformando Aiutaia num estado dependente.

Pouco mais de uma década depois da invasão, a independência do Sião foi estabelecida.

É dentro desse contexto de guerras que encontramos as raízes do Muay Thai. As formas de combate corpo a corpo da região, usadas nos campos de batalha, foram se desenvolvendo e assumindo aspectos específicos das culturas que sobreviveram às guerras, embora ainda mantivessem semelhança.

Com isso, o Muay Boran, forma de combate dos antigos guerreiros siameses, evoluiu para o que hoje conhecemos como Muay Thai, assim como os birmaneses (povo da antiga Birmânia, hoje oficialmente conhecida como Myanmar) hoje possuem o Lethwei.

No futuro, os países europeus como Holanda e França entrariam em contato com a Tailândia, estabelecendo relações de comércio. Esse contato também teve efeito sobre o Muay Thai, uma vez que muito do boxe ocidental fora absorvido, influenciando também o sistema de regras do Muay Thai moderno.''',
                                    ),
                                    ft.Container(
                                        height=200,
                                        width=1300,
                                        image_src='images/thai_parana_promo.png',
                                        image_fit=ft.ImageFit.CONTAIN,
                                    )
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
    port = int(os.environ.get("PORT", 5000)) #para colocar no heroku
    ft.app(target=main, assets_dir='assets', port=port, view=ft.WEB_BROWSER) #para colocar no heroku

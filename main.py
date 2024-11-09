#video de referencia
#https://www.youtube.com/watch?v=rcMuTUpqUsU&t=2177s

import flet as ft 
from flet import colors 
from decimal import Decimal

icone_url = "/home/levs/Documentos/Calculadora/FAV02BW 100X95.png"
#favicon_url = "/home/levs/Documentos/Calculadora/icon.png"

botões = [
    
    {'operador' : 'AC', 'fonte': colors.BLACK, 'fundo': colors.ORANGE},
    {'operador' : '±', 'fonte': colors.BLACK, 'fundo': colors.ORANGE},
    {'operador' : '%', 'fonte': colors.BLACK, 'fundo': colors.ORANGE},
    {'operador' : '/', 'fonte': colors.WHITE, 'fundo': colors.PURPLE_ACCENT},
    {'operador' : '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '*', 'fonte': colors.WHITE, 'fundo': colors.PURPLE_ACCENT},
    {'operador' : '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '-', 'fonte': colors.WHITE, 'fundo': colors.PURPLE_ACCENT},
    {'operador' : '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '+', 'fonte': colors.WHITE, 'fundo': colors.PURPLE_ACCENT},
    {'operador' : ft.Image(src=icone_url, fit=ft.ImageFit.CONTAIN), 'fonte': colors.WHITE, 'fundo': colors.TRANSPARENT},
    {'operador' : '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador' : '=', 'fonte': colors.WHITE, 'fundo': colors.PURPLE_ACCENT},
    
]

#função principal que define a tela principal
def main(page: ft.Page):
    page.bgcolor = '#000' #background color
    page.window_resizable = False
    page.window_width = 250 #largura da janeja
    page.window_height = 350 #altura da janela
    page.title = 'Calculadora' #titulo da janela
    page.window_always_on_top = True #sobreposição sobre outras janelas
    #page.favicon = favicon_url
    
    result =ft.Text(value = '0' ,color = colors.WHITE , size=20) #variavel principal que exibe os resultados e valores digitados
    
    def calculate(operador, value_at):#função para concretizar o calculo
        
        try:
            
            value = eval(value_at)
            
            if operador == '%': #verifica se o operador digitado é porcentagem.
                value /= 100

            elif operador == '±': #verifica se o operador digitado é mais ou menos.
                value = -value   
        except:
            return 'ERROR'
        
        digits=min(abs(Decimal(value).as_tuple().exponent),5)
        
        return format(value, f'.{digits}f') #retorna o resultados dos calculos.
    
    def select(e): #função para ações do mouse
        value_at = result.value if result.value not in ('0' , 'ERROR') else '' #valor atual // mantem o numero inicial em zero(0) e não realiza a concatenação se nada for clicado
        value = e.control.content.value  #pega o operador dentro do conteiner de cada botão
        
        if value.isdigit():#verifica se o valor digitado é um numeral
            value = value_at + value #realiza a concatenação dos valores digitados
        elif value == 'AC':#se o operador 'AC' for precionado irá limpar os resultados (variavel result).
            value = '0' #ao limpar os resultados com o operador "AC", transforma o resultado em zero.
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'): #realiza a verificação se o ultimo operador digitado é um sinal.
                value_at = value_at[:-1]#substitui o operador caso digite outro (sem concatenação)
                
            value = value_at + value #realiza a concatenação dos numerais + os operadores(+ , - , * , /)
            
            if value [-1] in ('=', '%', '±'):#verifica se o ultimo valor digitado é um operador especial.
                value = calculate(operador=value[-1], value_at = value_at)
                
                
        result.value = value #atualiza o resuldado dos calculos para a variavel de exibição
        result.update() #atualiza a área de resultados a cada operação 
            
            
    #propriedades da área de exibição
    display = ft.Row(
        width = 250, #largura
        controls = [result],
        alignment = 'end', #alinhado ao final da área
    )
    
    # Criação dos botões da calculadora.
    btn = [
        ft.Container(
            content=ft.Text(value=btn['operador'], color=btn['fonte']) if isinstance(btn['operador'], str) else btn['operador'],
            alignment=ft.alignment.center,
            width=50,
            height=50,
            bgcolor=btn['fundo'],
            border_radius=100,
            on_click=select
        ) for btn in botões
    ]
    keyboard = ft.Row(
        width = 250,
        wrap = True,
        controls = btn,
        alignment = 'end'
    )
    
    page.add(display, keyboard)
    
    
    
ft.app(target = main)#chamada da função principal     
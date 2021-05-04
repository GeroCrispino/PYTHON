import PySimpleGUI as sg

def build():


    color_fondo = "#000000"
    fuente = ('Arial',10)
    ventana = {'size':(300,250), 'background_color':color_fondo, 'element_justification':'center'}
    botones = {'size':(30,2), 'button_color':'#E50707','font':fuente,'border_width':3,'focus':True}
    titulos = {'font':('Arial Black',15), 'background_color':color_fondo, 'text_color':'#ffffff'}


    # Layout
    layout = [
                [sg.Text(k='-TITULO-', text='Analisis de datos', **titulos)],
                [sg.Button(k='-BOT_FM-', button_text='Top 10 jugadores Argentinos en PES', pad=((0,0),(10,0)), **botones)],
                [sg.Button(k='-BOT_PAISES-', button_text='Top 20 Paises con mayor poblacion en Sudamerica y Caribe', pad=((0,0),(10,0)),**botones)],
                [sg.Button(k='-BOT_SALIR-', button_text='Salir', pad=((0,0),(25,0)), **botones)],
            ]

    window = sg.Window('Menu',layout,**ventana)
    return window
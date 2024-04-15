import requests
from tkinter import *

class HomeView:
    #Funcoes
    def button_calcular_rota_action():
        cidade_incial = (input_cidade_incial.get())
        cidade_final = (input_cidade_final.get())
        label_caminho_percorrido_resultado["text"] = "O caminho até "+cidade_incial+" saindo de "+cidade_final+" é:"
        #Necessário corrigir essa função do botão

    def centralizar_janela(window):
        window.update_idletasks()
        x = (window.winfo_screenwidth() - window.winfo_width()) // 2
        y = (window.winfo_screenheight() - (60 - window.winfo_height())) // 2
        window.geometry(f'{window.winfo_width()}x{window.winfo_height()}+{x}+{y}')

    #Estrutura
    janela = Tk()
    janela.title("RomeniaMaps")
    janela.geometry("993x960")
    janela.configure(bg="#306bac")
    centralizar_janela(janela)

    label_titulo = Label(janela, text="Escolha as cidades para busca do 'Caixeiro-Viajante':", bg="#306bac",foreground="white", font="Arial, 30")
    label_titulo.pack(anchor="center")

    label_cidade_incial = Label(janela, text="Cidade Inicial:", bg="#306bac",foreground="white", font="Arial, 13")
    label_cidade_incial.pack(anchor="center")
    input_cidade_incial = Entry(janela)
    input_cidade_incial.pack(anchor="center")

    label_cidade_final = Label(janela, text="Cidade Final:", bg="#306bac",foreground="white", font="Arial, 13")
    label_cidade_final.pack(anchor="center", pady=(10, 0))
    input_cidade_final = Entry(janela)
    input_cidade_final.pack(anchor="center")

    label_caminho_percorrido = Label(janela, text="Resultado rota:", bg="#306bac",foreground="white", font="Arial, 16")
    label_caminho_percorrido.pack(anchor="center", pady=(10, 0))
    label_caminho_percorrido_resultado = Label(janela, text="", width=70)
    label_caminho_percorrido_resultado.pack(anchor="center", pady=(0, 10))

    #Botao
    button_calcular_rota = Button(janela, text="Calcular rota",bg="#3CB371",foreground="white", command=button_calcular_rota_action, width=10, height=2)
    button_calcular_rota.pack(anchor="center",pady=(15, 15))

    #foto_mapa = PhotoImage(file="Assets/grafo_resultado.png")
    #mapa = Label(janela, image=foto_mapa)
    #mapa.pack()


    #Roda a janela
    janela.mainloop()

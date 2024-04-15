from tkinter import *

class HomeView:
    janela: 'Tk'
    input_nome_da_cidade_inicial: 'Entry'
    input_nome_da_cidade_final: 'Entry'
    label_caminho_percorrido_resultado: 'Label'

    def __init__(self):
        self.janela = Tk()
        self._definir_janela()

        self._criar_label(
            texto_de_exibicao = "Escolha as cidades para criar rota:", 
            cor_de_fundo_em_hex = "#306bac", 
            cor_do_texto = "white", 
            fonte = "Arial, 30"
        )

        self._criar_label(
            texto_de_exibicao = "Cidade Inicial:", 
            cor_de_fundo_em_hex = "#306bac", 
            cor_do_texto = "white", 
            fonte = "Arial, 13"
        )

        self.input_nome_da_cidade_inicial = self._criar_input_de_caixa_de_texto()

        self._criar_label(
            texto_de_exibicao = "Cidade Final:",
            cor_de_fundo_em_hex = "#306bac",
            cor_do_texto = "white",
            fonte = "Arial, 13",
            pady = (10, 0)
        )

        self.input_nome_da_cidade_final = self._criar_input_de_caixa_de_texto()

        self._criar_label(
            texto_de_exibicao = "Rota Gerada:",
            cor_de_fundo_em_hex = "#306bac",
            cor_do_texto = "white",
            fonte = "Arial, 16",
            pady = (10, 0)
        )

        self.label_caminho_percorrido_resultado = self._criar_label(
            texto_de_exibicao = "",
            cor_de_fundo_em_hex = "#3CB371",
            width = 70,
            pady = (0, 10)
        )

        self._criar_botao(
            self._action_calcular_rota,
            texto_de_exibicao = "Calcular rota",
            cor_de_fundo_em_hex = "#3CB371",
            cor_do_texto = "white",
            width = 10,
            altura = 2,
            pady = (15, 15)
        )

        self._renderizar_janela()

    # Método privado
    def _action_calcular_rota(self):
        nome_da_cidade_inicial: str = (self.input_nome_da_cidade_inicial.get())
        nome_da_cidade_final: str = (self.input_nome_da_cidade_final.get())

        self.label_caminho_percorrido_resultado["text"] = f"O caminho de {nome_da_cidade_inicial} saindo de {nome_da_cidade_final} é:"

    # Método privado
    def _criar_botao(self,
                      acao_ao_clicar: callable,
                      texto_de_exibicao: str = "",
                      cor_de_fundo_em_hex: str = "#3CB371",
                      cor_do_texto: str = "white",
                      width: int = 10,
                      altura: int = 2,
                      pady: tuple[int, int] = (0, 0)):
        novo_botao: 'Button' = Button(
            self.janela,
            command = acao_ao_clicar,
            text = texto_de_exibicao,
            bg = cor_de_fundo_em_hex,
            foreground = cor_do_texto,
            width = width,
            height = altura
        )

        novo_botao.pack(anchor = "center", pady = pady)

        return novo_botao

    # Método privado
    def _criar_label(self,
                     texto_de_exibicao: str = "", 
                     cor_de_fundo_em_hex: str = "#306bac", 
                     cor_do_texto: str = "white", 
                     fonte: str = "Arial",
                     width: int = 100,
                     pady: tuple[int, int] = (0, 0)) -> 'Label':
        nova_label: 'Label' = Label(
            self.janela,
            text = texto_de_exibicao,
            bg = cor_de_fundo_em_hex,
            foreground = cor_do_texto,
            font = fonte,
            width = width
        )

        nova_label.pack(anchor = "center", pady = pady)

        return nova_label
    
    # Método privado
    def _criar_input_de_caixa_de_texto(self) -> 'Entry':
        novo_input: 'Entry' = Entry(self.janela)
        novo_input.pack(anchor = "center")

        return novo_input

    # Método privado
    def _definir_janela(self):
        self.janela.title("RomeniaMaps")
        self.janela.geometry("993x960")
        self.janela.configure(bg = "#306bac")
        self._centralizar_janela()

    # Método privado
    def _centralizar_janela(self):
        self.janela.update_idletasks()
        x = (self.janela.winfo_screenwidth() - self.janela.winfo_width()) // 2
        y = (self.janela.winfo_screenheight() - (60 - self.janela.winfo_height())) // 2
        self.janela.geometry(f'{self.janela.winfo_width()}x{self.janela.winfo_height()}+{x}+{y}')

    def _renderizar_janela(self):
        self.janela.mainloop()

    #foto_mapa = PhotoImage(file="Assets/grafo_resultado.png")
    #mapa = Label(janela, image=foto_mapa)
    #mapa.pack()

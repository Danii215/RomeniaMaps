from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkFrame, set_appearance_mode, set_default_color_theme
from Views.View import View

class Home(View):
    """
    A classe Home representa a interface gráfica da aplicação, que permite ao usuário interagir
    para selecionar as cidades inicial e final para calcular uma rota.

    Atributos Públicos
    ------------------
    nome_da_cidade_inicial : str
        O nome da cidade inicial selecionada pelo usuário.
    nome_da_cidade_final : str
        O nome da cidade final selecionada pelo usuário.

    Atributos Privados
    ------------------
    _janela : 'CTk'
        A instância da classe `CTk` que representa a janela principal da interface gráfica.
    _input_nome_da_cidade_inicial : 'CTkEntry'
        O campo de entrada onde o usuário pode inserir o nome da cidade inicial.
    _input_nome_da_cidade_final : 'CTkEntry'
        O campo de entrada onde o usuário pode inserir o nome da cidade final.
    _sidebar_lateral : 'CTkFrame'
        O painel lateral onde estão localizados os elementos da interface, como rótulos e botões.
    """
    # Atributos Públicos
    nome_da_cidade_inicial: str
    nome_da_cidade_final: str
    # Atributos Privados
    _janela: 'CTk'
    _input_nome_da_cidade_inicial: 'CTkEntry'
    _input_nome_da_cidade_final: 'CTkEntry'
    _sidebar_lateral: 'CTkFrame'

    def __init__(self):
        """
        Inicializa a aplicação e configura a interface gráfica.

        Este método cria uma instância da classe `CTk` para a janela principal da aplicação e define sua aparência.
        Em seguida, cria uma barra lateral esquerda na janela principal e adiciona diversos elementos de interface,
        como rótulos de texto, campos de entrada e botão de ação. O botão permite ao usuário confirmar a seleção
        das cidades inicial e final para calcular a rota. Por fim, renderiza a janela da interface gráfica.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self._janela = CTk()
        self._definir_janela()

        self._sidebar_lateral = self._criar_sidebar_lateral("left", "y", True)

        self._criar_label(
            master=self._sidebar_lateral,
            texto_de_exibicao = "Escolha as cidades para criar rota:", 
            cor_do_texto = "white", 
            fonte = ("Arial", 20),
            padx = (30, 30),
            pady = (10, 10)
        )

        self._criar_label(
            master=self._sidebar_lateral,
            texto_de_exibicao = "Cidade Inicial:", 
            cor_do_texto = "white", 
            fonte = ("Arial", 13),
            padx = (10, 0),
            anchor = "w"
        )

        self._input_nome_da_cidade_inicial = self._criar_input_de_caixa_de_texto()

        self._criar_label(
            master=self._sidebar_lateral,
            texto_de_exibicao = "Cidade Final:",
            cor_do_texto = "white",
            fonte = ("Arial", 13),
            pady = (10, 0),
            padx = (10, 0),
            anchor = "w"
        )

        self._input_nome_da_cidade_final = self._criar_input_de_caixa_de_texto()

        self._criar_botao(
            self._sidebar_lateral,
            self._action_definir_nomes_de_cidades,
            texto_de_exibicao = "Calcular rota",
            cor_do_texto = "white",
            altura = 32,
            pady = (10, 0),
            padx = (10, 10)
        )

        self._renderizar_janela()

    # Método privado
    def _action_definir_nomes_de_cidades(self):
        """
        Obtém os nomes das cidades inicial e final inseridos nos campos de entrada da interface gráfica.

        Este método é chamado quando o botão de confirmação é clicado. Ele recupera os nomes das cidades inicial
        e final inseridos nos campos de entrada da interface gráfica e os armazena nos atributos correspondentes
        da classe. Em seguida, fecha a janela da interface gráfica.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self.nome_da_cidade_inicial: str = self._input_nome_da_cidade_inicial.get()
        self.nome_da_cidade_final: str = self._input_nome_da_cidade_final.get()

        self._janela.quit()

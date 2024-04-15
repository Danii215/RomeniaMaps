from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkFrame, set_appearance_mode, set_default_color_theme

class View:
    """
    A classe View é uma classe base que fornece funcionalidades comuns para as visualizações da interface gráfica.
    Ela contém um atributo protegido _janela, que representa a janela principal da interface gráfica.

    Atributos Protegidos
    --------------------
    _janela : 'CTk'
        A janela principal da interface gráfica, representada por um objeto da classe CTk.
    """
    _janela: 'CTk'

    # Método privado
    def _criar_botao(self,
                  master: CTk | CTkFrame,
                  acao_ao_clicar: callable,
                  texto_de_exibicao: str = "",
                  cor_do_texto: str = "white",
                  width: int = 10,
                  altura: int = 2,
                  pady: tuple[int, int] = (0, 0),
                  padx: tuple[int, int] = (0, 0)) -> 'CTkButton':
        """
        Cria e retorna um novo widget de botão.

        Este método cria um novo widget de botão com o texto especificado, cor do texto, largura, altura e
        ação a ser executada quando o botão é clicado. Em seguida, adiciona o widget à barra lateral da interface gráfica.

        Parâmetros
        ----------
        master : CTk | CTkFrame
            O componente pai deste widget.
        acao_ao_clicar : callable
            A função ou método que será chamado quando o botão for clicado.
        texto_de_exibicao : str, opcional
            O texto a ser exibido no widget de botão. O padrão é uma string vazia.
        cor_do_texto : str, opcional
            A cor do texto a ser exibido no widget de botão. O padrão é "white".
        width : int, opcional
            A largura do widget de botão. O padrão é 10.
        altura : int, opcional
            A altura do widget de botão. O padrão é 2.
        pady : tuple[int, int], opcional
            O preenchimento vertical (espaço) a ser adicionado ao redor do widget de botão. 
            O padrão é (0, 0).
        padx : tuple[int, int], opcional
            O preenchimento horizontal (espaço) a ser adicionado ao redor do widget de botão. 
            O padrão é (0, 0).

        Retorna
        -------
        CTkButton
            O objeto do tipo CTkButton que representa o widget de botão criado.
        """
        novo_botao: 'CTkButton' = CTkButton(
            master=master,
            command=acao_ao_clicar,
            text=texto_de_exibicao,
            text_color=cor_do_texto,
            width=width,
            height=altura,
        )

        novo_botao.pack(anchor="center", fill="x", pady=pady, padx=padx)

        return novo_botao

    # Método privado
    def _criar_label(self,
                 master: CTk | CTkFrame,
                 texto_de_exibicao: str = "", 
                 cor_do_texto: str = "white", 
                 fonte: tuple[str, int] = ("Arial", 16),
                 width: int = 100,
                 padx: tuple[int, int] = (0, 0),
                 pady: tuple[int, int] = (0, 0),
                 anchor: str = "center") -> 'CTkLabel':
        """
        Cria e retorna um novo widget de label.

        Este método cria um novo widget de label com o texto especificado, cor do texto, fonte, largura e
        posicionamento definidos. Em seguida, adiciona o widget à barra lateral da interface gráfica.

        Parâmetros
        ----------
        master : CTk | CTkFrame
            O componente pai deste widget.
        texto_de_exibicao : str, opcional
            O texto a ser exibido no widget de label. O padrão é uma string vazia.
        cor_do_texto : str, opcional
            A cor do texto a ser exibido no widget de label. O padrão é "white".
        fonte : tuple[str, int], opcional
            A fonte a ser usada para o texto no widget de label, no formato (nome_da_fonte, tamanho_da_fonte).
            O padrão é ("Arial", 16).
        width : int, opcional
            A largura do widget de label. O padrão é 100.
        padx : tuple[int, int], opcional
            O preenchimento horizontal (espaço) a ser adicionado ao redor do widget de label. 
            O padrão é (0, 0).
        pady : tuple[int, int], opcional
            O preenchimento vertical (espaço) a ser adicionado ao redor do widget de label. 
            O padrão é (0, 0).
        anchor : str, opcional
            A âncora para posicionar o widget de label dentro do seu espaço disponível. 
            O padrão é "center".

        Retorna
        -------
        CTkLabel
            O objeto do tipo CTkLabel que representa o widget de label criado.
        """
        nova_label: 'CTkLabel' = CTkLabel(
            master=master,
            text=texto_de_exibicao,
            text_color=cor_do_texto,
            font=fonte,
            width=width
        )

        nova_label.pack(anchor=anchor, padx=padx, pady=pady)

        return nova_label

    # Método privado
    def _criar_input_de_caixa_de_texto(self) -> 'CTkEntry':
        """
        Cria e retorna um novo widget de entrada de caixa de texto.

        Este método cria um novo widget de entrada de caixa de texto e o adiciona à barra lateral da interface gráfica.
        O widget criado é retornado para que outros métodos possam interagir com ele, se necessário.

        Retorna
        -------
        CTkEntry
            O objeto do tipo CTkEntry que representa o widget de entrada de caixa de texto criado.
        """
        novo_input: 'CTkEntry' = CTkEntry(master=self._sidebar_lateral)
        novo_input.pack(anchor="w", fill="x", padx=(10, 10))

        return novo_input

    # Método privado
    def _criar_sidebar_lateral(self, lado: str = "top", preencher: str = "y", expandir: bool = False) -> 'CTkFrame':
        """
        Cria e retorna um novo frame para a barra lateral.

        Este método cria um novo frame para servir como a barra lateral da interface gráfica. O lado e as
        configurações de preenchimento e expansão podem ser personalizados. O frame criado é retornado para
        que outros widgets possam ser adicionados a ele.

        Parâmetros
        ----------
        lado : str, opcional
            O lado onde o frame será colocado. Pode ser "top", "bottom", "left" ou "right". O padrão é "top".
        preencher : str, opcional
            A direção na qual o frame deve preencher o espaço disponível. Pode ser "x", "y" ou "both". O padrão é "y".
        expandir : bool, opcional
            Indica se o frame deve expandir para ocupar todo o espaço disponível. O padrão é False.

        Retorna
        -------
        CTkFrame
            O objeto do tipo CTkFrame que representa o novo frame criado.
        """
        novo_frame: 'CTkFrame' = CTkFrame(master=self._janela, fg_color="#272727")
        novo_frame.pack(anchor="center", side=lado, fill=preencher, expand=expandir)

        return novo_frame

    # Método privado
    def _definir_janela(self) -> None:
        """
        Define as configurações iniciais da janela gráfica.

        Este método configura a aparência e o tamanho inicial da janela gráfica. Ele define o título da janela,
        o modo de aparência e o tema de cores padrão. Além disso, define as dimensões iniciais da janela e a
        centraliza na tela.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self._janela.title("RomeniaMaps")

        set_appearance_mode("Dark")
        set_default_color_theme("dark-blue")

        self._janela.geometry("400x800")
        
        self._centralizar_janela()

    # Método privado
    def _centralizar_janela(self) -> None:
        """
        Centraliza a posição da janela gráfica na tela.

        Este método calcula as coordenadas necessárias para centralizar a janela gráfica na tela do dispositivo.
        Ele utiliza informações sobre a largura e a altura da janela e da tela para calcular a posição central
        adequada e, em seguida, atualiza a geometria da janela para refletir essa posição centralizada.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self._janela.update_idletasks()

        width_da_janela: int = self._janela.winfo_width()
        height_da_janela: int = self._janela.winfo_height()

        width_da_tela: int = self._janela.winfo_screenwidth()
        height_da_tela: int = self._janela.winfo_screenheight()

        x_pra_centralizar = (width_da_tela - width_da_janela) // 2
        y_pra_centralizar = (height_da_tela - height_da_janela) // 2

        self._janela.geometry(f"+{x_pra_centralizar}+{y_pra_centralizar}")

    # Método privado
    def _renderizar_janela(self) -> None:
        """
        Inicia o loop principal de renderização da janela gráfica.

        Este método inicia o loop principal de renderização da janela gráfica utilizando a biblioteca tkinter.
        Durante esse loop, a interface gráfica permanece ativa e responde a eventos do usuário, como cliques
        de mouse e pressionamentos de tecla.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self._janela.mainloop()
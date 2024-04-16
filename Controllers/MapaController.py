from json import loads, JSONDecodeError

class MapaController:
    # Metódo privado
    @staticmethod
    def _pegar_nomes_de_todas_as_cidades_do_json(caminho_pro_json: str) -> list[str]:
        """
        Lê um arquivo JSON, analisa seu conteúdo em um dicionário Python e retorna uma lista de 
        strings consistindo das primeiras chaves imediatas do objeto JSON analisado.

        Este método é adaptado para trabalhar com JSONs específicos que seguem um formato compatível
        com o projeto em questão. No contexto deste projeto, espera-se que as primeiras chaves imediatas
        do objeto JSON sejam os nomes de todas as cidades relevantes para o estudo.

        Retorna uma lista contendo os nomes de todas as cidades presentes no JSON.

        Parâmetros
        ----------
        caminho_pro_json : str
            O caminho para o arquivo JSON que comporta as relações entre cidades.

        Retorna
        -------
        list[str]
            Uma lista contendo os nomes de todas as cidades presentes no JSON.
        """
        arquivo_legivel: dict[str, any] = MapaController._converter_json_em_dicionario(caminho_pro_json)
        
        lista_de_cidades: list[str] = list(arquivo_legivel.keys())
        
        return lista_de_cidades

    # Metódo privado
    @staticmethod
    def _converter_json_em_dicionario(caminho_pro_json: str) -> dict[str, any]:
        """
        Lê um arquivo JSON e o transforma em texto. Em seguida, converte novamente para um dicionário
        Python, a fim de ser usado em lógicas internas relacionadas à classe Mapa.

        Esse método pode levantar erros do tipo JSONDecodeError ou ValueError, dependendo do procedimento 
        de conversão.

        Retorna um dicionário que representa o conteúdo do arquivo JSON.

        Parâmetros
        ----------
        caminho_pro_json : str
            O caminho para o arquivo JSON que contém as relações entre cidades.

        Retorna
        -------
        dict[str, any]
            Um dicionário Python que representa o conteúdo do arquivo JSON.

        Lança
        ------
        JSONDecodeError
            Se o conteúdo do JSON for inválido.
        ValueError
            Se o objeto JSON não foi corretamente renderizado.
        """
        json_em_texto: str = MapaController._converter_json_em_texto(caminho_pro_json)
        
        try:
            arquivo_legivel: dict[str] = loads(json_em_texto)

        except JSONDecodeError as erro_de_decodificacao:
            raise JSONDecodeError("Conteúdo de JSON inválido.") from erro_de_decodificacao
        
        if not isinstance(arquivo_legivel, dict):
            raise ValueError("Objeto JSON não foi corretamente renderizado.")

        return arquivo_legivel

    # Metódo privado
    @staticmethod
    def _converter_json_em_texto(caminho_pro_json: str) -> str:
        """
        Lê um arquivo JSON e o transforma em texto.

        Pode levantar erros de FileNotFoundError se o arquivo passado não for encontrado ou se houver
        falha de leitura, por motivos quaisquer.

        Parâmetros
        ----------
        caminho_pro_json : str
            O caminho para o arquivo JSON que comporta as relações entre cidades.

        Retorna
        -------
        str
            O conteúdo do arquivo JSON como uma string.

        Lança
        ------
        ValueError
            Se ocorrer um erro ao abrir ou ler o arquivo JSON.
        FileNotFoundError
            Se o arquivo não for encontrado.
        """
        try:
            with open(caminho_pro_json, 'r') as arquivo:
                arquivo_em_texto: str = arquivo.read()

        except FileNotFoundError as erro_de_caminho_nao_encontrado:
            raise FileNotFoundError("Arquivo não encontrado.") from erro_de_caminho_nao_encontrado

        except Exception as excecao_generica:
            raise ValueError("Erro de leitura.") from excecao_generica

        return arquivo_em_texto

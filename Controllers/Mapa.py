from json import loads, JSONDecodeError
from Controllers.Cidade import Cidade

class Mapa:
    """
    A classe Mapa é a estrutura de dados que abstrai as conexões entre cidades, bem como suas cidades vizinhas,
    e as distâncias entre elas. É a classe responsável por organizar o nome de cada cidade e suas relações entre si.

    Atributos Públicos
    ------------------
    caminho_pro_json : str
        O caminho para o arquivo JSON que contém as informações sobre as conexões entre as cidades.
        Por padrão, é definido como "Assets/mapa_padrao.json".
    lista_de_nomes_de_cidades : list[str]
        Uma lista contendo os nomes de todas as cidades presentes no mapa.
    todas_as_cidades : dict[str, 'Cidade']
        Um dicionário que mapeia o nome de cada cidade para sua instância correspondente da classe `Cidade`.
        Por padrão, é um dicionário vazio.
    """
    caminho_pro_json: str = "Assets/mapa_padrao.json"
    lista_de_nomes_de_cidades: list[str]
    todas_as_cidades: dict[str, 'Cidade'] = {}

    def __init__(self, caminho_pro_json: str = "") -> None:
        """
        Construtor da classe Mapa.

        Este método inicializa uma instância da classe Mapa. Se um caminho para um arquivo JSON for fornecido,
        o mapa correspondente é carregado a partir desse arquivo. Se nenhum caminho for fornecido, o mapa 
        padrão da Romênia é importado.

        Parâmetros
        ----------
        caminho_pro_json : str, opcional
            O caminho para o JSON correspondente ao Mapa que o usuário deseja calcular rotas. Deixar vazio 
            importa automaticamente o JSON do mapa da Romênia, placeholder da aplicação.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        if caminho_pro_json:
            self.caminho_pro_json = caminho_pro_json

        self.lista_de_nomes_de_cidades = Mapa._pegar_nomes_de_todas_as_cidades_do_json(self.caminho_pro_json)

        self._definir_todas_as_cidades()
        self._relacionar_todos_os_vizinhos()
        self._aplicar_coordenadas_em_cada_cidade()

    def pegar_cidade_pelo_nome(self, nome: str) -> 'Cidade':
        """
        Retorna um objeto do tipo Cidade correspondente ao nome fornecido.

        Este método capitaliza automaticamente o nome antes de procurar a cidade correspondente.

        Parâmetros
        ----------
        nome : str
            O nome da cidade a ser retornada.

        Retorna
        -------
        Cidade
            O objeto do tipo Cidade correspondente ao nome fornecido.
        """
        cidade_pelo_nome: 'Cidade' = self.todas_as_cidades[nome.title()]

        return cidade_pelo_nome
    
    # Metódo privado
    def _definir_todas_as_cidades(self) -> None:
        """
        Separa e instancia todas as cidades determinadas pelo JSON passado para a instância atual. 
        Pelo padrão da aplicação, seriam todas as primeiras chaves imediatas do JSON.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        for nome_de_cidade in self.lista_de_nomes_de_cidades:
            self.todas_as_cidades[nome_de_cidade] = Cidade(nome_de_cidade)

    # Metódo privado
    def _relacionar_todos_os_vizinhos(self) -> None:
        """
        Aplica relação de vizinhança para todas as cidades definidas na instância atual.

        Como determinado no JSON, as cidades possuem outras cidades, vizinhas. Esse é o método
        responsável por estabelecer, de acordo com a lógica necessária para a aplicação, a
        estrutura de dados correspondente à esse conceito.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        cidades_em_dicionario: dict[str, object] = Mapa._converter_json_em_dicionario(self.caminho_pro_json)

        for essa_cidade in self.todas_as_cidades:
            for nome_de_vizinho in cidades_em_dicionario[essa_cidade]["Vizinhos"]:
                cidade_avaliada: Cidade = self.todas_as_cidades[essa_cidade]
                cidade_vizinha: Cidade = self.todas_as_cidades[nome_de_vizinho]
                distancia_ate_vizinha: int = cidades_em_dicionario[cidade_avaliada.nome]["Vizinhos"][nome_de_vizinho]
                
                Cidade.definir_vizinhos(cidade_avaliada, cidade_vizinha, distancia_ate_vizinha)

    # Metódo privado
    def _aplicar_coordenadas_em_cada_cidade(self) -> None:
        """
        Aplica coordenadas para todas as cidades definidas na instância atual.

        Este método itera sobre todas as cidades definidas na instância atual e aplica coordenadas 
        a cada uma delas. Se uma cidade não tiver coordenadas definidas no JSON, são aplicadas 
        coordenadas padrão de {x: 0.0, y: 0.0}.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        cidades_em_dicionario: dict[str, object] = Mapa._converter_json_em_dicionario(self.caminho_pro_json)

        for essa_cidade in self.todas_as_cidades:
            try:
                coordenadas: dict[str, float] = cidades_em_dicionario[essa_cidade]["Coordenada"]
            except KeyError:
                coordenadas = {"x": 0.0, "y": 0.0}

            Cidade.definir_coordenadas(self.todas_as_cidades[essa_cidade], coordenadas)


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
        arquivo_legivel: dict[str, any] = Mapa._converter_json_em_dicionario(caminho_pro_json)
        
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
        json_em_texto: str = Mapa._converter_json_em_texto(caminho_pro_json)
        
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

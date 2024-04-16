from Models.Cidade import Cidade
from Controllers.MapaController import MapaController
from Controllers.CidadeController import CidadeController
from Exceptions.CidadeNaoEncontradaError import CidadeNaoEncontradaError

class Mapa:
    """
    A classe Mapa é a estrutura de dados que abstrai as conexões entre
    cidades, bem como suas cidades vizinhas, e as distâncias entre elas.
    É a classe responsável em organizar o nome de cada cidade e suas
    relações entre si.
    """

    caminho_pro_json: str = "Assets/Json/mapa_padrao.json"
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

        self.lista_de_nomes_de_cidades = MapaController._pegar_nomes_de_todas_as_cidades_do_json(self.caminho_pro_json)

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

        Lança
        ------
        CidadeNaoEncontradaError
            Se a cidade especificada não for encontrada no mapa.
        """
        try:
            cidade_pelo_nome: 'Cidade' = self.todas_as_cidades[nome.title()]
            return cidade_pelo_nome
        except KeyError:
            raise CidadeNaoEncontradaError(f"A cidade '{nome}' não foi encontrada no mapa.")
    
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
        cidades_em_dicionario: dict[str, object] = MapaController._converter_json_em_dicionario(self.caminho_pro_json)

        for essa_cidade in self.todas_as_cidades:
            for nome_de_vizinho in cidades_em_dicionario[essa_cidade]["Vizinhos"]:
                cidade_avaliada: Cidade = self.todas_as_cidades[essa_cidade]
                cidade_vizinha: Cidade = self.todas_as_cidades[nome_de_vizinho]
                distancia_ate_vizinha: int = cidades_em_dicionario[cidade_avaliada.nome]["Vizinhos"][nome_de_vizinho]
                
                CidadeController.definir_vizinhos(cidade_avaliada, cidade_vizinha, distancia_ate_vizinha)

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
        cidades_em_dicionario: dict[str, object] = MapaController._converter_json_em_dicionario(self.caminho_pro_json)

        for essa_cidade in self.todas_as_cidades:
            try:
                coordenadas: dict[str, float] = cidades_em_dicionario[essa_cidade]["Coordenada"]
            except KeyError:
                coordenadas = {"x": 0.0, "y": 0.0}

            CidadeController.definir_coordenadas(self.todas_as_cidades[essa_cidade], coordenadas)

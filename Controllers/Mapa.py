import json
from typing import Dict, List
from Controllers.Cidade import Cidade

class Mapa:
    """
    A classe Mapa é a estrutura de dados que abstrai as conexões entre
    cidades, bem como suas cidades vizinhas, e as distâncias entre elas.
    É a classe responsável em organizar o nome de cada cidade e suas
    relações entre si.

    Em teoria, todos os métodos desta classe são privados.
    :TODO: Documentar corretamente uso de métodos privados nesta e outras
    classes.
    """

    caminho_pro_json: str = "Assets/mapa_padrao.json"
    lista_de_nomes_de_cidades: List[str]
    cidades_em_dicionario: Dict[str, object]
    todas_as_cidades: Dict[str, 'Cidade'] = {}

    def __init__(self, caminho_pro_json: str = "") -> None:
        """
        Construtor da classe Mapa.

        :param caminho_pro_json: O caminho para o JSON correspondente ao Mapa que o usuário desejar
        calcular rotas. Deixar vazio importa automaticamente o JSON do mapa da Romênia, placeholder
        da aplicação.
        :type caminho_pro_json: str
        :return: None
        """
        if caminho_pro_json: 
            self.caminho_pro_json = caminho_pro_json

        self.lista_de_nomes_de_cidades = Mapa.pegar_nomes_de_todas_as_cidades_do_json(self.caminho_pro_json)
        self.cidades_em_dicionario = Mapa.converter_json_em_dicionario(self.caminho_pro_json)
        self.definir_todas_as_cidades()
        self.relacionar_todos_os_vizinhos()

    def definir_todas_as_cidades(self) -> None:
        """
        Separa e instancia todas as cidades determinadas pelo JSON passado para a instância atual. 
        Pelo padrão da aplicação, seria todas as primeiras chaves imediatas do JSON.

        :return: None
        """
        for nome_de_cidade in self.lista_de_nomes_de_cidades:
            self.todas_as_cidades[nome_de_cidade] = Cidade(nome_de_cidade)

    def relacionar_todos_os_vizinhos(self) -> None:
        """
        Aplica relação de vizinhança para todas as cidades definidas na instância atual.

        Como determinado no JSON, as cidades possuem outras cidades, vizinhas. Esse é o método
        responsável por estabelecer, de acordo com a lógica necessária para a aplicação, a
        estrutura de dados correspondente à esse conceito.

        :return: None
        """
        for essa_cidade in self.todas_as_cidades:
            for nome_de_vizinho in self.cidades_em_dicionario[essa_cidade]:
                cidade_avaliada: Cidade = self.todas_as_cidades[essa_cidade]
                cidade_vizinha: Cidade = self.todas_as_cidades[nome_de_vizinho]
                distancia_ate_vizinha: int = self.cidades_em_dicionario[cidade_avaliada.nome][nome_de_vizinho]
                
                Cidade.definir_vizinhos(cidade_avaliada, cidade_vizinha, distancia_ate_vizinha)

    @staticmethod
    def pegar_nomes_de_todas_as_cidades_do_json(caminho_pro_json: str) -> List[str]:
        """
        Lê um arquivo JSON, analisa seu conteúdo em um dicionário Python e retorna uma lista de 
        strings consistindo das primeiras chaves imediatas do objeto JSON analisado.

        No caso específico deste projeto, é adaptado pra receber JSONs específicos compatíveis
        com o projeto, em que as primeiras chaves imediatas desse objeto devem ser o nome de todas
        as cidades do contexto à ser estudado.

        :param caminho_pro_json: O caminho para o arquivo JSON que comporta as relações entre
        cidades.
        :type caminho_pro_json: str
        :return: List[str]
        """
        arquivo_legivel: Dict[str, any] = Mapa.converter_json_em_dicionario(caminho_pro_json)
        
        lista_de_cidades: List[str] = list(arquivo_legivel.keys())
        
        return lista_de_cidades

    @staticmethod
    def converter_json_em_dicionario(caminho_pro_json: str) -> Dict[str, any]:
        """
        Lê um arquivo JSON e o transforma em texto. Em seguida, converte novamente para um dicionário
        Python, à fim de ser usado em lógicas internas relacionadas à classe Mapa.

        Pode levantar erros de JSONDecodeError ou ValueError à depender do procedimento de conversão.

        :param caminho_pro_json: O caminho para o arquivo JSON que comporta as relações entre cidades.
        :type caminho_pro_json: str
        :return: Dict[str, any]
        """
        json_em_texto: str = Mapa.converter_json_em_texto(caminho_pro_json)
        
        try:
            arquivo_legivel: Dict[str] = json.loads(json_em_texto)

        except json.JSONDecodeError as erro_de_decodificacao:
            raise ValueError("Conteúdo de JSON inválido.") from erro_de_decodificacao
        
        if not isinstance(arquivo_legivel, dict):
            raise ValueError("Objeto JSON não foi corretamente renderizado.")

        return arquivo_legivel

    @staticmethod
    def converter_json_em_texto(caminho_pro_json: str) -> str:
        """
        Lê um arquivo JSON e o transforma em texto.

        Pode levantar erros de FileNotFoundError se o arquivo passado não for encontrado ou se houver
        falha de leitura, por motivos quaisquer.

        :param caminho_pro_json: O caminho para o arquivo JSON que comporta as relações entre cidades.
        :type caminho_pro_json: str
        :return: str
        """
        try:
            with open(caminho_pro_json, 'r') as arquivo:
                arquivo_em_texto: str = arquivo.read()

        except FileNotFoundError as erro_de_caminho_nao_encontrado:
            raise ValueError("Arquivo não encontrado.") from erro_de_caminho_nao_encontrado

        except Exception as excecao_generica:
            raise ValueError("Erro de leitura.") from excecao_generica

        return arquivo_em_texto
    
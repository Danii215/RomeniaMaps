class Cidade:
    """
    A classe Cidade representa de forma abstrata, uma
    instância de um ponto no mapa, com nome, cidades 
    vizinhas, e as distâncias até elas. Armazena também
    as coordenadas dessa Cidade, pra melhor visualização
    em um gráfico, caso esse dado seja fornecido 
    corretamente.
    """

    nome: str
    vizinhas: dict[str, int]
    coordenadas: dict[str, float]

    def __init__(self, nome: str) -> None:
        """
        Construtor da classe Cidade.

        Este método inicializa uma instância da classe Cidade com o nome fornecido, com a primeira letra de cada palavra 
        em maiúscula e as demais em minúscula.

        Parâmetros
        ----------
        nome : str
            O nome da cidade que será atribuído à instância de Cidade.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self.nome = nome.title()
        self.vizinhas = {}

    def __str__(self) -> str:
        """
        Retorna uma representação em string da instância de Cidade.

        Esta representação inclui o nome da cidade e uma lista de suas cidades vizinhas, 
        com as respectivas distâncias em quilômetros.

        Retorna
        -------
        str
            Uma representação em string da instância de Cidade.
        """
        vizinhas_str = ', '.join(f"{cidade.nome if isinstance(cidade, Cidade) else cidade} ({distancia} km)" for cidade, distancia in self.vizinhas.items())
        return f"A cidade {self.nome} possui essas vizinhas: {vizinhas_str}"

    def distancia_de_vizinho(self, qual_vizinho: str) -> int:
        """
        Retorna a distância de uma cidade até um vizinho especificado.

        Este método retorna a distância em quilômetros de uma cidade até um vizinho especificado.

        Parâmetros
        ----------
        qual_vizinho : str
            O nome do vizinho da cidade para o qual deseja-se obter a distância.

        Retorna
        -------
        int
            A distância em quilômetros da cidade até o vizinho especificado.
        """
        return self.vizinhas[qual_vizinho]
    
    @staticmethod
    def definir_vizinhos(vizinhoA: 'Cidade', vizinhoB: 'Cidade', distancia: int) -> None:
        """
        Estabelece a relação de vizinhança entre duas cidades.

        Este método estático estabelece a relação de vizinhança entre duas cidades, adicionando 
        cada uma à lista de vizinhos da outra com a distância especificada.

        Parâmetros
        ----------
        vizinhoA : Cidade
            Uma das cidades que terá a relação de vizinhança estabelecida.
        vizinhoB : Cidade
            A segunda cidade que terá a relação de vizinhança estabelecida.
        distancia : int
            A distância em quilômetros entre as duas cidades.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        vizinhoA.vizinhas[vizinhoB.nome] = distancia
        vizinhoB.vizinhas[vizinhoA.nome] = distancia

    @staticmethod
    def definir_coordenadas(qual_cidade: 'Cidade', coordenadas: dict[str, float]) -> None:
        """
        Aplica coordenadas à cidade especificada.

        Este método estático define as coordenadas em formato de ponto flutuante para a cidade 
        especificada.

        Parâmetros
        ----------
        qual_cidade : Cidade
            A cidade à qual serão atribuídas as coordenadas.
        coordenadas : dict[str, float]
            Um dicionário contendo as coordenadas x e y, representadas por valores de ponto flutuante.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        qual_cidade.coordenadas = coordenadas

    @staticmethod
    def pegar_vizinhos_da_cidade(qual_cidade: 'Cidade') -> list[str]:
        """
        Retorna uma lista de nomes das cidades vizinhas à cidade especificada.

        Este método estático retorna uma lista de strings que correspondem aos nomes das cidades 
        que são vizinhas à cidade passada como parâmetro.

        Parâmetros
        ----------
        qual_cidade : Cidade
            A cidade da qual desejamos obter os vizinhos.

        Retorna
        -------
        list[str]
            Uma lista de nomes das cidades vizinhas à cidade especificada.
        """
        vizinhos_total: list[str] = list(qual_cidade.vizinhas.keys())
        return vizinhos_total

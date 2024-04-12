class Cidade:
    """
    A classe Cidade representa de forma abstrata, uma
    instância de um ponto no mapa, com nome, cidades 
    vizinhas, e as distâncias até elas.

    De forma estática, também armazena todas as cidades no projeto.
    """

    nome: str
    vizinhas: dict[str, int]
    # Atributo estático
    cidades_total: dict[str, 'Cidade'] = {}

    def __init__(self, nome: str) -> None:
        """
        Construtor da classe Cidade.
        
        :param nome: O parâmetro "nome" no construtor define uma string que serve
        de nome para a instância de Cidade que está sendo instanciada.
        :type nome: str
        :return: None
        """

        self.nome = nome
        self.vizinhas = {}
        Cidade.cidades_total[nome] = self

    def __str__(self) -> str:
        """
        Versão em string de uma instância de Cidade.
        
        :return: str
        """

        vizinhas_str = ', '.join(f"{cidade.nome if isinstance(cidade, Cidade) else cidade} ({distancia} km)" for cidade, distancia in self.vizinhas.items())
        return f"A cidade {self.nome} possui essas vizinhas: {vizinhas_str}"

    def distancia_de_vizinho(self, qual_vizinho: str) -> int:
        """
        Traz a distância de uma cidade até um vizinho especificado.

        :param qual_vizinho: Qual o nome do vizinho da cidade que deseja-se obter a 
        distância pra chegar até lá.
        :type qual_vizinho: str
        :return: int
        """

        return self.vizinhas[qual_vizinho]
    
    @staticmethod
    def definir_vizinhos(vizinhoA: 'Cidade', vizinhoB: 'Cidade', distancia: int) -> None:
        """
        O método estático definir_vizinhos aplica vizinhança
        pra cada uma das cidades passadas como parâmetros.

        :param vizinhoA: Uma das cidades que será estabelecida a relação de vizinhança.
        :type vizinhoA: Cidade
        :param vizinhoB: A segunda cidade que será estabelecida a relação de vizinhança.
        :type vizinhoB: Cidade
        :param distancia: A distância entre as duas cidades (sem unidade).
        :type distancia: int
        :return: None
        """

        vizinhoA.vizinhas[vizinhoB.nome] = distancia
        vizinhoB.vizinhas[vizinhoA.nome] = distancia

    @staticmethod
    def pegar_cidade_pelo_nome(nome: str) -> 'Cidade':
        """
        O método estático pegar_cidade_pelo_nome retorna um objeto do tipo
        Cidade a partir de uma string passada como parâmetro, qualquer
        que corresponder essa string ao nome da Cidade. Capitaliza os nomes
        automaticamente.

        :param nome: O nome da cidade a ser retornada.
        :type nome: str
        :return: Cidade
        """
        return Cidade.cidades_total[nome.lower().title()]

    @staticmethod
    def pegar_vizinhos_da_cidade(cidade: 'Cidade') -> list[str]:
        """
        O método pegar_vizinhos_da_cidade retorna uma lista de strings
        que correspondem ao nome das cidades que são vizinhas à cidade
        passada como parâmetro.

        :param cidade: Qual cidade queremos encontrar os vizinhos.
        :type cidade: Cidade
        :return: List[str]
        """
        vizinhos_total: list[str] = list(cidade.vizinhas.keys())

        return vizinhos_total

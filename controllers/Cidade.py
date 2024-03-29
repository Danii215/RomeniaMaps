from typing import Dict, List

class Cidade:
    nome: str
    vizinhas: Dict[str, int]
    # Atributo estático
    cidades_total: Dict[str, 'Cidade'] = {}

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
    def get_cidade_by_nome(nome: str) -> 'Cidade':
        """
        O método estático get_cidade_by_nome retorna um objeto do tipo
        Cidade a partir de uma string passada como parâmetro, qualquer
        que corresponder essa string ao nome da Cidade.

        :param nome: O nome da cidade a ser retornada.
        :type nome: str
        :return: Cidade
        """
        return Cidade.cidades_total.get(nome.lower().capitalize())

    @staticmethod
    def get_vizinhos_from_cidade(cidade: 'Cidade') -> List[str]:
        """
        O método get_vizinhos_from_cidade retorna uma lista de strings
        que correspondem ao nome das cidades que são vizinhas à cidade
        passada como parâmetro.

        :param cidade: Qual cidade queremos encontrar os vizinhos.
        :type cidade: Cidade
        :return: List[str]
        """
        vizinhos_total:            List[str] = list(cidade.vizinhas.keys())
        vizinhos_total_quantidade: int       = len(vizinhos_total)
        # print (f"{cidade.nome} possui {vizinhos_total_quantidade} vizinhos: {vizinhos_total}")

        return vizinhos_total

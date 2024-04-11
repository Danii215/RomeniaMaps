from typing import List
from controllers.Cidade import Cidade
from controllers.Debug import Debug

class Rota:
    """
    A classe Rota armazena uma lista contendo o nome
    de todas as cidades que foram percorridas do ponto
    inicial até o final, além de toda a distância
    percorrida até chegar lá.
    """

    nome_da_cidade_final: str
    caminho: List[str] = []
    distancia_percorrida: int = 0

    def __init__(self, nome_da_cidade_final: str) -> None:
        """
        Construtor da classe Rota.
        
        :param nome_da_cidade_final: Define uma string que serve
        de nome para a instância de Cidade que está sendo instanciada.
        :type nome_da_cidade_final: str
        :return: None
        """
        self.nome_da_cidade_final = nome_da_cidade_final

    def __str__(self) -> str:
        """
        Versão em string de uma instância de Rota.
        
        :return: str
        """

        rota_str = f"Essa rota fez o caminho {self.caminho} percorrendo um total de {self.distancia_percorrida} unidades de distância."
        return rota_str
    
    def incluir_cidade_no_caminho(self, qual_cidade: 'Cidade') -> bool:
        """
        Verifica se a cidade existe e insere o nome dela na lista de cidades
        caminhadas (caminho), caso não esteja lá antes.

        Não insere se já estiver lá pois isso significaria um loop, e força
        a rota a retornar pra trás.

        Retorna "False" se deu errado, "True" se a inserção ocorreu como
        esperado.

        :param qual_cidade: Qual a cidade que deve ser avaliada pra
        adicionar no caminho.
        :type qual_cidade: Cidade
        :return: bool
        """
        if qual_cidade is None: return False
        if qual_cidade.nome in self.caminho: return False

        self.caminho.append(qual_cidade.nome)
        Debug.log("Inserida a cidade " + qual_cidade.nome + " no caminho da rota atual com sucesso.")
        return True

    def tirar_cidade_do_caminho_da_rota(self, qual_cidade: 'Cidade') -> None:
        """
        Retira a distância percorrida de um caminho tomado e retira o nome
        da cidade passada da lista de caminhos desta rota.

        :param qual_cidade: Qual a cidade que será removida do caminho da rota.
        :type qual_cidade: Cidade
        :return: None
        """

        nome_da_penultima_cidade_no_caminho: str = self._nome_da_penultima_cidade_no_caminho()
        distancia_a_subtrair: int = qual_cidade.distancia_de_vizinho(nome_da_penultima_cidade_no_caminho)
        self.subtrair_distancia_percorrida(distancia_a_subtrair)
        self._tirar_nome_da_cidade_do_caminho(qual_cidade)
        Debug.log("Retirada a cidade " + qual_cidade.nome + " do caminho da rota atual com sucesso.")

    def aplicar_distancia(self, de_qual_cidade: 'Cidade', ate_qual_cidade: str) -> None:
        """
        Calcula uma distância de uma cidade até a outra e aplica na distância
        percorrida total da rota.

        :param de_qual_cidade: Cidade inicial, que começará o cálculo.
        :type de_qual_cidade: Cidade
        :param ate_qual_cidade: O nome da cidade final, ponto de chegada.
        :type ate_qual_cidade: str
        :return: None
        """

        unidades_percorridas: int = de_qual_cidade.distancia_de_vizinho(ate_qual_cidade)
        self.distancia_percorrida += unidades_percorridas

    def subtrair_distancia_percorrida(self, unidades_percorridas: int) -> None:
        """
        Subtrai da distância percorrida da Rota o tanto especificado.

        :param unidades_percorridas: O quanto deve ser subtraído.
        :type unidades_percorridas: int
        :return: None
        """

        self.distancia_percorrida -= unidades_percorridas

    def verifica_se_esta_no_caminho(self, nome_da_cidade: str) -> bool:
        """
        Verifica se o nome da cidade passado está presente no caminho.

        Retorna True se encontrado, False se estiver ausente.

        :param nome_da_cidade: O nome da cidade que será verificado.
        :type nome_da_cidade: str
        :return: bool
        """

        if nome_da_cidade in self.caminho: return True
        return False

    def chegou_no_final(self) -> bool:
        """
        Verifica se o nome da cidade final (o objetivo da Rota) está
        presente no caminho.

        Retorna True se encontrado, False se estiver ausente.

        :return: bool
        """

        if self.nome_da_cidade_final in self.caminho: return True
        return False
    
    def encontrado_caminho_morto(self) -> bool:
        """
        Verifica se o caminho da rota atual possui mais de uma cidade.
        Caso não tenha, é possível que o caminho tenha encontrado um
        dead-end.

        Se tiver mais do que uma cidade no caminho, retorna False. 
        Se tiver menos, retorna True, pois é um caminho válido (ainda).

        :return: bool
        """

        if len(self.caminho) > 1: return False
        return True
    
    # Método privado
    def _nome_da_penultima_cidade_no_caminho(self) -> str:
        """
        Traz o nome da penúltima cidade listada no caminho da Rota.

        :return: str
        """

        return self.caminho[-2]
    
    # Método privado
    def _tirar_nome_da_cidade_do_caminho(qual_rota: 'Rota', qual_cidade: 'Cidade') -> bool:
        """
        Verifica se o nome da cidade se encontra armazenado no caminho. Se sim, o remove de lá.

        Retorna True tendo remoção sucedida, ou False se nada ocorreu.

        :param qual_rota: A rota que deve-se avaliar o caminho.
        :type qual_rota: Rota
        :param qual_cidade: A cidade que deve-se retirar do caminho, existindo nele.
        :type qual_cidade: Cidade
        :return: bool
        """

        if qual_cidade.nome in qual_rota.caminho:
            qual_rota.caminho.remove(qual_cidade.nome)
            return True
        
        return False
    
    def quantas_cidades_passamos(self) -> int:
        """
        Retorna a quantidade de cidades armazenadas no caminho da
        Rota.

        :return: int
        """
        
        return len(self.caminho)

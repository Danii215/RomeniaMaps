from Models.Cidade import Cidade

class CidadeController:
    """
    A classe CidadeController fornece métodos estáticos para gerenciar operações relacionadas à Cidade.

    Esses métodos incluem a definição de vizinhos entre cidades, a atribuição de coordenadas a uma cidade
    e a obtenção da lista de vizinhos de uma cidade específica.
    """

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

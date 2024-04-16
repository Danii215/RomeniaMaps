class Cidade:
    """
    A classe Cidade representa de forma abstrata uma instância de um ponto no mapa, com nome, cidades 
    vizinhas e as distâncias até elas. Armazena também as coordenadas dessa Cidade, para melhor visualização
    em um gráfico, caso esse dado seja fornecido corretamente.
    """

    nome: str
    vizinhas: dict[str, int]
    coordenadas: dict[str, float]

    def __init__(self, nome: str) -> None:
        """
        Construtor da classe Cidade.

        Este método inicializa uma instância da classe Cidade com o nome fornecido, 
        com a primeira letra de cada palavra em maiúscula e as demais em minúscula.

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
from Models.Mapa import Mapa
from Models.Cidade import Cidade
from Controllers.CidadeController import CidadeController

class Rota:
    """
    A classe Rota armazena uma lista contendo o nome de todas as cidades que foram percorridas do ponto
    inicial até o final, além de toda a distância percorrida até chegar lá.

    Atributos Públicos
    ------------------
    mapa_da_rota : 'Mapa'
        O objeto `Mapa` que contém todas as informações sobre as cidades e suas conexões.
    cidade_inicial : 'Cidade'
        A cidade inicial da rota.
    nome_da_cidade_final : str
        O nome da cidade final da rota.
    caminho : list[str]
        Uma lista contendo o nome de todas as cidades percorridas na rota, do ponto inicial ao final.
        O padrão é uma lista vazia.
    distancia_percorrida : int
        A distância total percorrida ao longo da rota, em quilômetros.
        O padrão é 0.
    """
    mapa_da_rota: 'Mapa'
    cidade_inicial: 'Cidade'
    nome_da_cidade_final: str
    caminho: list[str] = []
    distancia_percorrida: int = 0

    def __init__(self, mapa_da_rota: 'Mapa', nome_da_cidade_inicial: str, nome_da_cidade_final: str) -> None:
        """
        Construtor da classe Rota.

        Este método inicializa uma instância da classe Rota à traçar de acordo com o mapa, iniciando pelo nome da 
        cidade inicial e finalizando no nome da cidade final.

        Parâmetros
        ----------
        mapa_da_rota : Mapa
            O mapa no qual a rota será criada.
        nome_da_cidade_inicial : str
            O nome da cidade inicial da rota.
        nome_da_cidade_final : str
            O nome da cidade final da rota.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self.mapa_da_rota = mapa_da_rota
        self.cidade_inicial = self.mapa_da_rota.pegar_cidade_pelo_nome(nome_da_cidade_inicial.title())
        self.nome_da_cidade_final = nome_da_cidade_final.title()
        self._criar_rota(self.mapa_da_rota, self.cidade_inicial)

    def __str__(self) -> str:
        """
        Retorna uma representação em string da instância de Rota.

        Este método retorna uma string que descreve a rota, incluindo o caminho percorrido e a 
        distância total percorrida.

        Retorna
        -------
        str
            Uma representação em string da instância de Rota.
        """
        rota_str = f"Esta rota segue o caminho {self.caminho}, percorrendo um total de {self.distancia_percorrida} unidades de distância."
        return rota_str
    
    def verifica_se_esta_no_caminho(self, nome_da_cidade: str) -> bool:
        """
        Verifica se o nome da cidade passada está presente no caminho desta rota.

        Retorna True se encontrado, False se estiver ausente.

        Parâmetros
        ----------
        nome_da_cidade : str
            O nome da cidade que será verificado.

        Retorna
        -------
        bool
            True se o nome da cidade estiver presente no caminho da rota, False se estiver ausente.
        """
        return nome_da_cidade in self.caminho

    def chegou_no_final(self) -> bool:
        """
        Verifica se o nome da cidade final (o destino da rota) está presente no caminho desta rota.

        Retorna True se encontrado, False se estiver ausente.

        Retorna
        -------
        bool
            True se o nome da cidade final estiver presente no caminho da rota, False se estiver ausente.
        """
        return self.nome_da_cidade_final in self.caminho
    
    # Método privado
    def _nome_da_penultima_cidade_no_caminho(self) -> str:
        """
        Retorna o nome da penúltima cidade listada no caminho da rota.

        Este método retorna o nome da penúltima cidade presente na lista de cidades
        no caminho da rota.

        Retorna
        -------
        str
            O nome da penúltima cidade no caminho da rota.
        """
        
        return self.caminho[-2]
    
    # Método privado
    def _subtrair_distancia_percorrida(self, unidades_percorridas: int) -> None:
        """
        Subtrai a quantidade especificada das unidades percorridas na rota.

        Este método subtrai a quantidade especificada das unidades percorridas na rota
        da distância total percorrida pela rota.

        Parâmetros
        ----------
        unidades_percorridas : int
            A quantidade de unidades a ser subtraída da distância percorrida.

        Retorna
        -------
        None
            Este método não retorna nada.
        """

        self.distancia_percorrida -= unidades_percorridas

    # Método privado
    def _criar_rota(self, mapa: 'Mapa', cidade_inicial: 'Cidade') -> 'Rota':
        """
        Inicia o processo de geração de uma nova rota, partindo de uma cidade inicial até uma cidade final.

        Este método inicia o processo de criação de uma rota, que vai da cidade inicial fornecida até a 
        cidade final especificada pelo nome.

        Parâmetros
        ----------
        mapa : Mapa
            O mapa no qual a rota será criada.
        cidade_inicial : Cidade
            A cidade inicial da rota.

        Retorna
        -------
        Rota
            A rota gerada, representada como uma instância da classe Rota.
        """
        print("Criando nova rota...")

        rota = self._caminhar(mapa, self, cidade_inicial)

        print("Rota criada com sucesso: " + str(rota))

        return rota
    
    # Método privado
    def _caminhar(self, mapa: 'Mapa', qual_rota: 'Rota', qual_cidade: 'Cidade') -> 'Rota':
        """
        Realiza a etapa de caminhada durante a geração de uma rota.

        Este método executa a etapa de caminhada durante a geração de uma rota, a partir de uma cidade
        inicial até a cidade final desejada. Ele atualiza a rota conforme avança de uma cidade para a
        próxima, considerando todas as possibilidades de caminho disponíveis.

        Parâmetros
        ----------
        mapa : Mapa
            O mapa no qual a rota está sendo criada.
        qual_rota : Rota
            A rota atual que está sendo gerada.
        qual_cidade : Cidade
            A cidade atual em que a rota está, que será utilizada como ponto de partida para explorar
            novos caminhos.

        Retorna
        -------
        Rota
            A rota atualizada após a etapa de caminhada.
        """
        qual_rota._incluir_cidade_no_caminho(qual_cidade)

        possiveis_caminhos: list[str] = CidadeController.pegar_vizinhos_da_cidade(qual_cidade)

        self._decidir_proximo_caminho_a_percorrer(mapa, qual_rota, qual_cidade, possiveis_caminhos)

        if not qual_rota.chegou_no_final():
            qual_rota._tirar_cidade_do_caminho_da_rota(qual_cidade)
        
        return qual_rota
    
    # Método privado
    def _decidir_proximo_caminho_a_percorrer(self, mapa: 'Mapa', qual_rota: 'Rota', cidade_atual: 'Cidade', possiveis_caminhos: list[str]):
        """
        Decide o próximo caminho a ser percorrido na rota.

        Este método estático é responsável por decidir qual será o próximo caminho a ser percorrido na rota.
        Ele itera sobre uma lista de possíveis caminhos a partir da cidade atual, escolhendo o próximo caminho
        com base em critérios como a conclusão da rota ou se o caminho já está presente na rota.

        Parâmetros
        ----------
        mapa : Mapa
            O mapa que contém as informações sobre as cidades e suas relações.
        qual_rota : Rota
            A rota atual que está sendo percorrida.
        cidade_atual : Cidade
            A cidade atual na rota.
        possiveis_caminhos : list[str]
            Uma lista de possíveis caminhos (nomes de cidades vizinhas) a partir da cidade atual.

        Retorna
        -------
        Rota
            A rota atualizada após percorrer o próximo caminho.

        Observações
        ------------
        Este método é utilizado internamente para decidir o próximo passo a ser tomado na rota.
        """
        for caminho_escolhido in possiveis_caminhos:
            if qual_rota.chegou_no_final():
                return qual_rota
            if qual_rota.verifica_se_esta_no_caminho(caminho_escolhido):
                continue

            qual_rota._aplicar_distancia(cidade_atual, caminho_escolhido)

            proxima_cidade: 'Cidade' = mapa.pegar_cidade_pelo_nome(caminho_escolhido)

            self._caminhar(mapa, qual_rota, proxima_cidade)
    
    # Método privado
    def _incluir_cidade_no_caminho(self, qual_cidade: 'Cidade') -> bool:
        """
        Verifica se a cidade não está presente no caminho atual da rota e a insere, se possível.

        Este método verifica se a cidade especificada ainda não está presente no caminho atual da rota.
        Se a cidade não estiver no caminho, ela é adicionada à lista de cidades percorridas (caminho).
        A inserção não ocorre se a cidade já estiver no caminho, o que indicaria um loop na rota e forçaria
        a rota a retroceder.

        Parâmetros
        ----------
        qual_cidade : Cidade
            A cidade que será avaliada para inclusão no caminho.

        Retorna
        -------
        bool
            True se a cidade foi adicionada com sucesso ao caminho, False se não foi possível adicionar.
        """
        if qual_cidade is None:
            return False
        if qual_cidade.nome in self.caminho:
            return False

        self.caminho.append(qual_cidade.nome)
        return True

    # Método privado
    def _tirar_cidade_do_caminho_da_rota(self, qual_cidade: 'Cidade') -> None:
        """
        Remove uma cidade do caminho percorrido e subtrai a distância percorrida.

        Este método remove o nome da cidade especificada da lista de cidades percorridas (caminho) nesta rota.
        Além disso, subtrai a distância percorrida entre a cidade removida e a cidade anterior ao caminho.

        Parâmetros
        ----------
        qual_cidade : Cidade
            A cidade que será removida do caminho da rota.

        Retorna
        -------
        None
            Este método não retorna nada.
        """

        nome_da_penultima_cidade_no_caminho: str = self._nome_da_penultima_cidade_no_caminho()
        distancia_a_subtrair: int = qual_cidade.distancia_de_vizinho(nome_da_penultima_cidade_no_caminho)
        self._subtrair_distancia_percorrida(distancia_a_subtrair)
        self._tirar_nome_da_cidade_do_caminho(qual_cidade)

    # Método privado
    def _tirar_nome_da_cidade_do_caminho(self, qual_cidade: 'Cidade') -> bool:
        """
        Verifica se o nome da cidade está armazenado no caminho da rota e o remove, se presente.

        Retorna True se a remoção for bem-sucedida, ou False se a cidade não estiver presente no caminho.

        Parâmetros
        ----------
        qual_cidade : Cidade
            A cidade que deve ser removida do caminho, se estiver presente.

        Retorna
        -------
        bool
            True se a cidade foi removida com sucesso, False se a cidade não estiver no caminho.
        """
        if qual_cidade.nome in self.caminho:
            self.caminho.remove(qual_cidade.nome)
            return True
        return False

    # Método privado
    def _aplicar_distancia(self, de_qual_cidade: 'Cidade', ate_qual_cidade: str) -> None:
        """
        Calcula e aplica a distância percorrida de uma cidade até outra.

        Este método calcula a distância entre a cidade inicial e a cidade final especificadas,
        e adiciona essa distância à distância total percorrida pela rota.

        Parâmetros
        ----------
        de_qual_cidade : Cidade
            A cidade inicial para calcular a distância.
        ate_qual_cidade : str
            O nome da cidade final, ponto de chegada.

        Retorna
        -------
        None
            Este método não retorna nada.
        """

        unidades_percorridas: int = de_qual_cidade.distancia_de_vizinho(ate_qual_cidade)
        self.distancia_percorrida += unidades_percorridas
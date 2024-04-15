import matplotlib.pyplot as plt
import networkx as nx
from Controllers.Mapa import Mapa

class Grafo:
    """
    A classe Grafo representa a estrutura de dados gráfica que contém as informações sobre as conexões entre
    as cidades e suas representações visuais.

    Atributos Públicos
    ------------------
    mapa : 'Mapa'
        O mapa associado ao grafo, contendo as informações sobre as cidades e suas conexões.
    representacao : 'nx.Graph'
        A representação gráfica do grafo, utilizando a biblioteca NetworkX.
    atributos_do_desenho : dict[str, any]
        Um dicionário contendo os atributos de desenho do grafo, como cor, tamanho e largura das arestas,
        bem como a posição dos nós no espaço gráfico. Por padrão, inclui os seguintes atributos:
        - 'pos': Um dicionário vazio, que será preenchido posteriormente com as coordenadas das cidades.
        - 'node_color': Cor dos nós, padrão 'skyblue'.
        - 'node_size': Tamanho dos nós, padrão 500.
        - 'edge_color': Cores das arestas, inicialmente uma lista vazia.
        - 'width': Largura das arestas, padrão 3.
        - 'with_labels': Define se as etiquetas (nomes das cidades) devem ser exibidas nos nós, padrão True.
        - 'font_color': Cor das etiquetas, padrão 'black'.
        - 'font_size': Tamanho da fonte das etiquetas, padrão 5.

    """
    mapa: 'Mapa'
    representacao: 'nx.Graph'
    atributos_do_desenho: dict[str, any] = {
        "pos": {},
        "node_color": "skyblue",
        "node_size": 500,
        "edge_color": [],
        "width": 3,
        "with_labels": True,
        "font_color": "black",
        "font_size": 5
    }

    def __init__(self, qual_mapa_para_representar: 'Mapa', caminho: list[str] = None) -> None:
        """
        Inicializa um objeto da classe Grafo para representar um mapa em forma de grafo.

        Este método cria uma representação gráfica do mapa fornecido utilizando
        a biblioteca NetworkX, onde as cidades são representadas como nós e as 
        conexões entre elas como arestas.

        Parâmetros
        ----------
        qual_mapa_para_representar : Mapa
            O objeto Mapa que será representado pelo grafo.
        caminho : list[str], opcional
            Uma lista de nomes de cidades que definirá um caminho específico
            a ser destacado no grafo. Por padrão, é None, o que significa
            que nenhum caminho será destacado.

        Retorna
        -------
        None
            Este método não retorna nada diretamente, mas inicializa o objeto
            Grafo com a representação gráfica do mapa.
        """
        self.representacao = nx.Graph()
        self.mapa = qual_mapa_para_representar

        self._adicionar_cidades_ao_grafo()
        self._adicionar_conexoes_ao_grafo()
        
        self._definir_coordenadas_de_cada_cidade()

        self._definir_cores_para_as_etiquetas(caminho)

        self._desenhar_grafo()

    # Metódo privado
    def _adicionar_cidades_ao_grafo(self) -> None:
        """
        Adiciona nós ao grafo de acordo com as cidades definidas no mapa.

        Este método adiciona nós ao grafo representativo do mapa. Cada nó
        é nomeado de acordo com a lista de nomes de cidades fornecida pela
        instância de Mapa associada.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        self.representacao.add_nodes_from(self.mapa.lista_de_nomes_de_cidades)

    # Metódo privado
    def _adicionar_conexoes_ao_grafo(self) -> None:
        """
        Adiciona as conexões entre os nós ao grafo de acordo com o JSON fornecido à instância
        de Mapa passada para esta instância de Grafo atual.

        As conexões são representadas como edges, que são uma lista de tuplas. Cada tupla contém
        o nome de uma cidade, o nome de sua vizinha e um dicionário com a propriedade "dist",
        correspondente à distância entre as duas cidades. A estrutura complexa das tuplas é uma
        exigência da biblioteca NetworkX, permitindo outras propriedades além da distância, como
        o peso (weight), que não é aplicável ao escopo do projeto atual.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        edges: list[tuple[str, str, dict[str, int]]] = []

        for essa_cidade in self.mapa.todas_as_cidades:
            for nome_de_vizinho in self.mapa.todas_as_cidades[essa_cidade].vizinhas:
                distancia_ate_vizinha: int = self.mapa.todas_as_cidades[essa_cidade].vizinhas[nome_de_vizinho]

                edges.append((essa_cidade, nome_de_vizinho, {"dist": distancia_ate_vizinha}))

        self.representacao.add_edges_from(edges)

    # Metódo privado
    def _definir_coordenadas_de_cada_cidade(self) -> None:
        """
        Define as coordenadas de cada nódulo no grafo para desenhar o mapa corretamente.

        Cria um dicionário onde cada chave é o nome de uma cidade e o valor é uma tupla de dois
        valores de ponto flutuante, representando as coordenadas X e Y da cidade. Essas coordenadas
        são definidas como a posição dos nós no grafo.

        Retorna
        -------
        None
            Este método não retorna nada.
        """
        coordenadas: dict[str, tuple[float]] = {}

        for nome_da_cidade in self.mapa.todas_as_cidades:
            conjunto_de_coordenadas: dict[str, float] = self.mapa.todas_as_cidades[nome_da_cidade].coordenadas
            coordenadas[nome_da_cidade] = (conjunto_de_coordenadas["x"], conjunto_de_coordenadas["y"])

        self.atributos_do_desenho["pos"] = coordenadas
    
    # Metódo privado
    def _definir_etiqueta_para_distancias(self) -> dict[tuple[str, str], int]:
        """
        Coloca uma etiqueta no meio das arestas no resultado final do grafo desenhado, representando a
        distância de uma cidade até a outra.

        Retorna um dicionário onde a chave é uma tupla consistindo do nome, em string, de duas cidades
        vizinhas entre si, e o valor é o número inteiro representando sua distância.

        Retorna
        -------
        dict[tuple[str, str], int]
            Um dicionário onde cada chave é uma tupla de dois nomes de cidades vizinhas e o valor
            é a distância entre elas em inteiro.
        """
        etiqueta_distancia_vizinhos = {
            (cidade, vizinha): distancia["dist"] for cidade, vizinha, distancia in self.representacao.edges(data=True)
        }

        return etiqueta_distancia_vizinhos
    
    # Método privado
    def _definir_cores_para_as_etiquetas(self, caminho: list[str] = None) -> None:
        """
        Define as cores das etiquetas das arestas do grafo.

        Esta função atribui cores às etiquetas das arestas do grafo representado.
        Se um caminho for fornecido, as arestas que compõem esse caminho serão
        destacados com uma cor vermelha, enquanto as demais manterão a cor preta.

        Parâmetros
        ----------
        caminho : list[str], opcional
            Uma lista de strings contendo o caminho que deve ser destacado no grafo.
            Por padrão, é None, o que significa que nenhum caminho será destacado.

        Retorna
        -------
        None
            Esta função não retorna nada.

        """
        nx.set_edge_attributes(self.representacao, "black", "color")        

        if caminho:
            edges_a_serem_pintadas: list[tuple[str, str]] = []

            for nome_de_cidade in caminho:
                indice_da_cidade_atual = caminho.index(nome_de_cidade)
                if indice_da_cidade_atual + 1 == len(caminho): continue

                edge: tuple[str, str] = (nome_de_cidade, caminho[indice_da_cidade_atual + 1])
                edges_a_serem_pintadas.append(edge)
        
            for edge in edges_a_serem_pintadas:
                self.representacao.edges[edge]["color"] = "red"

        self.atributos_do_desenho["edge_color"] = [self.representacao[cidade][vizinha]["color"] for cidade, vizinha in self.representacao.edges()]

    # Método privado
    def _desenhar_grafo(self) -> None:
        """
        Desenha o grafo representado, incluindo etiquetas de distância nas arestas.

        Esta função desenha o grafo representado usando a biblioteca NetworkX e
        inclui etiquetas de distância nas arestas. As etiquetas são posicionadas
        no meio das arestas e exibem a distância entre as cidades conectadas.

        Retorna
        -------
        None
            Esta função não retorna nada.
        """
        etiqueta_distancia_vizinhos: dict[tuple[str, str], int] = self._definir_etiqueta_para_distancias()
        
        nx.draw(self.representacao, **self.atributos_do_desenho)
        nx.draw_networkx_edge_labels(
            self.representacao,
            pos = self.atributos_do_desenho["pos"],
            edge_labels = etiqueta_distancia_vizinhos,
            font_size = 4,
            label_pos = 0.5
        )
    
    def exibir_grafo_em_janela(self) -> None:
        """
        Exibe o grafo representado pelo objeto Mapa em uma janela separada.

        Esta função exibe o grafo renderizado pelo objeto Mapa em uma janela
        separada usando a biblioteca Matplotlib. A janela exibida contém o grafo
        renderizado.

        Retorna
        -------
        None
            Esta função não retorna nada.
        """
        plt.show()

    def exibir_grafo_em_png(self, nome_do_arquivo: str) -> None:
        """
        Gera uma imagem PNG do grafo renderizado pelo objeto Mapa.

        Esta função gera uma imagem PNG do grafo renderizado pelo objeto Mapa
        usando a biblioteca Matplotlib. A imagem é salva no diretório Assets com
        o nome passado e uma resolução de 300 DPI.

        Retorna
        -------
        None
            Esta função não retorna nada.
        """
        plt.savefig(f"Assets/{nome_do_arquivo}.png", dpi=300)
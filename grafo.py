import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

#Garante que o grafo terá um valor de geração fixo (No caso 0)
random.seed(0)
np.random.seed(0)

#Declara o grafo
romenia = nx.Graph()
romenia.graph["Nome"] = "Mapa de Romênia"

#Adiciona os vértices
romenia.add_node("Oradea")
romenia.add_node("Zerind")
romenia.add_node("Arad")
romenia.add_node("Sibiu")
romenia.add_node("Timisoara")
romenia.add_node("Lugoj")
romenia.add_node("Mehadia")
romenia.add_node("Dobreta")
romenia.add_node("Craiova")
romenia.add_node("Rimnicu Vilcea")
romenia.add_node("Fagaras")
romenia.add_node("Pitesti")
romenia.add_node("Bucharest")
romenia.add_node("Giurgiu")
romenia.add_node("Urziceni")
romenia.add_node("Hirsova")
romenia.add_node("Eforie")
romenia.add_node("Vaslui")
romenia.add_node("Iasi")
romenia.add_node("Neamt")
#OU              romenia.add_nodes_from( ["Oradea","Zerind","Arad"...] )      NESSE CASO, É POSSÍVEL PASSAR UM ARRAY COMO REFERÊNCIA PARA OS VÉRTICES


#Adiciona os relacionamentos de vizinhos
romenia.add_edge("Oradea","Zerind",dist=71)
romenia.add_edge("Oradea","Sibiu",dist=151)
romenia.add_edge("Zerind","Arad",dist=75)
romenia.add_edge("Arad","Sibiu",dist=140)
romenia.add_edge("Arad","Timisoara",dist=118)
romenia.add_edge("Timisoara","Lugoj",dist=111)
romenia.add_edge("Lugoj","Mehadia",dist=70)
romenia.add_edge("Mehadia","Dobreta",dist=75)
romenia.add_edge("Dobreta","Craiova",dist=120)
romenia.add_edge("Sibiu","Fagaras",dist=99)
romenia.add_edge("Sibiu","Rimnicu Vilcea",dist=80)
romenia.add_edge("Craiova","Rimnicu Vilcea",dist=146)
romenia.add_edge("Craiova","Pitesti",dist=138)
romenia.add_edge("Rimnicu Vilcea","Pitesti",dist=97)
romenia.add_edge("Fagaras","Bucharest",dist=211)
romenia.add_edge("Pitesti","Bucharest",dist=101)
romenia.add_edge("Bucharest","Giurgiu",dist=90)
romenia.add_edge("Bucharest","Urziceni",dist=85)
romenia.add_edge("Urziceni","Hirsova",dist=98)
romenia.add_edge("Urziceni","Vaslui",dist=142)
romenia.add_edge("Hirsova","Eforie",dist=86)
romenia.add_edge("Vaslui","Iasi",dist=92)
romenia.add_edge("Iasi","Neamt",dist=87)
#OU              romenia.add_edges_from( [("Oradea","Zerind"),("Zerind","Arad")...] )      NESSE CASO, É POSSÍVEL PASSAR ARRAYS COMO REFERÊNCIA PARA OS VIZINHOS


#Define as coordenadas de cada cidade (Feito em cima do plano cartesiano do Romenia.ggb no repositório)
coord = {
            "Oradea":(-0.07,7.96),
            "Zerind":(-0.75,6.72),
              "Arad":(-1.17,5.3),
             "Sibiu":(2.35,4.66),
         "Timisoara":(-1.03,3.16),
             "Lugoj":(1.15,2.48),
           "Mehadia":(1.21,1.4),
           "Dobreta":(1.17,0.36),
           "Craiova":(3.27,0),
    "Rimnicu Vilcea":(2.97,3.3),
           "Fagaras":(4.99,4.54),
           "Pitesti":(5.45,2.4),
         "Bucharest":(7.63,1.68),
           "Giurgiu":(6.79,-0.02),
          "Urziceni":(9.25,2.24),
           "Hirsova":(11.2,2.28),
            "Eforie":(11.71,0.92),
            "Vaslui":(10.57,5.02),
              "Iasi":(9.52,6.58),
             "Neamt":(7.89,7.18),
}

#Monta um dicionário com as distâncias dentro dos "edges"
label_distancia_vizinhos = {(c,v):d["dist"] for c,v,d in romenia.edges(data=True)}

#Alimenta o grafo
nx.draw(romenia,
        pos=coord,
        node_color="skyblue",
        node_size=2000,
        edge_color="black",
        width=5,
        with_labels=True,
        font_color="black",
        font_size=8)

#Alimenta os distâncias entre vizinhos nos grafos
nx.draw_networkx_edge_labels(romenia,
                             pos=coord,
                             edge_labels=label_distancia_vizinhos,
                             label_pos=0.5)

#Define a margem na janela do matplot
plt.margins(0.005)

#Exibe grafo na janela
plt.show()
#print(romenia.edges[dist])

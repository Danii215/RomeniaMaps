from typing import List
from controllers.Cidade import Cidade
from controllers.Rota import Rota

oradea         = Cidade("Oradea")
zerind         = Cidade("Zerind")
arad           = Cidade("Arad")
sibiu          = Cidade("Sibiu")
timisoara      = Cidade("Timisoara")
lugoj          = Cidade("Lugoj")
mehadia        = Cidade("Mehadia")
dobreta        = Cidade("Dobreta")
craiova        = Cidade("Craiova")
rimnicu_vilcea = Cidade("Rimnicu Vilcea")
fagaras        = Cidade("Fagaras")
pitesti        = Cidade("Pitesti")
bucharest      = Cidade("Bucharest")
giurgiu        = Cidade("Giurgiu")
urziceni       = Cidade("Urziceni")
hirsova        = Cidade("Hirsova")
eforie         = Cidade("Eforie")
vaslui         = Cidade("Vaslui")
iasi           = Cidade("Iasi")
neamt          = Cidade("Neamt")

Cidade.definir_vizinhos(oradea, zerind, 71)
Cidade.definir_vizinhos(oradea, sibiu, 151)
Cidade.definir_vizinhos(zerind, arad, 75)
Cidade.definir_vizinhos(arad, sibiu, 140)
Cidade.definir_vizinhos(arad, timisoara, 118)
Cidade.definir_vizinhos(timisoara, lugoj, 111)
Cidade.definir_vizinhos(lugoj, mehadia, 70)
Cidade.definir_vizinhos(mehadia, dobreta, 75)
Cidade.definir_vizinhos(dobreta, craiova, 120)
Cidade.definir_vizinhos(sibiu, fagaras, 99)
Cidade.definir_vizinhos(sibiu, rimnicu_vilcea, 80)
Cidade.definir_vizinhos(craiova, rimnicu_vilcea, 146)
Cidade.definir_vizinhos(craiova, pitesti, 138)
Cidade.definir_vizinhos(rimnicu_vilcea, pitesti, 97)
Cidade.definir_vizinhos(fagaras, bucharest, 211)
Cidade.definir_vizinhos(pitesti, bucharest, 101)
Cidade.definir_vizinhos(bucharest, giurgiu, 90)
Cidade.definir_vizinhos(bucharest, urziceni, 85)
Cidade.definir_vizinhos(urziceni, hirsova, 98)
Cidade.definir_vizinhos(urziceni, vaslui, 142)
Cidade.definir_vizinhos(hirsova, eforie, 86)
Cidade.definir_vizinhos(vaslui, iasi, 92)
Cidade.definir_vizinhos(iasi, neamt, 87)


nome_da_cidade_inicial: str = input("Insira a cidade inicial: ").lower().capitalize()
cidade_inicial: 'Cidade' = Cidade.get_cidade_by_nome(nome_da_cidade_inicial)

nome_da_cidade_final: str = input("Insira a cidade final: ").lower().capitalize()
cidade_final: 'Cidade' =  Cidade.get_cidade_by_nome(nome_da_cidade_final)

rota: 'Rota' = Rota(nome_da_cidade_final)

def criar_rota(qual_cidade: 'Cidade'):
    if rota.incluir_cidade_no_caminho(qual_cidade):
        if rota.chegou_no_final(): return

        vizinhos: List[str] = Cidade.get_vizinhos_from_cidade(qual_cidade)

        for vizinho in vizinhos:
            if rota.chegou_no_final(): break
            if rota.verifica_se_esta_no_caminho(vizinho): continue

            distancia_ate_o_vizinho: int = qual_cidade.distancia_de_vizinho(vizinho)
            rota.somar_distancia_percorrida(distancia_ate_o_vizinho)
            criar_rota(Cidade.get_cidade_by_nome(vizinho))

        if not rota.chegou_no_final():
            nome_da_penultima_cidade: str = rota.nome_da_penultima_cidade_no_caminho()
            distancia_a_subtrair: int = qual_cidade.distancia_de_vizinho(nome_da_penultima_cidade)
            rota.tirar_cidade_do_caminho(qual_cidade.nome)
            rota.subtrair_distancia_percorrida(distancia_a_subtrair)

criar_rota(cidade_inicial)

print(rota)
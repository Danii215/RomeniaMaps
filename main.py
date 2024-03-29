from typing import Dict, List
from controllers.Cidade import Cidade

#Define as variáveis do tipo Cidade para cada cidade
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

#Define os vizinhos das Cidades
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

nome_da_cidade_inicial: str = input("Insira a cidade inicial: ")
cidade_inicial: 'Cidade' = Cidade.get_cidade_by_nome(nome_da_cidade_inicial)

nome_da_cidade_final: str = input("Insira a cidade final: ")
cidade_final: 'Cidade' =  Cidade.get_cidade_by_nome(nome_da_cidade_final)

#Proximo passo -> Trabalhar com o "for" do "get_vizinhos_from_vizinho"

rota: List[str] = []

def iterar_vizinhos(qual_cidade: 'Cidade'):
    if nome_da_cidade_final.lower().capitalize() in rota: return 
    if qual_cidade is None: return
    
    rota.append(qual_cidade.nome)

    vizinhos: List[str] = Cidade.get_vizinhos_from_cidade(qual_cidade)
    for vizinho in vizinhos:
        if nome_da_cidade_final.lower().capitalize() in rota: return 
        
        if vizinho in rota: 
            continue

        if vizinho != nome_da_cidade_final.lower().capitalize():
            iterar_vizinhos(Cidade.get_cidade_by_nome(vizinho))
        else: break
    
    if nome_da_cidade_final.lower().capitalize() not in rota: 
        print("sucesso parabenms")
        rota.append(nome_da_cidade_final.lower().capitalize())
    return

iterar_vizinhos(cidade_inicial)

print(rota)
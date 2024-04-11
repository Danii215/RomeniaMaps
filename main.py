from typing import List
from controllers.Cidade import Cidade
from controllers.Rota import Rota
from controllers.Debug import Debug

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
cidade_inicial: 'Cidade' = Cidade.pegar_cidade_pelo_nome(nome_da_cidade_inicial)

nome_da_cidade_final: str = input("Insira a cidade final: ").lower().capitalize()
cidade_final: 'Cidade' =  Cidade.pegar_cidade_pelo_nome(nome_da_cidade_final)

lista_de_rotas: List['Rota'] = []

def criar_rota():
    Debug.log("Criando nova rota...")
    nova_rota: 'Rota' = Rota(nome_da_cidade_final)

    rota = caminhar(nova_rota, cidade_inicial)

    Debug.log("Rota criada com sucesso: " + str(rota))
    lista_de_rotas.append(rota)

def caminhar(qual_rota: 'Rota', qual_cidade: 'Cidade') -> 'Rota':
    qual_rota.incluir_cidade_no_caminho(qual_cidade)

    possiveis_caminhos: List[str] = Cidade.pegar_vizinhos_da_cidade(qual_cidade)

    if len(qual_rota.caminho) == 1: quantidade_de_possibilidades: int = len(possiveis_caminhos)
    else: quantidade_de_possibilidades: int = len(possiveis_caminhos) - 1

    for caminho_escolhido in possiveis_caminhos:
        if qual_rota.chegou_no_final(): return qual_rota
        if qual_rota.verifica_se_esta_no_caminho(caminho_escolhido): continue

        Debug.log(f"atualmente estou em {qual_cidade.nome}.")
        Debug.log(f"de {possiveis_caminhos} eu escolhi {caminho_escolhido}, que é a opção {possiveis_caminhos.index(caminho_escolhido)} de {quantidade_de_possibilidades} opções")

        qual_rota.aplicar_distancia(qual_cidade, caminho_escolhido)

        proxima_cidade: 'Cidade' = Cidade.pegar_cidade_pelo_nome(caminho_escolhido)

        caminhar(qual_rota, proxima_cidade)

    if not qual_rota.chegou_no_final(): qual_rota.tirar_cidade_do_caminho_da_rota(qual_cidade)
    
    return qual_rota

criar_rota()

print(lista_de_rotas)
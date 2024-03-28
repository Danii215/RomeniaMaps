from typing import Dict, List

class Cidade:
    nome: str
    vizinhas: Dict[str, int]
    # Atributo estático
    cidades_total: Dict[str, 'Cidade'] = {}

    #Construtor
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.vizinhas = {}
        Cidade.cidades_total[nome] = self

    #Retorno da cidade e seus vizinhos
    def __str__(self) -> str:
        vizinhas_str = ', '.join(f"{cidade.nome if isinstance(cidade, Cidade) else cidade} ({distancia} km)" for cidade, distancia in self.vizinhas.items())
        return f"A cidade {self.nome} possui essas vizinhas: {vizinhas_str}"
    
    #Cadastro dos Vizinhos
    @staticmethod
    def definir_vizinhos(vizinhoA: 'Cidade', vizinhoB: 'Cidade', distancia: int) -> None:
        vizinhoA.vizinhas[vizinhoB.nome] = distancia
        vizinhoB.vizinhas[vizinhoA.nome] = distancia

    #Retorna nome no tipo Cidade
    @staticmethod
    def get_cidade_by_nome(nome: str) -> 'Cidade':
        return Cidade.cidades_total.get(nome.lower().capitalize())

    #Método principal
    @staticmethod
    def get_vizinhos_from_vizinho(vizinho: 'Cidade'):
        vizinhos_total:            List[str] = list(vizinho.vizinhas.keys())
        vizinhos_total_quantidade: int       = len(vizinhos_total)
        print (f"{vizinho.nome} possui {vizinhos_total_quantidade} vizinhos: {vizinhos_total}")
        for cidade_vizinha in vizinhos_total:
            # print(Cidade.get_cidade_by_nome(cidade_vizinha))
            cidade_from_nome: 'Cidade' = Cidade.get_cidade_by_nome(cidade_vizinha)
            print(cidade_vizinha)
            # Cidade.get_vizinhos_from_vizinho(cidade_from_nome)


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

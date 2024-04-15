from Controllers.Mapa import Mapa
from Controllers.Rota import Rota
from Controllers.Grafo import Grafo
from Views.HomeView import HomeView
#Terminar de implementar a classe HomeView e trazer os inputs para o main, gerando a rota

def main():
    mapa: 'Mapa' = Mapa()
    
    nome_da_cidade_inicial: str = input("Insira a cidade inicial: ")
    nome_da_cidade_final: str = input("Insira a cidade final: ")

    rota: 'Rota' = Rota(mapa, nome_da_cidade_inicial, nome_da_cidade_final)

    grafo: 'Grafo' = Grafo(mapa, rota.caminho)
    grafo.exibir_grafo_em_png()

if __name__ == "__main__":
    main()

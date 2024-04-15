from Controllers.Mapa import Mapa
from Controllers.Rota import Rota
from Controllers.Grafo import Grafo
from Views.HomeView import Home

def main():
    mapa: 'Mapa' = Mapa()

    grafo_inicial: 'Grafo' = Grafo(mapa)
    grafo_inicial.exibir_grafo_em_png("grafo_inicial")

    home: 'Home' = Home()

    nome_da_cidade_inicial: str = home.nome_da_cidade_inicial
    nome_da_cidade_final: str = home.nome_da_cidade_final

    rota: 'Rota' = Rota(mapa, nome_da_cidade_inicial, nome_da_cidade_final)

    grafo: 'Grafo' = Grafo(mapa, rota.caminho)
    grafo.exibir_grafo_em_png("grafo_finalizado")
    grafo.exibir_grafo_em_janela()

if __name__ == "__main__":
    main()

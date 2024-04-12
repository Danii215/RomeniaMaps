from Controllers.Cidade import Cidade
from Controllers.Mapa import Mapa
from Controllers.Rota import Rota

def main():
    Mapa()

    nome_da_cidade_inicial: str = input("Insira a cidade inicial: ").lower().title()
    cidade_inicial: 'Cidade' = Cidade.pegar_cidade_pelo_nome(nome_da_cidade_inicial)

    nome_da_cidade_final: str = input("Insira a cidade final: ").lower().title()

    Rota.criar_rota(cidade_inicial, nome_da_cidade_final)

if __name__ == "__main__":
    main()
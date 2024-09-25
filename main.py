import os
from operacoes.persistencia import InicializandoBase, CarregarDados
from operacoes.particao import SelecionarPorSubstituicao
from operacoes.arvore_binaria_vencedores import intercalar_particoes

if __name__ == "__main__":
    # Inicializando a base de dados se necessário
    NumeroDeEntidades = 100  # Número de entidades para inicializar
    InicializandoBase(NumeroDeEntidades)

    # Definindo o arquivo de dados a ser ordenado (somente eventos)
    arquivo_para_ordenar = "dados/eventos.pkl"
    
    # Verificar se o arquivo existe e contém dados de eventos
    dados = CarregarDados(arquivo_para_ordenar)
    if not dados:
        print(f"Arquivo {arquivo_para_ordenar} não contém dados ou está vazio.")
    else:
        print(f"Arquivo {arquivo_para_ordenar} carregado com sucesso.")

        # Definindo o tamanho da memória (quantidade de itens que cabem no heap)
        tamanho_memoria = 50  # Ajuste este valor para definir o tamanho do heap

        # Passo 1: Gera as partições iniciais utilizando Seleção por Substituicao
        SelecionarPorSubstituicao(arquivo_para_ordenar, tamanho_memoria)

        # Passo 2: Intercala as partições para gerar o arquivo final ordenado
        pasta_particoes = "particoes"  # Diretório onde as partições foram salvas
        arquivo_saida = "dados/eventos_ordenados"  # Nome do arquivo de saída final
        intercalar_particoes(pasta_particoes, arquivo_saida)

        print("Ordenação de eventos concluída com sucesso. Arquivo final salvo.")

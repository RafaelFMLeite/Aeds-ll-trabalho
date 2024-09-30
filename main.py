import os
from operacoes.persistencia import InicializandoBase, CarregarDados
from operacoes.particao import SelecionarPorSubstituicao
from operacoes.arvore_binaria_vencedores import intercalar_particoes
from operacoes.arvore_b import BTree

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

        # Criando uma árvore B para armazenar e ordenar os eventos
        btree = BTree(3)  # Grau mínimo da árvore B

        # Inserindo todos os eventos na árvore B
        for evento in dados:
            btree.insert(evento)

        # Travessia da árvore B para exibir os eventos ordenados
        print("Eventos na árvore B:")
        btree.traverse()
        """""
        id_evento_para_deletar = 101
        btree.delete(id_evento_para_deletar)
        print(f"Evento com ID {id_evento_para_deletar} excluído da árvore B.")
        """""
        # Exemplo de busca por um evento com ID específico
        id_evento_para_buscar = 102
        evento_encontrado = btree.search(id_evento_para_buscar)
        if evento_encontrado:
            print(f"Evento encontrado: ID = {evento_encontrado.id_evento}, Nome = {evento_encontrado.nome}")
        else:
            print(f"Evento com ID {id_evento_para_buscar} não encontrado.")

        # Agora podemos seguir com a ordenação externa utilizando partições:
        tamanho_memoria = 50  # Defina o tamanho do heap

        # Passo 1: Gera as partições iniciais utilizando Seleção por Substituição
        SelecionarPorSubstituicao(arquivo_para_ordenar, tamanho_memoria)

        # Passo 2: Intercala as partições para gerar o arquivo final ordenado
        pasta_particoes = "particoes"  # Diretório onde as partições foram salvas
        arquivo_saida = "dados/eventos_ordenados"  # Nome do arquivo de saída final
        intercalar_particoes(pasta_particoes, arquivo_saida)

        print("Ordenação de eventos concluída com sucesso. Arquivo final salvo.")
import os
import pickle
import heapq
from operacoes.persistencia import SalvarDados, SalvarDadosTxt, CarregarDados

def SelecionarPorSubstituicao(filename, tam_memoria):
    """
    Realiza a seleção por substituição para ordenar os dados e gerar corridas iniciais.
    
    Parameters:
    - filename: Nome do arquivo de entrada com os dados desordenados.
    - tam_memoria: Tamanho da memória disponível (número de itens que cabem no heap).
    """
    dados = CarregarDados(filename)
    if not dados:
        print(f"O arquivo {filename} está vazio ou não foi encontrado.")
        return

    particoes = []  # Lista para armazenar as partições/corridas
    corrida_atual = []  # Buffer para a corrida atual
    heap = []  # Fila de prioridades (heap)
    contador_particoes = 0  # Contador para nomear as partições
    
    # Preenche o heap inicial com os primeiros m itens
    for i in range(min(tam_memoria, len(dados))):
        heapq.heappush(heap, dados[i])
    
    proxima_corrida = False  # Flag para indicar quando iniciar uma nova corrida
    for i in range(tam_memoria, len(dados)):
        menor_item = heapq.heappop(heap)  # Retira o menor item do heap
        corrida_atual.append(menor_item)

        # Se o próximo item for menor que o menor item retirado, inicia uma nova corrida
        if dados[i] < menor_item:
            proxima_corrida = True

        # Adiciona o próximo item ao heap, mesmo que ele pertença à próxima corrida
        heapq.heappush(heap, dados[i])

        # Se for hora de iniciar uma nova corrida
        if proxima_corrida:
            # Salva a corrida atual
            nome_particao = f"particoes/particao_{contador_particoes}"
            SalvarDados(corrida_atual, f"{nome_particao}.pkl")
            SalvarDadosTxt(corrida_atual, nome_particao)
            particoes.append(nome_particao)
            contador_particoes += 1
            corrida_atual = []  # Reseta o buffer da corrida atual
            proxima_corrida = False

    # Após processar todos os itens, salvar o restante da corrida atual
    while heap:
        corrida_atual.append(heapq.heappop(heap))
    
    if corrida_atual:
        nome_particao = f"particoes/particao_{contador_particoes}"
        SalvarDados(corrida_atual, f"{nome_particao}.pkl")
        SalvarDadosTxt(corrida_atual, nome_particao)
        particoes.append(nome_particao)

    print(f"Partições criadas: {particoes}")
    return particoes


def IntercalarParticoes(particoes, output_file):
    """
    Função para intercalar as partições ordenadas e gerar um arquivo final ordenado.

    Parameters:
    - particoes: Lista de nomes das partições
    - output_file: Nome do arquivo de saída ordenado
    """
    heap = []
    arquivos = []

    # Abre todas as partições e insere o primeiro item de cada uma no heap
    for particao in particoes:
        arquivo = open(f"{particao}.pkl", 'rb')
        arquivos.append(arquivo)
        dados_particao = pickle.load(arquivo)
        
        if dados_particao:
            # Cada item no heap será um tupla com o formato (valor, index da partição)
            heapq.heappush(heap, (dados_particao.pop(0), particao))

    resultado_ordenado = []

    # Intercala os dados usando o heap
    while heap:
        menor_item, particao = heapq.heappop(heap)
        resultado_ordenado.append(menor_item)

        # Reabastece o heap com o próximo item da partição de onde veio o menor item
        particao_index = particoes.index(particao)
        if arquivos[particao_index]:
            try:
                proximo_item = pickle.load(arquivos[particao_index])
                if proximo_item:
                    heapq.heappush(heap, (proximo_item, particao))
            except EOFError:
                arquivos[particao_index].close()

    # Salva o resultado final
    SalvarDados(resultado_ordenado, f"{output_file}.pkl")
    SalvarDadosTxt(resultado_ordenado, output_file)
    print(f"Arquivo final ordenado salvo como: {output_file}.pkl e {output_file}.txt")


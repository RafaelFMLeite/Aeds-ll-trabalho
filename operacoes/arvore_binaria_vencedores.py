import os
import pickle
import heapq

class ArvoreVencedores:
    def __init__(self, pasta_particoes):
        self.corridas = []  # Lista para armazenar as partições carregadas
        self.heap = []  # O heap será utilizado para armazenar os vencedores de cada corrida.
        self.carregar_particoes(pasta_particoes)
    
    def carregar_particoes(self, pasta_particoes):
        arquivos_pkl = [f for f in os.listdir(pasta_particoes) if f.startswith('particao_') and f.endswith('.pkl')]
        arquivos_pkl.sort()  # Opcional, caso queira garantir uma ordem de leitura
        
        for i, arquivo in enumerate(arquivos_pkl):
            caminho_arquivo = os.path.join(pasta_particoes, arquivo)
            with open(caminho_arquivo, 'rb') as f:
                corrida = pickle.load(f)  # Carrega a partição do arquivo .pkl
                if corrida:
                    self.corridas.append(corrida)  # Armazena a corrida
                    # Inicializa o heap com o primeiro item de cada corrida
                    heapq.heappush(self.heap, (corrida.pop(0), i))  # (valor, índice da corrida)
    
    def proximo_vencedor(self):
        if not self.heap:
            return None
        
        # O heap nos dá o menor valor disponível (o vencedor)
        menor, corrida_index = heapq.heappop(self.heap)
        
        # Pega o próximo elemento da corrida de onde saiu o menor valor
        if self.corridas[corrida_index]:
            # Adiciona o próximo elemento dessa corrida ao heap
            heapq.heappush(self.heap, (self.corridas[corrida_index].pop(0), corrida_index))
        
        return menor

    def intercalar(self):
        resultado_final = []
        
        while self.heap:
            vencedor = self.proximo_vencedor()
            if vencedor is not None:
                resultado_final.append(vencedor)
        
        return resultado_final


def intercalar_particoes(pasta_particoes, arquivo_saida):
    arvore = ArvoreVencedores(pasta_particoes)
    resultado = arvore.intercalar()
    
    # Salva o resultado final intercalado em um arquivo .pkl
    with open(arquivo_saida + ".pkl", 'wb') as f:
        pickle.dump(resultado, f)
    
    # Também salva o resultado em um arquivo .txt para leitura simples
    with open(arquivo_saida + ".txt", 'w') as f:
        for item in resultado:
            f.write(f"{str(item)}\n")
    
    print(f"Resultado da intercalação salvo em: {arquivo_saida}.pkl e {arquivo_saida}.txt")

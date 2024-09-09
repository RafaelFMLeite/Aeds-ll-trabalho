import heapq
from operacoes.persistencia import salvar_dados

class NoVencedor:
    def __init__(self, indice, valor):
        self.indice = indice
        self.valor = valor
    
    def __lt__(self, outro):
        return self.valor < outro.valor

    def __repr__(self):
        return f"NoVencedor(indice={self.indice}, valor={self.valor})"

def arvore_vencedores(particoes):
    heap = []
    resultado = []

    # Inicializa o heap com o primeiro elemento de cada partição
    for i, particao in enumerate(particoes):
        if particao:  # Certifique-se de que a partição não está vazia
            heapq.heappush(heap, NoVencedor(i, particao.pop(0)))

    while heap:
        vencedor = heapq.heappop(heap)
        resultado.append(vencedor.valor)

        # Se a partição do vencedor ainda tem elementos, insira o próximo elemento
        if particoes[vencedor.indice]:  # Corrigido para 'indice'
            heapq.heappush(heap, NoVencedor(vencedor.indice, particoes[vencedor.indice].pop(0)))

    # Salvar o log dos eventos intercalados
    salvar_log_intercalacao(resultado)
    
    return resultado

def salvar_log_intercalacao(resultado):
    with open('dados/log_intercalacao.txt', 'w') as f:
        f.write("Eventos Intercalados:\n")
        for evento in resultado:
            f.write(f"{evento}\n")
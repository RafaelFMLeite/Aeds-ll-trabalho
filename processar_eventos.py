# processar_eventos.py

from arvore_b import BTree
from evento import Evento

def ler_eventos(nome_arquivo):
    eventos = []
    with open(nome_arquivo, 'r') as file:
        for linha in file:
            partes = linha.strip().split(',')
            if len(partes) != 4:
                continue  # Ignora linhas inválidas
            evento_id_str, tipo, data, cliente = partes
            try:
                evento_id = int(evento_id_str)
            except ValueError:
                continue  # Ignora IDs que não são inteiros
            evento = Evento(evento_id, tipo, data, cliente)
            eventos.append(evento)
    return eventos

def processar_eventos(nome_eventos, grau, log_file):
    btree = BTree(grau, log_file)
    eventos = ler_eventos(nome_eventos)
    
    # Inserindo todos os eventos na Árvore B
    for evento in eventos:
        btree.insert(evento)
    
    # Opcional: Realizar buscas e remoções aleatórias para demonstrar funcionalidades
    # Aqui, vamos realizar 10 buscas e 5 remoções aleatórias
    import random
    eventos_para_busca = random.sample(eventos, 10)
    eventos_para_remover = random.sample(eventos, 5)
    
    for evento in eventos_para_busca:
        resultado = btree.search(btree.root, evento.evento_id)
        if resultado:
            btree.log(f"Busca: {resultado}")
        else:
            btree.log(f"Busca: Evento ID {evento.evento_id} nao encontrado.")
    
    for evento in eventos_para_remover:
        btree.remove(evento.evento_id)
    
    # Opcional: Exibir a estrutura final da árvore
    btree.log("\nEstrutura Final da Arvore B:")
    btree.print_tree(btree.root)

if __name__ == "__main__":
    nome_eventos = "eventos.txt"
    grau = 3  # Grau mínimo da Árvore B
    log_file = "arvore_b_log.txt"
    processar_eventos(nome_eventos, grau, log_file)
    print(f"Processamento concluido. Veja o log em '{log_file}'.")

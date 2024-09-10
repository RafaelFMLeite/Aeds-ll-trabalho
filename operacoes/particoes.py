import heapq
from operacoes.persistencia import salvar_dados
from entidades.evento import Evento

def particionar_por_letra(dados):
    from collections import defaultdict
    
    particoes = defaultdict(list)
    
    for evento in dados:
        if isinstance(evento, Evento):
            if hasattr(evento, 'nome') and evento.nome:
                letra_inicial = evento.nome[0].upper()
                if 'A' <= letra_inicial <= 'Z':
                    particoes[letra_inicial].append(evento)
                    print(f"Evento adicionado à partição '{letra_inicial}': {evento}")
    
    for letra, eventos in particoes.items():
        print(f"Partição '{letra}': {len(eventos)} eventos")
    
    return [particoes[letra] for letra in sorted(particoes)]

def gerar_particoes_por_letra_com_log(dados):
    import logging
    from datetime import datetime

    # Configuração do logging
    logging.basicConfig(filename='particoes_log.txt', level=logging.INFO)
    
    # Gera partições
    particoes = particionar_por_letra(dados)
    
    # Salva log
    log_filename = f"particoes_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_filename, 'w') as f:
        for i, particao in enumerate(particoes, start=1):
            f.write(f"Partição {i}:\n")
            for evento in particao:
                f.write(f"  {evento}\n")
            f.write(f"Tamanho da partição {i}: {len(particao)} eventos\n\n")
    
    return particoes
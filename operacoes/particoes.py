import heapq
from operacoes.persistencia import salvar_dados

def geracao_particoes_selecao_substituicao(dados, tam_memoria):
    particoes = []
    memoria = []
    i = 0
    num_particao = 0  # Para contar as partições geradas

    # Abre o arquivo de log para escrita
    with open('log_particoes.txt', 'w') as log_file:
        # Preenche a memória com os primeiros elementos
        while i < tam_memoria and i < len(dados):
            heapq.heappush(memoria, dados[i])
            i += 1

        # Enquanto houver dados
        while i < len(dados):
            particao_atual = []
            
            # Enquanto houver itens na memória
            while memoria:
                menor = heapq.heappop(memoria)
                particao_atual.append(menor)

                # Se o próximo item nos dados for maior ou igual ao menor item da memória
                if i < len(dados) and dados[i] >= menor:
                    heapq.heappush(memoria, dados[i])
                    i += 1
                else:
                    break

            # Armazenar a partição gerada
            particoes.append(particao_atual)

            # Log para a partição gerada
            log_file.write(f"Partição {num_particao + 1}:\n")
            for evento in particao_atual:
                log_file.write(f"  Evento ID: {evento.id_evento}, Nome: {evento.nome}\n")
            log_file.write(f"Tamanho da partição {num_particao + 1}: {len(particao_atual)} eventos\n\n")

            num_particao += 1

            # Recarregar a memória com os próximos itens
            memoria.clear()
            while i < len(dados) and len(memoria) < tam_memoria:
                heapq.heappush(memoria, dados[i])
                i += 1

        # Adicionar a última partição restante
        if memoria:
            particao_atual = []
            while memoria:
                particao_atual.append(heapq.heappop(memoria))

            particoes.append(particao_atual)

            # Log para a última partição gerada
            log_file.write(f"Partição {num_particao + 1}:\n")
            for evento in particao_atual:
                log_file.write(f"  Evento ID: {evento.id_evento}, Nome: {evento.nome}\n")
            log_file.write(f"Tamanho da partição {num_particao + 1}: {len(particao_atual)} eventos\n\n")

    return particoes
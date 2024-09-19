import pickle
from datetime import datetime
from entidades.evento import Evento

def criar_particoes_max_20(dados, tamanho_particao=20):
    """
    Cria partições a partir dos dados com gerenciamento de congelamento de registros.
    """
    particoes = []
    particao_atual = []
    congelados = []  # Lista de eventos congelados

    while dados:
        # Seleciona o registro com a menor chave que não esteja congelado
        registro = min(dados, key=lambda evento: evento.nome)

        # Remove o registro do conjunto de dados original
        dados.remove(registro)

        # Adiciona o registro à partição atual
        particao_atual.append(registro)

        # Verifica se a partição atingiu o tamanho máximo
        if len(particao_atual) == tamanho_particao:
            particoes.append(particao_atual)
            particao_atual = []

        # Verifica o próximo registro
        if dados:
            proximo_registro = min(dados, key=lambda evento: evento.nome)
            # Se o próximo registro tiver chave menor que o recém gravado, congela-o
            if proximo_registro.nome < registro.nome:
                congelados.append(proximo_registro)
                dados.remove(proximo_registro)

        # Se não houver mais registros não congelados, finalize a partição e descongele
        if not dados:
            if particao_atual:
                particoes.append(particao_atual)
            if congelados:
                dados.extend(congelados)
                congelados = []

    return particoes

# Função para salvar o log das partições
def gerar_particoes_por_letra_com_log(dados):
    """
    Gera partições e um log com o processamento de cada uma.
    """
    total_eventos = len(dados)
    tamanho_particao = 20
    numero_particoes = (total_eventos + tamanho_particao - 1) // tamanho_particao  # Cálculo do número máximo de partições

    with open('log_particoes.txt', 'w') as log_file:
        log_file.write(f"Log de Partições Gerado em {datetime.now()}\n")
        log_file.write(f"Número máximo de partições possíveis: {numero_particoes}\n\n")

        particoes = criar_particoes_max_20(dados, tamanho_particao)
        
        # Percorre cada partição
        for i, particao in enumerate(particoes):
            log_file.write(f"Partição {i+1}:\n")
            for evento in particao:
                log_file.write(f"  {evento.nome}\n")
            log_file.write(f"Tamanho da partição {i+1}: {len(particao)} eventos\n\n")
    
    return particoes

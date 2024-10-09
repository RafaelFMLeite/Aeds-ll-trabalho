# gerar_eventos.py

import random
from evento import Evento

def gerar_eventos(nome_arquivo, num_eventos, faixa_ids):
    tipos_evento = ['Aniversario', 'Casamento', 'Formatura', 'Conferencia', 'Evento Corporativo']
    clientes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana']
    eventos = []
    ids_disponiveis = list(range(0, faixa_ids + 1))  # IDs de 0 a 100 inclusive
    random.shuffle(ids_disponiveis)

    with open(nome_arquivo, 'w') as file:
        for _ in range(num_eventos):
            if not ids_disponiveis:
                print("Todos os IDs disponiveis foram utilizados.")
                break
            evento_id = ids_disponiveis.pop()
            tipo = random.choice(tipos_evento)
            dia = random.randint(1, 28)  # Simplificacao para evitar datas invalidas
            mes = random.randint(1, 12)
            ano = random.randint(2024, 2025)
            data = f"{dia:02d}/{mes:02d}/{ano}"
            cliente = random.choice(clientes)
            evento = Evento(evento_id, tipo, data, cliente)
            eventos.append(evento)
            file.write(f"{evento.evento_id},{evento.tipo},{evento.data},{evento.cliente}\n")
    print(f"Arquivo de eventos '{nome_arquivo}' gerado com sucesso com {len(eventos)} eventos.")

if __name__ == "__main__":
    nome_arquivo = "eventos.txt"
    num_eventos = 10  # Numero de eventos a serem gerados (0 a 100 inclusive)
    faixa_ids = 9  # Faixa de IDs (0 a 100)
    gerar_eventos(nome_arquivo, num_eventos, faixa_ids)

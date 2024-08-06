from operacoes.busca import busca_sequencial

def adicionar_convidado_evento(eventos, convidados, evento_id, convidado_id):
    evento = busca_sequencial(eventos, evento_id, 'id_evento')
    convidado = busca_sequencial(convidados, convidado_id, 'id_convidado')
    if evento and convidado:
        if not hasattr(evento, 'convidados'):
            evento.convidados = []
        evento.convidados.append(convidado)
        return True
    return False

def listar_convidados_evento(eventos, evento_id):
    evento = busca_sequencial(eventos, evento_id, 'id_evento')
    if evento and hasattr(evento, 'convidados'):
        return [convidado.nome for convidado in evento.convidados]
    return []

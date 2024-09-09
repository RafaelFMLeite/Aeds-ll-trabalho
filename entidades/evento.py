class Evento:
    def __init__(self, id_evento, nome, organizador_id):
        self.id_evento = id_evento        # ID do evento  
        self.nome = nome                  # Nome do evento
        self.organizador_id = organizador_id  # ID do organizador
        self.bebidas = []                 # Lista de bebidas
        self.comidas = []                 # Lista de comidas
        self.convidados = []              # Lista de convidados
        
    # Método para comparação "menor que"
    def __lt__(self, outro):
        return self.id_evento < outro.id_evento

    # Método para comparação "maior que"
    def __gt__(self, outro):
        return self.id_evento > outro.id_evento

    # Método para comparação "igual"
    def __eq__(self, outro):
        return self.id_evento == outro.id_evento

    # Método para comparação "menor ou igual"
    def __le__(self, outro):
        return self.id_evento <= outro.id_evento

    # Método para comparação "maior ou igual"
    def __ge__(self, outro):
        return self.id_evento >= outro.id_evento

    # Adicionar bebida ao evento
    def adicionar_bebida(self, bebida_id):
        self.bebidas.append(bebida_id)    
    
    # Adicionar comida ao evento
    def adicionar_comida(self, comida_id):
        self.comidas.append(comida_id)     
    
    # Adicionar convidado ao evento
    def adicionar_convidado(self, convidado_id):
        self.convidados.append(convidado_id)  

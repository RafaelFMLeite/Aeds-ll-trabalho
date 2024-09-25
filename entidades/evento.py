class Evento:
    def __init__(self, id_evento, nome, organizador_id):
        self.id_evento = id_evento      
        self.nome = nome                 
        self.organizador_id = organizador_id  
        self.bebidas = []                 
        self.comidas = []                 
        self.convidados = []              
    
    def __lt__(self, other):
        return self.id_evento < other.id_evento
    def __str__(self):
        return f"Evento ID: {self.id_evento}, Nome: {self.nome}"

    def __repr__(self):
        return f"Evento(ID: {self.id_evento}, Nome: '{self.nome}')"

    def adicionar_bebida(self, bebida_id):
        self.bebidas.append(bebida_id)    

    def adicionar_comida(self, comida_id):
        self.comidas.append(comida_id)     
    
    def adicionar_convidado(self, convidado_id):
        
        self.convidados.append(convidado_id)  

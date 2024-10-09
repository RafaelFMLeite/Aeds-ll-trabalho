# evento.py

class Evento:
    def __init__(self, evento_id, tipo, data, cliente):
        self.evento_id = evento_id  # Chave unica para a Arvore B
        self.tipo = tipo            # Tipo do evento (Aniversario, Casamento, etc.)
        self.data = data            # Data do evento (formato: DD/MM/AAAA)
        self.cliente = cliente      # Nome do cliente

    def __str__(self):
        return f"ID: {self.evento_id}, Tipo: {self.tipo}, Data: {self.data}, Cliente: {self.cliente}"

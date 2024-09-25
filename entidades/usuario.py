class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome

    def __lt__(self, other):
        return self.id_usuario < other.id_usuario

    def __str__(self):
        return f"Usuario({self.id_usuario}, {self.nome})"
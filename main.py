import random
import string

from entidades.usuario import Usuario
from entidades.evento import Evento
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida

from operacoes.ordenacao import merge_sort
from operacoes.interacoes import adicionar_convidado_evento, listar_convidados_evento

def gerar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Gerando bases de dados desordenadas
usuarios = [Usuario(gerar_id(), f"Usuario_{i}") for i in range(10)]
eventos = [Evento(gerar_id(), f"Evento_{i}", random.choice(usuarios).id_usuario) for i in range(5)]
convidados = [Convidado(gerar_id(), f"Convidado_{i}", random.choice([True, False])) for i in range(20)]
comidas = [Comida(gerar_id(), f"Comida_{i}") for i in range(10)]
bebidas = [Bebida(gerar_id(), f"Bebida_{i}") for i in range(10)]

# Ordenando a base de dados de usuários pelo nome
merge_sort(usuarios, 'nome')

# Exemplo de uso
evento_id = eventos[0].id_evento
convidado_id = convidados[0].id_convidado

adicionar_convidado_evento(eventos, convidados, evento_id, convidado_id)
print(listar_convidados_evento(eventos, evento_id))

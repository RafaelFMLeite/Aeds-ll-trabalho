import pickle
import random
import string
from entidades.usuario import Usuario
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida

def salvar_dados(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def carregar_dados(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def gerar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def gerar_dados():
    usuarios = [Usuario(gerar_id(), f"Usuario_{i}") for i in range(80)]
    convidados = [Convidado(gerar_id(), f"Convidado_{i}", random.choice([True, False])) for i in range(80)]
    comidas = [Comida(gerar_id(), f"Comida_{i}") for i in range(80)]
    bebidas = [Bebida(gerar_id(), f"Bebida_{i}") for i in range(80)]

    salvar_dados(usuarios, 'dados/usuarios.pkl')
    salvar_dados(convidados, 'dados/convidados.pkl')
    salvar_dados(comidas, 'dados/comidas.pkl')
    salvar_dados(bebidas, 'dados/bebidas.pkl')

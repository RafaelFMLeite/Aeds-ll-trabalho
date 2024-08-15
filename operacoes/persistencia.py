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
    # ID é composto de 6 caracteres alfanuméricos, seguido de um sufixo numérico
    sufixo = f"_{random.randint(1, 999):03d}"
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + sufixo

def gerar_dados():
    usuarios = [Usuario(gerar_id(), f"Usuario_{gerar_id()}") for i in range(80)]
    convidados = [Convidado(gerar_id(), f"Convidado_{gerar_id()}", random.choice([True, False])) for i in range(80)]
    comidas = [Comida(gerar_id(), f"Comida_{gerar_id()}") for i in range(80)]
    bebidas = [Bebida(gerar_id(), f"Bebida_{gerar_id()}") for i in range(80)]

    salvar_dados(usuarios, 'dados/usuarios.pkl')
    salvar_dados(convidados, 'dados/convidados.pkl')
    salvar_dados(comidas, 'dados/comidas.pkl')
    salvar_dados(bebidas, 'dados/bebidas.pkl')

import pickle
import random
import string
from entidades.usuario import Usuario
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida
from entidades.evento import Evento

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

def gerar_nome_entidade(entidade, index):
    """Gera nomes no formato Entidade_a, Entidade_b, etc."""
    letras = string.ascii_lowercase
    if index < len(letras):
        return f"{entidade}_{letras[index]}"
    else:
        index -= len(letras)
        primeiro_letra = letras[index // len(letras)]
        segunda_letra = letras[index % len(letras)]
        return f"{entidade}_{primeiro_letra}{segunda_letra}"

def gerar_dados():
    # Carregar dados existentes
    usuarios = carregar_dados('dados/usuarios.pkl')
    convidados = carregar_dados('dados/convidados.pkl')
    comidas = carregar_dados('dados/comidas.pkl')
    bebidas = carregar_dados('dados/bebidas.pkl')
    eventos = carregar_dados('dados/eventos.pkl')

    if not usuarios:
        usuarios = [Usuario(gerar_id(), gerar_nome_entidade("Usuario", i)) for i in range(80)]
        random.shuffle(usuarios)  # Embaralhar usuários
        salvar_dados(usuarios, 'dados/usuarios.pkl')

    if not convidados:
        convidados = [Convidado(gerar_id(), gerar_nome_entidade("Convidado", i), random.choice([True, False])) for i in range(80)]
        random.shuffle(convidados)  # Embaralhar convidados
        salvar_dados(convidados, 'dados/convidados.pkl')

    if not comidas:
        comidas = [Comida(gerar_id(), gerar_nome_entidade("Comida", i)) for i in range(80)]
        random.shuffle(comidas)  # Embaralhar comidas
        salvar_dados(comidas, 'dados/comidas.pkl')

    if not bebidas:
        bebidas = [Bebida(gerar_id(), gerar_nome_entidade("Bebida", i)) for i in range(80)]
        random.shuffle(bebidas)  # Embaralhar bebidas
        salvar_dados(bebidas, 'dados/bebidas.pkl')

    if not eventos:
        organizadores = [usuario.id_usuario for usuario in usuarios]
        eventos = [Evento(gerar_id(), gerar_nome_entidade("Evento", i), random.choice(organizadores)) for i in range(80)]
        random.shuffle(eventos)  # Embaralhar eventos
        salvar_dados(eventos, 'dados/eventos.pkl')
    else:
        # Embaralhar eventos existentes
        eventos = carregar_dados('dados/eventos.pkl')
        random.shuffle(eventos)
        salvar_dados(eventos, 'dados/eventos.pkl')

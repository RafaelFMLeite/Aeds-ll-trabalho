# operacoes/ordenacao.py

from entidades.usuario import Usuario
from entidades.convidado import Convidado
from entidades.comida import Comida
from entidades.bebida import Bebida

def merge_sort(lista, key_func):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], key_func)
    direita = merge_sort(lista[meio:], key_func)

    return merge(esquerda, direita, key_func)

def merge(esquerda, direita, key_func):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if key_func(esquerda[i]) <= key_func(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def key_func(item):
    if isinstance(item, Usuario):
        return item.id_usuario
    elif isinstance(item, Convidado):
        return item.id_convidado
    elif isinstance(item, Comida):
        return item.id_comida
    elif isinstance(item, Bebida):
        return item.id_bebida
    else:
        raise AttributeError("Entidade não tem um atributo de ID conhecido.")

def ordenar_dados(dados):
    return merge_sort(dados, key_func)

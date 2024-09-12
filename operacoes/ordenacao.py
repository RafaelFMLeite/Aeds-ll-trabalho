<<<<<<< HEAD
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
=======
def merge_sort(dados, chave):
    # Verifica se a lista tem mais de um elemento para garantir que a divisão faz sentido
    if len(dados) > 1:
        mid = len(dados) // 2  # Divide a lista ao meio (usando divisão inteira)
        left_half = dados[:mid]  # Cria a metade esquerda da lista
        right_half = dados[mid:]  # Cria a metade direita da lista

        merge_sort(left_half, chave)  # Ordena recursivamente a metade esquerda
        merge_sort(right_half, chave)  # Ordena recursivamente a metade direita

        i = j = k = 0  # Inicializa os índices para percorrer left_half, right_half e dados, respectivamente

        # Combina as duas metades em uma lista ordenada
        while i < len(left_half) and j < len(right_half):  # Enquanto houver elementos em ambas as metades
            # Compara o valor da chave do elemento da metade esquerda com o da metade direita
            if getattr(left_half[i], chave, float('inf')) < getattr(right_half[j], chave, float('inf')):
                dados[k] = left_half[i]  # Se o elemento da esquerda é menor, coloca-o na lista de dados
                i += 1  # Move para o próximo elemento na metade esquerda
            else:
                dados[k] = right_half[j]  # Caso contrário, coloca o elemento da direita na lista de dados
                j += 1  # Move para o próximo elemento na metade direita
            k += 1  # Move para o próximo índice na lista de dados

        # Adiciona os elementos restantes da metade esquerda, se houver
        while i < len(left_half):  # Enquanto houver elementos na metade esquerda não processados
            dados[k] = left_half[i]  # Adiciona o elemento restante da esquerda na lista de dados
            i += 1  # Move para o próximo elemento na metade esquerda
            k += 1  # Move para o próximo índice na lista de dados

        # Adiciona os elementos restantes da metade direita, se houver
        while j < len(right_half):  # Enquanto houver elementos na metade direita não processados
            dados[k] = right_half[j]  # Adiciona o elemento restante da direita na lista de dados
            j += 1  # Move para o próximo elemento na metade direita
            k += 1  # Move para o próximo índice na lista de dados
>>>>>>> development

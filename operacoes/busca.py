def busca_sequencial(lista, chave, atributo):
    for item in lista:
        if getattr(item, atributo) == chave:
            return item
    return None

def busca_binaria(lista, chave, atributo):
    lista.sort(key=lambda x: getattr(x, atributo))
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor_meio = getattr(lista[meio], atributo)
        if valor_meio == chave:
            return lista[meio]
        elif valor_meio < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

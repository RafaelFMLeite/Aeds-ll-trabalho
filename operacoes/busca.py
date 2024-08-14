def busca_sequencial(lista, atributo, valor):
    for item in lista:
        if getattr(item, atributo) == valor:
            return item
    return None

def busca_binaria(lista, atributo, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if getattr(lista[meio], atributo) < valor:
            inicio = meio + 1
        elif getattr(lista[meio], atributo) > valor:
            fim = meio - 1
        else:
            return lista[meio]
    return None

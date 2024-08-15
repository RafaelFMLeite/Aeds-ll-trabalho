def busca_sequencial(lista, atributo, valor):
    for item in lista:
        if getattr(item, atributo) == valor:  # valor do atributo do item é igual ao valor buscado
            return item
    return None

def busca_binaria(lista, atributo, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        # valor do atributo no meio da lista é menor, maior ou igual ao valor buscado
        if getattr(lista[meio], atributo) < valor:
            inicio = meio + 1  # se for menor, move o início para a metade superior
        elif getattr(lista[meio], atributo) > valor:
            fim = meio - 1  # se for maior, move o fim para a metade inferior
        else:
            return lista[meio]  # se for igual, retorna o item encontrado
    return None

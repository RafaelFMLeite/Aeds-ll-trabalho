def merge_sort(lista, atributo):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda, atributo)
        merge_sort(direita, atributo)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if getattr(esquerda[i], atributo) < getattr(direita[j], atributo):
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

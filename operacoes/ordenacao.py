def merge_sort(dados, chave):
    if len(dados) > 1:
        mid = len(dados) // 2
        left_half = dados[:mid]
        right_half = dados[mid:]

        merge_sort(left_half, chave)
        merge_sort(right_half, chave)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], chave, float('inf')) < getattr(right_half[j], chave, float('inf')):
                dados[k] = left_half[i]
                i += 1
            else:
                dados[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            dados[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            dados[k] = right_half[j]
            j += 1
            k += 1
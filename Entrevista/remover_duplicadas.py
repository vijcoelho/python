def remover_duplicada(arr):
    novo_arr = set()
    for i in arr:
        if i not in novo_arr:
            novo_arr.add(i)
    return novo_arr

print(remover_duplicada([1,11,2,1,1,2]))
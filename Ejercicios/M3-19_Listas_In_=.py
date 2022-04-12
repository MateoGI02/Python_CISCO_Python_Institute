miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
miLista2=[]
#
for i in miLista:
    if i not in miLista2:
        miLista2.append(i)
#
miLista=miLista2
print("La lista solo con elementos únicos:")
print(miLista)

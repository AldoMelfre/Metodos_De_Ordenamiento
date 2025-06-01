# Método de Ordenamiento QuickSort
# --------------------------------
# QuickSort es un algoritmo eficiente de ordenamiento que utiliza el método de "divide y vencerás".
# Selecciona un elemento como pivote y divide la lista en dos sublistas: una con elementos menores
# al pivote y otra con elementos mayores. Luego ordena recursivamente las sublistas.

def quicksort(lista, inicio, fin):
    if inicio < fin:
        # Particionamos la lista y obtenemos el índice del pivote
        pivote_idx = particion(lista, inicio, fin)
        # Ordenamos la sublista izquierda
        quicksort(lista, inicio, pivote_idx - 1)
        # Ordenamos la sublista derecha
        quicksort(lista, pivote_idx + 1, fin)

def particion(lista, inicio, fin):
    pivote = lista[fin]  # Elegimos el último elemento como pivote
    i = inicio - 1       # Índice del menor elemento

    for j in range(inicio, fin):
        if lista[j] <= pivote:  # Si el elemento actual es menor o igual al pivote
            i += 1
            lista[i], lista[j] = lista[j], lista[i]  # Intercambiamos

    # Colocamos el pivote en su posición correcta
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1  # Retornamos el índice del pivote

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [10, 7, 8, 9, 1, 5]
    print("Lista original:", datos)
    quicksort(datos, 0, len(datos) - 1)
    print("Lista ordenada:", datos)
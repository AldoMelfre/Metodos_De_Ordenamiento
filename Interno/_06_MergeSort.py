# Método de Ordenamiento Merge Sort
# ---------------------------------
# Merge Sort es un algoritmo eficiente que utiliza el método de "divide y vencerás".
# Divide la lista en mitades, ordena cada mitad recursivamente y luego las combina (merge)
# en una sola lista ordenada. Es muy eficiente para listas grandes.

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2  # Encontramos el punto medio
        izquierda = lista[:medio]  # Dividimos la lista en dos mitades
        derecha = lista[medio:]

        # Ordenamos recursivamente ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Mezclamos las mitades ordenadas
        i = j = k = 0  # i para izquierda, j para derecha, k para lista principal

        # Combinamos los elementos en orden
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Añadimos los elementos restantes de la izquierda (si hay)
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Añadimos los elementos restantes de la derecha (si hay)
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", datos)
    merge_sort(datos)
    print("Lista ordenada:", datos)
# Método de Ordenamiento por Selección
# ------------------------------------
# El método de selección ordena una lista buscando el elemento más pequeño
# (o más grande) y colocándolo en la primera posición, luego repite el proceso
# con el resto de la lista. Es sencillo pero no muy eficiente para listas grandes.

def seleccion(lista):
    # Recorremos toda la lista
    for i in range(len(lista)):
        min_idx = i  # Suponemos que el elemento actual es el menor

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:  # Si encontramos uno menor
                min_idx = j                # Actualizamos el índice del menor

        # Intercambiamos el elemento actual con el menor encontrado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11]
    print("Lista original:", datos)
    seleccion(datos)
    print("Lista ordenada:", datos)
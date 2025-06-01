# Método de Ordenamiento por Intercambio (Burbuja)
# ------------------------------------------------
# El método de intercambio, conocido como "burbuja", compara pares de elementos
# adyacentes y los intercambia si están en el orden incorrecto. Este proceso se
# repite varias veces hasta que la lista está ordenada. Es fácil de entender,
# pero poco eficiente para listas grandes.

def burbuja(lista):
    n = len(lista)  # Obtenemos la longitud de la lista
    # Recorremos la lista tantas veces como elementos tiene
    for i in range(n):
        # En cada pasada, los elementos más grandes "suben" al final
        for j in range(0, n - i - 1):
            # Comparamos el elemento actual con el siguiente
            if lista[j] > lista[j + 1]:
                # Si están en el orden incorrecto, los intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [5, 1, 4, 2, 8]
    print("Lista original:", datos)
    burbuja(datos)
    print("Lista ordenada:", datos)
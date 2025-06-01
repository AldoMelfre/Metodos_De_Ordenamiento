# Método de Ordenamiento Radix Sort
# ---------------------------------
# Radix Sort es un algoritmo de ordenamiento no comparativo que ordena los números
# procesando sus dígitos individualmente. Ordena los elementos por cada dígito,
# desde el menos significativo hasta el más significativo, usando un método estable
# como Counting Sort para cada posición.

def counting_sort(lista, exp):
    n = len(lista)
    salida = [0] * n  # Lista de salida ordenada según el dígito actual
    conteo = [0] * 10  # Conteo para los dígitos (0-9)

    # Contamos la cantidad de ocurrencias de cada dígito
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # Actualizamos conteo para que contenga las posiciones reales de los dígitos
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construimos la lista de salida
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    # Copiamos la lista ordenada según el dígito al arreglo original
    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    # Encontramos el número máximo para saber el número de dígitos
    maximo = max(lista) if lista else 0

    # Aplicamos counting_sort para cada dígito (exp = 1, 10, 100, ...)
    exp = 1
    while maximo // exp > 0:
        counting_sort(lista, exp)
        exp *= 10

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", datos)
    radix_sort(datos)
    print("Lista ordenada:", datos)
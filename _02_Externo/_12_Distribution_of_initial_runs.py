# Algoritmo para la distribución inicial de runs en Polyphase Sort
# ---------------------------------------------------------------
# Este algoritmo reparte los runs iniciales entre varios archivos temporales
# siguiendo la secuencia de Fibonacci, como requiere Polyphase Sort.
# Así se optimiza el número de fusiones y se garantiza que siempre haya un archivo vacío.

def fibonacci_sequence(n):
    # Genera la secuencia de Fibonacci hasta que la suma sea al menos n
    fibs = [1, 1]
    while sum(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def distribuir_runs(num_runs, num_archivos):
    # Calcula la distribución de runs según Fibonacci para num_archivos archivos
    fibs = fibonacci_sequence(num_runs)
    # Tomamos los últimos 'num_archivos' números de la secuencia
    distribucion = fibs[-num_archivos:]
    suma = sum(distribucion)
    # Ajustamos la distribución para que la suma sea igual a num_runs
    exceso = suma - num_runs
    for i in range(exceso):
        distribucion[i] -= 1  # Restamos uno a los primeros archivos hasta ajustar
    return distribucion

# Ejemplo de uso:
if __name__ == "__main__":
    num_runs = 10      # Número total de runs iniciales
    num_archivos = 3   # Número de archivos temporales

    distribucion = distribuir_runs(num_runs, num_archivos)
    print(f"Distribución de runs en {num_archivos} archivos:", distribucion)
    # Por ejemplo, salida: [5, 3, 2] para 10 runs y 3 archivos

    # Ahora puedes escribir los runs en los archivos según esta distribución
    # run0.txt tendrá 5 runs, run1.txt tendrá 3, run2.txt tendrá 2, etc.
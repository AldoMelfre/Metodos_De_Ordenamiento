# Método de Ordenamiento Externo: Straight Merging
# ------------------------------------------------
# Straight Merging es un método de ordenamiento externo utilizado cuando los datos
# no caben en memoria principal. Divide el archivo en bloques ordenados (runs) y
# luego los fusiona repetidamente hasta obtener el archivo ordenado completo.
# Es útil para archivos grandes almacenados en disco.

def merge_files(file1, file2, output):
    # Fusiona dos archivos ordenados en uno solo
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as fout:
        line1 = f1.readline()
        line2 = f2.readline()
        while line1 and line2:
            if int(line1) <= int(line2):
                fout.write(line1)
                line1 = f1.readline()
            else:
                fout.write(line2)
                line2 = f2.readline()
        # Escribimos el resto de los archivos
        while line1:
            fout.write(line1)
            line1 = f1.readline()
        while line2:
            fout.write(line2)
            line2 = f2.readline()

# Nota: Para un ordenamiento externo completo, se requiere dividir el archivo original
# en runs ordenados y luego fusionar repetidamente usando la función anterior.
# Este ejemplo muestra solo la función de fusión (merge) para archivos de texto
# donde cada línea es un número.

# Ejemplo de uso:
# merge_files('run1.txt', 'run2.txt', 'salida.txt')
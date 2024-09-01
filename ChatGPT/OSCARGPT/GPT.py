def gauss_jordan(A, b):
    # Número de filas y columnas en la matriz A
    n = len(A)
    
    # Crear una copia de A y b para no modificar los originales
    A = [row[:] for row in A]
    b = b[:]
    
    # Convertir A en una matriz aumentada con b
    for i in range(n):
        A[i].append(b[i])
    
    # Aplicar eliminación hacia adelante para llevar la matriz a la forma escalonada
    for i in range(n):
        # Buscar el pivote más grande en la columna i en o por debajo de la fila i
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        # Intercambiar la fila actual con la fila del pivote máximo
        A[i], A[max_row] = A[max_row], A[i]
        
        # Convertir el pivote en 1 (hacer la fila pivote)
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("La matriz es singular y no se puede resolver.")
        A[i] = [x / pivot for x in A[i]]
        
        # Hacer ceros todos los elementos en la columna i debajo y encima del pivote
        for j in range(n):
            if i != j:
                factor = A[j][i]
                A[j] = [A[j][k] - factor * A[i][k] for k in range(len(A[i]))]
    
    # Extraer la solución que ahora está en la última columna de la matriz aumentada
    return [row[-1] for row in A]

# Ejemplo de uso
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
solucion = gauss_jordan(A, b)
print("La solución es:", solucion)

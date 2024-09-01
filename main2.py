from models.GaussJordan import GaussJordan 
def crear_matriz():
    # Solicitar al usuario el tamaño de la matriz
    n = int(input("Ingrese el tamaño de la matriz: "))
    
    # Crear una matriz vacía
    matriz = []
    
    print(f"Ingrese los datos de su matriz tamaño {n} (ingrese fila por fila, separando los números con espacios):")
    
    # Rellenar la matriz con los datos del usuario
    for i in range(n):
        fila = list(map(int, input(f"Ingrese los datos de la fila {i+1}: ").split()))
        matriz.append(fila)
    
    return matriz

# Ejemplo de uso de la función
matrix = crear_matriz()
print("Matriz ingresada por el usuario:")
for fila in matrix:
    print(fila)

if not GaussJordan._valid_matrix(matrix):
    exit(0)
m = GaussJordan(matrix)
m.gauss_jordan(True)
print(m)
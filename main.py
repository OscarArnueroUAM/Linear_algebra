from models.GaussJordan import GaussJordan 
from models.Matrix import Matrix
from sys import argv

def show_details(number:str) ->bool | None:
    if len(argv) < 3: return False
    if number == '1':
        return True
    elif number == '0':
        return False
    return None

def main() -> int:
    '''
    Códigos de salida

    1: Argumentos no ingresados al llamar al archivo desde la consola
    2: Matriz inválida
    3: Tercer argumento inválido
    4: Fallo en el cálculo de la matriz identidad (Matriz inconsistente)
    5: Salida exitosa. No se presentaron errores
    '''
    if len(argv) < 2:
        print(f'Uso: {argv[0]} matrix.csv "0/1" para mostrar detalles. Por defecto no se muestran')
        return 1
    file_path = argv[1]
    matrix = Matrix.create_matrix(file_path)
    if not Matrix._valid_matrix(matrix):
        return 2
    matrix_instance = GaussJordan(matrix)
    print_ = show_details(argv[2])
    if print_ == None:
        return 3
    print("\nMatriz inicial")
    print(matrix_instance)
    if matrix_instance.gauss_jordan(print_) !=None:
        return 4
    print("Matriz final")
    print(matrix_instance)
    matrix_instance.soluciones()
    return 5

exit_code = main()
print(f"Executable finished with code {exit_code}")
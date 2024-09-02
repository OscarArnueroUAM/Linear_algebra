from csv import reader
from sys import argv

def matrix_error_handler(f):
    def wrapper(*args,**kwargs):
        try:
            if not args[0].endswith('.csv'):
                raise FileNotFoundError
            result = f(*args,**kwargs)
        except ValueError:
            print('Tipo de dato invalido')
            return []
        except FileNotFoundError:
            print('Archivo no encontrado')
            return []
        except Exception as e:
            print(f'Error: {e}')
            return []
        else:
            return result
    return wrapper

class Matrix():

    def __init__(self,matrix: list[list]) -> None:
        self.matrix = matrix
        self.width = len(matrix)
        self.length = len(matrix[0])
    
    @staticmethod
    def _valid_matrix(matrix: list[list]) -> bool:
        if matrix == []: 
            print('Matriz invalida')
            return False
        width = len(matrix)
        length = len(matrix[0])
        if length - width !=1: 
            print("Cantidad de filas o de columnas insuficientes.")
            return False
        zero_row = True
        for row in range(width):
            zero_row = True
            for col in range(length):
                if matrix [row][col] !=0: zero_row = False
                if len(matrix[row]) !=length:
                    print('Matriz incompleta')
                    return False
            if zero_row:
                print('Matriz inconsistente')
                return False
        return True

    def swap(self,row,row_to_swap,print_=True) -> None:
        '''
        Permite cambiar entre dos filas de una matriz. 
        
        Parámetros:
        row (int) : Una de las filas que se va a intercambiar
        row_to_swap (int) : La otra fila que se va a intercambiar
        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero

        El cambio se realiza en la matriz de la instancia que se esté trabajando.
        '''

        self.matrix[row],self.matrix[row_to_swap] = self.matrix[row_to_swap],self.matrix[row]
        if print_: 
            print(f"f{row+1} <--> f{row_to_swap+1}\n")
            print(self)

    @staticmethod
    def __gcd(a: int,b: int) -> int: 
        '''
        Retorna el máximo común divisor entre dos números enteros

        Parámetros:
        a (int) : El primer numero
        b (int) : El segundo numero
        '''
        if a == 0:
            return b
        return Matrix.gcd(b%a,a)

    @staticmethod
    def __lcd(a: int, b:int) ->int:
        '''
        Retorna el mínimo común múltiplo entre dos números enteros

        Parámetros:
        a (int) : El primer numero
        b (int) : El segundo numero
        '''
        return a*b // Matrix.gcd(a,b)
    
    def soluciones(self) ->None:
        x_count: int = 1
        print("Soluciones")
        for col in range(self.width):
            print(f'x{x_count} = {self.matrix[col][-1]}')
            x_count+=1
    @staticmethod
    @matrix_error_handler
    def create_matrix(file_path: str) ->list[list[int]]:
        with open(file_path,mode='r',encoding='utf-8') as f:
            content = list(reader(f,delimiter=';'))
            content = [list(map(float, row)) for row in content]
            return content
        
    def __str__(self) -> str:
        matrix : str = ''
        max_row_width = max(len(f'{round(self.matrix[row][col], 3)}') for row in range(self.width) for col in range(self.length)) + 2
        for row in range(self.width):
            row_str = ''
            for col in range(self.length):
                row_str += f'{round(self.matrix[row][col], 3):<{max_row_width}}'
            matrix += row_str + '\n'
        return matrix
    '''
     matrix :str= ''
        for row in range(self.width):
            for col in range(self.length):
                matrix+=f'{round(self.matrix[row][col],3)} '
            matrix +='salto de linea aqui'
        return matrix
    '''
    
if __name__ == '__main__':
    if len(argv)<2:
        print(f"Uso: {argv[0]} matrix.csv")
        exit(0)
    file_path = argv[1]
    matrix = Matrix.create_matrix(file_path)
    if not Matrix._valid_matrix(matrix):
        exit(0)
    m = Matrix(matrix)
    print(m)
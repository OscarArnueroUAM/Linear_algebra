if __name__ !='__main__':
    from models.Matrix import Matrix
else:
    from Matrix import Matrix
from sys import argv

class GaussJordan(Matrix):
    def __init__(self, matrix: list[list]) -> None:
        super().__init__(matrix)
    
    def gauss_jordan(self,print_=True) ->None | int:
        '''
        Transforma la matriz de la instancia en una matriz identidad con los valores de las incógnitas, siempre y cuando la matriz sea consistente.

        Itera sobre la matriz de manera vertical para determinar que el "pivote" o número en la diagonal sea 1, y proceder a reducir cada término a 0, excepto los de la diagonal.

        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero
        
        '''
        for col in range(self.length):
            for row in range(col,self.width):
                if self.matrix[col][col] != 1: #Estos bloques if se pueden mejorar, tienen mucha profundidad y se ve feo
                    if not self.diagonal_number_to_1(col,row,print_):
                        print('Matriz inconsistente')
                        return 5
                self.reduce_col(col,print_)
                
    def diagonal_number_to_1(self,col: int,row: int,print_=True) -> bool:
        '''
        Intenta tranformar un "pivote" de la matriz en 1.

        La función prioriza que en las posiciones debajo del pivote exista un 1 o -1, realizando un cambio directo en ese caso.

        Posteriormente, prioriza que los números debajo del pivote sean cualquiera excepto 0, realizando un cambio directo en ese caso.

        Ya recorridos todos los numeros, se verifica si el "pivote" no es 0, pues esto daria pie a una matriz inconsistente.

        Finalmente, se realiza una operacion sobre la fila del "pivote" para transformar ese número en 1.

        Parámetros:

        col (int): Es la columna en la que se encuentra ubicado el "pivote"

        row (int): Es la fila en la que se encuentra ubicado el "pivote"

        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero

        Retorna verdadero si la transformacion fue valida, retorna falso si la matriz es inconsistente
        '''
        #La logica se podria mejorar
        if col == self.width: return True

        for i in range(col+1, self.width):
            if self.matrix[i][row] == -1: self.operate_in_row(i,print_)
            if self.matrix[i][row] != 1: continue
            self.swap(col,i,print_)
            return True
        for i in range(col+1,self.width):
            if self.matrix[i][row] == 0: continue
            self.swap(col,i,print_)
            self.operate_in_row(col,print_)
            return True
        if self.matrix[col][row] == 0: return False
        self.operate_in_row(col,print_)
        return True

    def operate_in_row(self,row: int,print_ = True):
        '''
        Opera sobre una fila con el propósito de transformar el "pivote" de esa fila en 1.

        La fila es dividida entre el mismo numero que el pivote

        Parámetros:

        col (int) : Es la columna sobre la que se va a operar

        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero
        '''
        divide_number = self.matrix[row][row]
        self.matrix[row] = list(map(lambda number: number/divide_number,self.matrix[row]))
        if print_:
            print(f'f{row+1} -> {divide_number}f{row+1}')
            print(self)

    def reduce_row(self, diagonal_col : int, operate_row : int,print_ = True) ->None:
        '''
        Reduce una fila para convertir el numero que esta en la columna del "pivote" en 0.

        Calcula el numero por el que se va a operar y lo suma con la fila que se desea convertir

        Parámetros:

        diagonal_col (int): Es la columna donde se encuentra el "pivote"

        operate_row (int): Es la fila que se va a reducir

        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero
        '''
        number_to_operate = self.matrix[operate_row][diagonal_col] * -1

        self.matrix[operate_row] = [self.matrix[operate_row][i]+self.matrix[diagonal_col][i]*
                                    number_to_operate for i in range(self.length)]
        if print_:
            print(f'f{operate_row+1} -> f{operate_row+1} {'+' if number_to_operate > 0 else '-'} {number_to_operate if number_to_operate >0 else number_to_operate*-1}f{diagonal_col+1}\n')
            print(self)
    def reduce_col(self,col: int,print_=True):
        '''
        Reduce una columna en 0 caundo el pivote es 1

        Parámetros:

        col (int): Es la columna que se desea reducir

        print_ (bool) : Determina si se debe imprimir el cambio realizado con la matriz. Por defecto es verdadero
        '''
        for row in range(self.width):
            if row == col: continue
            if self.matrix[row][col] == 0: continue
            self.reduce_row(col,row,print_)

    def is_inconsistent(self,row: int) ->bool:
        '''
        Verifica la inconsistencia de una fila de la matriz.

        Parámetros: 

        row (int): es la fila que se desea verficiar
        '''
        for col in range(self.length):
            if self.matrix[row][col] !=0: return False
        return True

    def __str__(self) -> str:
        return super().__str__()
    

if __name__ == '__main__':
    if len(argv)<2:
        print(f"Uso: {argv[0]} matrix.csv")
        exit(0)
    file_path = argv[1]
    matrix = GaussJordan.create_matrix(file_path)
    if not GaussJordan._valid_matrix(matrix):
        exit(0)
    m = GaussJordan(matrix)
    m.gauss_jordan()
    print(m)
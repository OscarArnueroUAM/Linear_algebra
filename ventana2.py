import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from models.GaussJordan import GaussJordan  # Importa la clase GaussJordan

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.m = GaussJordan(self.Mmtrix)  # Inicializa el objeto GaussJordan como una variable de instancia
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        self.textEdit.setPlainText(str(self.matrix))  # Muestra la matriz inicial
        layout.addWidget(self.textEdit)

        self.btn = QPushButton('Perform Gauss-Jordan Elimination', self)
        self.btn.clicked.connect(self.perform_elimination)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('Gauss-Jordan Elimination')
        self.show()

    def perform_elimination(self):
        if not self.m._valid_matrix(self.matrix):
            self.textEdit.setPlainText("Invalid matrix")
            return
        
        result = self.m.gauss_jordan()  # Asegura que este método devuelva la matriz resultante
        self.textEdit.setPlainText(str(result))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText(str(matrix))
        layout.addWidget(self.textEdit)

        self.btn = QPushButton('Perform Gauss-Jordan Elimination', self)
        self.btn.clicked.connect(self.perform_elimination)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('Gauss-Jordan Elimination')
        self.show()

    def perform_elimination(self):
        if not m._valid_matrix(matrix):  
            self.textEdit.setPlainText("Invalid matrix")
            return
    
        result = m.gauss_jordan(True)
        self.textEdit.setPlainText(str(result))

        
        return matriz
    
if __name__ == '__main__':
    matrix = [[1, 4, -2, 8, 12], [0, 1, -7, 2, -4], [0, 0, 5, -1, 7], [0, 0, 1, 3, -5]]
    app = QApplication(sys.argv)
    ex = App()
    ex.matrix = matrix  # Define la matriz como un atributo de la instancia
    sys.exit(app.exec())

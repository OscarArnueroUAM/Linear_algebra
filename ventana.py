import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from models.GaussJordan import GaussJordan  # Import the GaussJordan class
from main2 import *


    
class MatrixInput(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        # Solicitar el tamaño de la matriz
        self.size_input = QLineEdit(self)
        self.size_input.setPlaceholderText("Ingrese el tamaño de la matriz")
        self.layout.addWidget(self.size_input)

        self.enter_button = QPushButton("Crear campos de matriz", self)
        self.enter_button.clicked.connect(self.create_matrix_fields)
        self.layout.addWidget(self.enter_button)

        # Establecer el layout y mostrar la ventana
        self.setLayout(self.layout)
        self.setWindowTitle('Entrada de Matriz')

    def create_matrix_fields(self):
        try:
            n = int(self.size_input.text())
        except ValueError:
            return
        
        self.matrix_inputs = []
        for i in range(n):
            row = []
            for j in range(n):
                entry = QLineEdit(self)
                entry.setPlaceholderText(f"Elemento [{i},{j}]")
                self.layout.addWidget(entry)
                row.append(entry)
            self.matrix_inputs.append(row)
        
        self.submit_button = QPushButton("Aceptar Matriz", self)
        self.submit_button.clicked.connect(self.accept_matrix)
        self.layout.addWidget(self.submit_button)
    
    def accept_matrix(self):
        n = len(self.matrix_inputs)
        matrix = []
        for row in self.matrix_inputs:
            current_row = []
            for entry in row:
                try:
                    num = int(entry.text())
                    current_row.append(num)
                except ValueError:
                    current_row.append(0)
            matrix.append(current_row)
        
        print("Matriz ingresada por el usuario:")
        for row in matrix:
            print(row)

app = QApplication(sys.argv)
ex = MatrixInput()
ex.show()
sys.exit(app.exec())
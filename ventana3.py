import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QGridLayout
from models.GaussJordan import GaussJordan

class MatrixInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Ingresa el tamaño de la matriz
        self.sizeInput = QLineEdit(self)
        self.sizeInput.setPlaceholderText("Enter the size of the matrix")
        self.layout.addWidget(self.sizeInput)

        # Botón para confirmar el tamaño
        self.confirmSizeBtn = QPushButton('Confirm Size', self)
        self.confirmSizeBtn.clicked.connect(self.setupMatrixInputs)
        self.layout.addWidget(self.confirmSizeBtn)

        # Grid layout para los campos de la matriz
        self.matrixGrid = QGridLayout()
        self.layout.addLayout(self.matrixGrid)

        # Botón para calcular
        self.calculateBtn = QPushButton('Calculate', self)
        self.calculateBtn.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculateBtn)

        # Label para mostrar el resultado
        self.resultLabel = QLabel(self)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)


    # Crea los campos de la matriz
    def setupMatrixInputs(self):
        n = int(self.sizeInput.text())
        self.matrixInputs = []
        for i in range(n):
            row = []
            for j in range(n):
                entry = QLineEdit(self)
                entry.setPlaceholderText(f'Row {i+1} Col {j+1}')
                row.append(entry)
                self.matrixGrid.addWidget(entry, i, j)
            self.matrixInputs.append(row)

    # Calcula la matriz
    def calculate(self):
        try:
            n = len(self.matrixInputs)
            matrix = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(float(self.matrixInputs[i][j].text()))
                matrix.append(row)
            
            if GaussJordan._valid_matrix(matrix):
                m = GaussJordan(matrix)
                m.gauss_jordan(True)
                self.resultLabel.setText(str(m))
            else:
                self.resultLabel.setText("Invalid matrix")
        except Exception as e:
            self.resultLabel.setText(str(e))

# Inicializa la aplicación
app = QApplication(sys.argv)
ex = MatrixInputWidget()
ex.show()
sys.exit(app.exec())

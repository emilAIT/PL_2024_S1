import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont

shtrih = ['0225', '1116', '9394', '3218', '9678', '6869']
tovar = ['ruchka', 'laptop', 'chay', 'majito', 'sprite', 'rezinka']
tsena = [50, 20000, 50, 65, 55, 20]
quantity = [100, 2, 50, 20, 20, 10]

def showLatest():
    result = '\n\n LATEST IN THE DEPO \n\n'
    for s, to, ts, q in zip(shtrih, tovar, tsena, quantity):
        result += f'{s} : {to} : {ts} : {q}\n'
    return result

def kassoviy_check(karzinka):
    total = 0
    result = 'KASSOVIY CHECK\n_______________\n'
    for k in karzinka.split(','):
        for i, sh in enumerate(shtrih):
            to = tovar[i]
            ts = tsena[i]
            if k == sh:
                result += to + ' -> ' + str(ts) + '\n'
                total += ts
                quantity[i] -= 1
    return result + '\n___________\nTOTAL : ' + str(total) + showLatest()


def add(karzinka):
    for k in karzinka.split(','):
        for i, sh in enumerate(shtrih):
            if k == sh:
                quantity[i] += 1
    return showLatest()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.label = QLabel('Shtrih code:')
        self.edit_line = QLineEdit()
        self.button = QPushButton('Calculate')
        self.add = QPushButton('ADD')
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)  # Makes the text area read-only

        # Set the font size
        font = QFont()
        font.setPointSize(14)  # Adjust this value to make the text bigger

        # Apply the font to all elements
        self.label.setFont(font)
        self.edit_line.setFont(font)
        self.button.setFont(font)
        self.text_output.setFont(font)

        # Connect the button click to the function
        self.button.clicked.connect(self.calculate)
        self.add.clicked.connect(self.addbutton)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit_line)
        layout.addWidget(self.button)
        layout.addWidget(self.add)
        layout.addWidget(self.text_output)

        self.setLayout(layout)
        self.setWindowTitle('Shtrih Code Calculator')
        self.setGeometry(200, 200, 400, 300)

    def calculate(self):
        karzinka = self.edit_line.text()
        result = kassoviy_check(karzinka)
        self.text_output.setPlainText(result)

    def addbutton(self):
        karzinka = self.edit_line.text()
        result = add(karzinka)
        self.text_output.setPlainText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

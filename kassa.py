import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont



##################################################

items = {"cola": 50, "shoro":85, "mars":40, "sprite":60, "nan":25, "burger":150, "ruchka":40}
names = {
    "imena":{},
    "summa":{}
}

def getText(name):
    text = f'\t***{name} KARIZDARI***\n\n'
    for i in names['imena'].get(name, []):
        text += f'{i}:\t{items[i]}\n'
    
    text += f'\nTOTAL :\t{names["summa"][name]}'
    return text

def kariz(name, item):
    if item in items:
        names['imena'][name] = names['imena'].get(name, []) + [item] 
        names['summa'][name] = names['summa'].get(name, 0) + items[item]
    return getText(name)

def atai(name, item):
    if item in names['imena'][name]:
        names['imena'][name].remove(item)
        names['summa'][name] -= items[item]
    return getText(name)

def emneler_aldi(name):
    return names["imena"].get(name, ['netu tokogo klienta v baze'])

def kancha_kariz(name):
    return names['summa'].get(name, 'netu tokogo klienta v baze')

def kimkanchakariz():
    text = '\t***KARIZDAR***\n\n'
    total = 0
    for name, summa in names['summa'].items():
        text += f'{name}:\t{summa}\n'
        total += summa
    return text + f'\n\nTOTAL: {total}'



#################################################


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.name_label = QLabel('imya:')
        self.name_edit = QLineEdit()
        self.tovar_label = QLabel('tovar:')
        self.tovar_edit = QLineEdit()

        self.karizButton = QPushButton('Kariz ber')
        self.kanchaButton = QPushButton('Kancha kariz')
        self.emnelerButton = QPushButton('Emnelerdi aldi')
        self.ataiButton = QPushButton('Atai')
        self.karizdarButton = QPushButton('Karizdar')

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)  # Makes the text area read-only

        # Set the font size
        font = QFont()
        font.setPointSize(18)  # Adjust this value to make the text bigger


        self.name_label.setFont(font)
        self.name_edit.setFont(font)
        self.tovar_label.setFont(font)
        self.tovar_edit.setFont(font)
        self.karizButton.setFont(font)
        self.kanchaButton.setFont(font)
        self.emnelerButton.setFont(font)
        self.text_output.setFont(font)
        self.ataiButton.setFont(font)
        self.karizdarButton.setFont(font)


        # Connect the button click to the function
        self.karizButton.clicked.connect(self.kariz)
        self.kanchaButton.clicked.connect(self.kancha)
        self.emnelerButton.clicked.connect(self.emneler)
        self.ataiButton.clicked.connect(self.atai)
        self.karizdarButton.clicked.connect(self.karizdar)


        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.tovar_label)
        layout.addWidget(self.tovar_edit)
        layout.addWidget(self.karizButton)
        layout.addWidget(self.kanchaButton)
        layout.addWidget(self.emnelerButton)
        layout.addWidget(self.ataiButton)
        layout.addWidget(self.karizdarButton)
        layout.addWidget(self.text_output)

        self.setLayout(layout)
        self.setWindowTitle('KASSA')
        self.setGeometry(200, 200, 400, 300)

    def karizdar(self):
        self.text_output.setPlainText(kimkanchakariz())

    def kariz(self):
        name = self.name_edit.text()
        item = self.tovar_edit.text()
        p = kariz(name, item)
        self.name_edit.setText('')
        self.tovar_edit.setText('')
        self.text_output.setPlainText(p)
    
    def atai(self):
        name = self.name_edit.text()
        item = self.tovar_edit.text()
        p = atai(name, item)
        self.name_edit.setText('')
        self.tovar_edit.setText('')
        self.text_output.setPlainText(p)

    def kancha(self):
        name = self.name_edit.text()
        result = name + ' karizi = ' + str(kancha_kariz(name))
        self.text_output.setPlainText(result)

    def emneler(self):
        name = self.name_edit.text()
        result = name + ' algandari \n'
        for i in emneler_aldi(name):
            result += i + '\n'
        self.text_output.setPlainText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

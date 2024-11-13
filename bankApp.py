import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget, QLineEdit, QTextEdit, QFormLayout, QMessageBox)
from PyQt5.QtGui import QFont


# The original classes are included here to ensure the code runs properly
class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.balance = 0
    
    def addBalance(self, amount):
        self.balance += amount
    
    def removeBalance(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name


class Optima:
    def __init__(self):
        self.clients = {}
        self.total = 0
        self.pribl = 0
        self.history = []
    
    def addNewClient(self, name, phone):
        self.clients[phone] = Client(name, phone)
        self.history.append(f'Added new client {name}, {phone}')
    
    def addBalance(self, id, amount):
        if id in self.clients:
            self.clients[id].addBalance(amount)
            self.total += amount
            self.history.append(f'Added balance to {self.clients[id].name} amount of {amount}')
        else:
            raise Exception(f'Client with phone {id} does not exist.')
    
    def transfer(self, from_id, to_id, amount):
        if from_id in self.clients and to_id in self.clients:
            komissia = amount * 0.1 / 100
            self.clients[to_id].addBalance(amount)
            self.clients[from_id].removeBalance(amount + komissia)
            self.pribl += komissia
            from_name = self.clients[from_id].name
            to_name = self.clients[to_id].name
            self.history.append(f'Transfer {from_name} to {to_name} amount of {amount}')
        else:
            raise Exception('One or both clients do not exist.')
    
    def obshiyBalansBanka(self):
        return self.total
    
    def getHistory(self):
        return '\n'.join(self.history)
    
    def getClientBalance(self, id):
        if id in self.clients:
            return self.clients[id].getBalance()
        else:
            raise Exception(f'Client with phone {id} does not exist.')

    def getPribl(self):
        return self.pribl

    def getClients(self):
        result = []
        for key, value in self.clients.items():
            result.append(f'{key}: {value.getName()} : {value.getBalance()}')    
        return '\n'.join(result)


class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.bank = Optima()

    def initUI(self):
        self.setWindowTitle('Optima Bank')
        
        # Set font size
        font = QFont()
        font.setPointSize(14)
        
        # Layout for adding new client
        self.name_input = QLineEdit(self)
        self.name_input.setFont(font)
        self.phone_input = QLineEdit(self)
        self.phone_input.setFont(font)
        self.add_client_btn = QPushButton('Add Client', self)
        self.add_client_btn.setFont(font)
        self.add_client_btn.clicked.connect(self.add_client)

        form_layout = QFormLayout()
        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Phone:', self.phone_input)
        form_layout.addRow(self.add_client_btn)

        # Layout for adding balance
        self.phone_balance_input = QLineEdit(self)
        self.phone_balance_input.setFont(font)
        self.amount_input = QLineEdit(self)
        self.amount_input.setFont(font)
        self.add_balance_btn = QPushButton('Add Balance', self)
        self.add_balance_btn.setFont(font)
        self.add_balance_btn.clicked.connect(self.add_balance)

        balance_layout = QFormLayout()
        balance_layout.addRow('Phone:', self.phone_balance_input)
        balance_layout.addRow('Amount:', self.amount_input)
        balance_layout.addRow(self.add_balance_btn)

        # Layout for transferring balance
        self.from_phone_input = QLineEdit(self)
        self.from_phone_input.setFont(font)
        self.to_phone_input = QLineEdit(self)
        self.to_phone_input.setFont(font)
        self.transfer_amount_input = QLineEdit(self)
        self.transfer_amount_input.setFont(font)
        self.transfer_btn = QPushButton('Transfer', self)
        self.transfer_btn.setFont(font)
        self.transfer_btn.clicked.connect(self.transfer)

        transfer_layout = QFormLayout()
        transfer_layout.addRow('From Phone:', self.from_phone_input)
        transfer_layout.addRow('To Phone:', self.to_phone_input)
        transfer_layout.addRow('Amount:', self.transfer_amount_input)
        transfer_layout.addRow(self.transfer_btn)

        # History display
        self.history_display = QTextEdit(self)
        self.history_display.setFont(font)
        self.history_display.setReadOnly(True)
        self.history_btn = QPushButton('Show History', self)
        self.history_btn.setFont(font)
        self.history_btn.clicked.connect(self.show_history)

        # Layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(balance_layout)
        main_layout.addLayout(transfer_layout)
        main_layout.addWidget(self.history_btn)
        main_layout.addWidget(self.history_display)

        self.setLayout(main_layout)

    def add_client(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        if name and phone:
            self.bank.addNewClient(name, phone)
            QMessageBox.information(self, 'Success', f'Client {name} added successfully!')
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Please enter both name and phone number.')

    def add_balance(self):
        phone = self.phone_balance_input.text()
        amount = self.amount_input.text()
        if phone and amount.isdigit():
            self.bank.addBalance(phone, int(amount))
            QMessageBox.information(self, 'Success', f'Balance of {amount} added to {phone} successfully!')
            self.phone_balance_input.clear()
            self.amount_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a valid phone number and amount.')

    def transfer(self):
        from_phone = self.from_phone_input.text()
        to_phone = self.to_phone_input.text()
        amount = self.transfer_amount_input.text()
        if from_phone and to_phone and amount.isdigit():
            try:
                self.bank.transfer(from_phone, to_phone, int(amount))
                QMessageBox.information(self, 'Success', f'Transferred {amount} from {from_phone} to {to_phone} successfully!')
                self.from_phone_input.clear()
                self.to_phone_input.clear()
                self.transfer_amount_input.clear()
            except Exception as e:
                QMessageBox.warning(self, 'Error', str(e))
        else:
            QMessageBox.warning(self, 'Error', 'Please enter valid phone numbers and amount.')

    def show_history(self):
        history = self.bank.getHistory()
        self.history_display.setText(history)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BankApp()
    ex.show()
    sys.exit(app.exec_())

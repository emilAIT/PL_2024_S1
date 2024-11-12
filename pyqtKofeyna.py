import sys
from PyQt5 import QtWidgets, QtGui
from collections import defaultdict

GLOBAL_FONT = QtGui.QFont('Arial', 14)

class Kofeyna:
    def __init__(self):
        self.personal = None
        self.history = []
        self.purchase_prices = defaultdict(int)
        self.sale_prices = defaultdict(int)
        self.quantity = defaultdict(int)
        self.total = 0
        self.kassa = 0
        self.history_purchase = []

    def getHistory(self):
        return '\n'.join(self.history)

    def sellItems(self, item):
        sale_price = self.sale_prices.get(item, 0)
        purchase_price = self.purchase_prices.get(item, 0)
        if self.quantity[item] > 0:
            self.quantity[item] -= 1
        else:
            return 'Item does not exist'
        self.total += sale_price - purchase_price
        self.kassa += sale_price
        self.history.append(f'{item} : {sale_price} : {self.personal}')
        return f'Sold {item} for {sale_price}'

    def getProfit(self):
        return self.total
    
    def getKassa(self):
        return self.kassa

    def getCurrentPersonal(self):
        return self.personal
    
    def changePersonal(self, personal):
        self.personal = personal

    def addItem(self, item, quantity, price):
        self.purchase_prices[item] = price
        self.sale_prices[item] = price * 1.25
        self.quantity[item] += quantity
        self.history_purchase.append(f'{item} : {price} : {quantity} : {self.personal}')
    
    def getPurchaseHistory(self):
        return '\n'.join(self.history_purchase)

    def getItems(self):
        arr = []
        for item, quantity in self.quantity.items():
            if quantity > 0:
                arr.append(f'{item} : {quantity}')
        return '\n'.join(arr)

class KofeynaApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.kofeyna = Kofeyna()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kofeyna Management System')
        self.setGeometry(100, 100, 500, 500)

        # Labels
        self.personal_label = QtWidgets.QLabel('Current Personal:', self)
        self.personal_label.setFont(GLOBAL_FONT)
        self.personal_label.move(20, 20)
        
        self.personal_name = QtWidgets.QLabel('', self)
        self.personal_name.setFont(GLOBAL_FONT)
        self.personal_name.move(150, 20)
        
        # Change Personal
        self.personal_input = QtWidgets.QLineEdit(self)
        self.personal_input.setFont(GLOBAL_FONT)
        self.personal_input.setPlaceholderText('Enter personal name')
        self.personal_input.setGeometry(20, 50, 200, 30)

        self.change_personal_btn = QtWidgets.QPushButton('Change Personal', self)
        self.change_personal_btn.setFont(GLOBAL_FONT)
        self.change_personal_btn.setGeometry(230, 50, 150, 30)
        self.change_personal_btn.clicked.connect(self.changePersonal)

        # Add Item
        self.item_input = QtWidgets.QLineEdit(self)
        self.item_input.setFont(GLOBAL_FONT)
        self.item_input.setPlaceholderText('Item Name')
        self.item_input.setGeometry(20, 100, 120, 30)

        self.quantity_input = QtWidgets.QLineEdit(self)
        self.quantity_input.setFont(GLOBAL_FONT)
        self.quantity_input.setPlaceholderText('Quantity')
        self.quantity_input.setGeometry(150, 100, 80, 30)

        self.price_input = QtWidgets.QLineEdit(self)
        self.price_input.setFont(GLOBAL_FONT)
        self.price_input.setPlaceholderText('Price')
        self.price_input.setGeometry(240, 100, 80, 30)

        self.add_item_btn = QtWidgets.QPushButton('Add Item', self)
        self.add_item_btn.setFont(GLOBAL_FONT)
        self.add_item_btn.setGeometry(330, 100, 100, 30)
        self.add_item_btn.clicked.connect(self.addItem)

        # Sell Item
        self.sell_item_input = QtWidgets.QLineEdit(self)
        self.sell_item_input.setFont(GLOBAL_FONT)
        self.sell_item_input.setPlaceholderText('Item to Sell')
        self.sell_item_input.setGeometry(20, 150, 200, 30)

        self.sell_item_btn = QtWidgets.QPushButton('Sell Item', self)
        self.sell_item_btn.setFont(GLOBAL_FONT)
        self.sell_item_btn.setGeometry(230, 150, 100, 30)
        self.sell_item_btn.clicked.connect(self.sellItem)

        # Show History
        self.history_btn = QtWidgets.QPushButton('Show Sales History', self)
        self.history_btn.setFont(GLOBAL_FONT)
        self.history_btn.setGeometry(20, 200, 150, 30)
        self.history_btn.clicked.connect(self.showHistory)

        # Show Items
        self.items_btn = QtWidgets.QPushButton('Show Available Items', self)
        self.items_btn.setFont(GLOBAL_FONT)
        self.items_btn.setGeometry(200, 200, 150, 30)
        self.items_btn.clicked.connect(self.showItems)

        # Text Browser for Output
        self.output_browser = QtWidgets.QTextBrowser(self)
        self.output_browser.setFont(GLOBAL_FONT)
        self.output_browser.setGeometry(20, 250, 450, 200)

    def changePersonal(self):
        personal = self.personal_input.text()
        if personal:
            self.kofeyna.changePersonal(personal)
            self.personal_name.setText(personal)
            self.output_browser.append(f'Personal changed to: {personal}')
        self.personal_input.clear()

    def addItem(self):
        item = self.item_input.text()
        quantity = self.quantity_input.text()
        price = self.price_input.text()
        if item and quantity.isdigit() and price.isdigit():
            self.kofeyna.addItem(item, int(quantity), int(price))
            self.output_browser.append(f'Added {quantity} of {item} at price {price}')
            self.item_input.clear()
            self.quantity_input.clear()
            self.price_input.clear()
            
        else:
            self.output_browser.append('Invalid input for adding item')

    def sellItem(self):
        item = self.sell_item_input.text()
        if item:
            result = self.kofeyna.sellItems(item)
            self.output_browser.append(result)
        self.sell_item_input.clear()

    def showHistory(self):
        history = self.kofeyna.getHistory()
        self.output_browser.append('Sales History:\n' + history)

    def showItems(self):
        items = self.kofeyna.getItems()
        self.output_browser.append('Available Items:\n' + items)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = KofeynaApp()
    ex.show()
    sys.exit(app.exec_())

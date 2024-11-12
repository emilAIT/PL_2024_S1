from collections import defaultdict
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

    def sellItems(self,item):
        sale_price = self.sale_prices.get(item, 0)
        purchase_price = self.purchase_prices.get(item, 0)
        if self.quantity[item] > 0:
            self.quantity[item] -= 1
        else:
            print('Item does not exist')
        self.total += sale_price - purchase_price
        self.kassa += sale_price
        self.history.append(f'{item} : {sale_price} : {self.personal}')

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

    
    




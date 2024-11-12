from kofeyna import Kofeyna
from collections import defaultdict

class Salma(Kofeyna):
    def __init__(self):
        super().__init__()
        self.prodovets = defaultdict(list)
    
    def sellItems(self, item):
        super().sellItems(item)
        price = self.sale_prices.get(item, 0)
        self.prodovets[self.personal].append(f'{item}: {price}')
    
    def getPersonalSales(self, name):
        return '\n'.join([name + " SOLD ITEMS "] + self.prodovets[name])
    
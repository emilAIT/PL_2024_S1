# dannie nomer, rekveziti
# perevod
# istoria
# polzovateli
# balans
# deposit
# kredit
# obmen
# obshiy balans banka
# pribl

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
    
    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

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
        self.clients[id].addBalance(amount)
        self.total += amount
        self.history.append(f'Added balance to {self.clients[id].name} amount of {amount}')
    
    def transfer(self, from_id, to_id, amount):
        komissia = amount * 0.1 / 100
        self.clients[to_id].addBalance(amount)
        self.clients[from_id].removeBalance(amount + komissia)
        self.pribl += komissia
        from_name = self.clients[from_id].name
        to_name = self.clients[to_id].name
        self.history.append(f'Transfer {from_name} to {to_name} amount of {amount}')
    
    def obshiyBalansBanka(self):
        return self.total
    
    def getHistory(self):
        return '\n'.join(self.history)
    
    def getClientBalance(self, id):
        return self.clients[id].getBalance()

    def getPribl(self):
        return self.pribl

    def getClients(self):
        result = []
        for key, value in self.clients.items():
            result.append(f'{key}: {value.getName()} : {value.getBalance()}')    
        return '\n'.join(result)
    
    





    


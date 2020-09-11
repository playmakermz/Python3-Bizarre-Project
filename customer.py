from atm_card import ATMCard
class Customer():

    def __init__(self,id, defaultPin = 123, defaultBalance=10000):
        self.id = id
        self.Pin = defaultPin
        self.Balance = defaultBalance

    
    def ambilId(self):
        return self.id

    def ambilPin(self):
        return self.Pin

    def ambilBalance(self):
        return self.Balance

    def ambiluang(self, nominal):
        self.Balance -= nominal

    def simpanuang(self, nominal):
        self.Balance += nominal



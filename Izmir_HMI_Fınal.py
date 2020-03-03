import random

class MutualFund:
    def __init__(self, ticker):
        self.ticker = ticker
        
    def name_teller(self, MutualFund):
        return self.ticker
    
        
class Stock:
    def __init__(self, price, ticker):
        self.price = price
        self.ticker = ticker
        print ({price , ticker})
        
    def price_teller(self, Stock):
        return self.price

    def name_teller(self, Stock):
        return self.ticker

class Portfolio(Stock, MutualFund):
    def __init__(self, cash = 0):
        self.cash = cash
        self.stock = {}
        self.mutualfund = {}

    def __repr__(self):
        return "cash: %s \nstock: %s \nmutual funds: %s" % (self.cash, self.stock, self.mutualfund)
     
    def __str__(self):
        return "cash: %s \nstock: %s \nmutualfunds: %s" % (self.cash, self.stock, self.mutualfund)
    
    def addCash(self, cash_to_add):
        self.cash += cash_to_add
        print("your current cash balance:"),
        print(self.cash)
        
    def withdrawCash(self, cash_to_withdraw):
        self.cash -= cash_to_withdraw
        print("your current cash balance:"),
        print(self.cash)
    
    def buyStock(self, share, Stock):
        self.sum = share * Stock.price_teller(Stock)
        print("total cost:")
        print(self.sum)
        print("Would you like to proceed to buy?")
        print("To proceed, type 'davay' and press enter. To cease transaction just press enter")
        decision = input("> ")
        if decision == "davay":
            if Stock.name_teller(Stock) in self.stock:
                self.stock.update({Stock.name_teller(Stock) : (share + (self.stock[Stock.name_teller(Stock)]))})
            else:
                self.stock.update({Stock.name_teller(Stock) : share})
        else:
            print("okay I respect your decision...")
        print(self.stock)
        self.cash-= self.sum
        print("current cash balance:")
        print(self.cash)
    
    def sellStock(self, ticker, share): 
        self.stock.update({ticker : ((self.stock[ticker]) - share)})
        firstprice = self.stock[ticker]
        self.sellprice = share * random.uniform(0.5 , 1.5) * firstprice
        print("total revenue:")
        print(self.sellprice)
        print("Would you like to proceed?")
        print("To proceed, type 'davay' and press enter. To cease transaction just press enter")
        decision = input("> ")
        if decision == "davay":
            self.cash += self.sellprice
        else:
            print("okay I respect your decision...")
        print("current cash balance:")
        print (self.cash)
        
    def buyMutualFund(self, share, MutualFund):
        self.share = share
        print("total cost:")
        print(self.share)
        print("Would you like to proceed to buy?")
        print("To proceed, type 'davay' and press enter. To cease transaction just press enter")
        decision = input("> ")
        if decision == "davay":
            if MutualFund.name_teller(MutualFund) in self.mutualfund:
                self.mutualfund.update({MutualFund.name_teller(MutualFund) : (share + (self.mutualfund[MutualFund.name_teller(MutualFund)]))})
            else:
                self.mutualfund.update({MutualFund.name_teller(MutualFund) : share})
            print(self.mutualfund)
            self.cash-= self.share
            print("current cash balance:")
            print(self.cash)

        else:
            print("okay I respect your decision...")
    def sellMutualFund(self, ticker, share):
        self.mutualfund.update({ticker : ((self.mutualfund[ticker]) - share)})
        self.sellprice = share * random.uniform(0.9 , 1.2)
        print("total revenue:")
        print(self.sellprice)
        print("Would you like to proceed?")
        print("To proceed, type 'davay' and press enter. To cease transaction just press enter")
        decision = input("> ")
        if decision == "davay":
            self.cash += self.sellprice
        else:
            print("okay I respect your decision...")
        print("current cash balance:")
        print (self.cash)
        
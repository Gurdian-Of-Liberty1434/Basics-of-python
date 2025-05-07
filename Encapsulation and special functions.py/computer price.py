class Computer:
    def __init__(self):
        self.__max_price=90000

    def sell(self):
        print("The selling price:{}",format(self.__max_price))

    def setmaxprice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(100000)
c.sell()

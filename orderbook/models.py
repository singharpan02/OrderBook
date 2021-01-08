import random

a_orders = {11.38: 400, 11.39: 1600, 11.4: 1205, 11.41: 1400, 11.42: 900}
b_orders = {11.36: 2700, 11.35: 1100, 11.34: 1100, 11.33: 1600, 11.32: 700}


class Order:

    def __init__(self, price, size):
        self._price = price
        self._size = size
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
    
    def __str__(self):
        return f'Order(price: {self._price}, size: {self._size})'


def get_ask_orders():
    start = 11.42
    while start < 12.5:
        start = round(start + 0.01, 2)
        a_orders[start] = random.randint(100, 5000)
    askorders = []
    return [Order(price, size) for price, size in a_orders.items()]
    


def get_bid_orders():
    start = 11.32
    while start >= 10.2:
        start = round(start - 0.01, 2)
        b_orders[start] = random.randint(100, 5000)
    return [Order(price, size) for price, size in b_orders.items()]

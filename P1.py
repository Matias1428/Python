from traceback import print_exception


class Item:
    def __init__(self,name,price,quantity):
        print("I am created!")
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self,x,y):
        return x*y

item1= Item("Phone",110,5)
item2= Item("Pc",200,4)

print(item1.name)


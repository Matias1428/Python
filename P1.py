from traceback import print_exception


class Item:
    pay_rate= 0.8 # The pay rate after 20% discount
    def __init__(self,name: str,price: float,quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero"

        
        print("I am created!")
        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price=self.price*Item.pay_rate 

#item1= Item("Phone",110)
item1= Item("Phone",1)
item2= Item("Pc",200,4)

item2.has_numpad=False;

print(item2.calculate_total_price())  
print(Item.pay_rate)
print(Item.__dict__)
print(item1.__dict__)
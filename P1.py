from traceback import print_exception
import csv

class Item:
    pay_rate= 0.8 # The pay rate after 20% discount
    all=[]
    def __init__(self,name: str,price: float,quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero"
        
        print("I am created!")
        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price=self.price*self.pay_rate

    #Class method
    @classmethod     
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader= csv.DictReader(f)
            items=list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
                )
            

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

#item1= Item("Phone",110)
#item1= Item("Phone",1,1)
#item2= Item("Pc",2000,4)
#item3= Item("Laptop",200,40)
#item4= Item("cable",20,5)
#item5= Item("keyboard",10,20)


#item2.has_numpad=False;

#print(item2.calculate_total_price())  
#print(Item.pay_rate)
#print(Item.__dict__) # Shows all the 
#print(item1.__dict__)

#for instances in Item.all:
#    print(instances.name)
Item.instantiate_from_csv()
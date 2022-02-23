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

    @staticmethod        
    def is_integer(num):
        #We will count out the floats that are point zero 
        if isinstance(num,float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()
print(Item.is_integer(7.4))

class Phone(Item):
    def __init__(self,name: str,price: float,quantity=0, broken_phones=0):
        super().__init__(name,price,quantity)

        assert broken_phones >=0, f"Broken Phones {broken_phones} is not grater than zero0"
       
    

phone1= Phone("jscPhonev10",500,5,1)
phone2= Phone("jscPhonev20", 700, 5,1)

print(Item.all)
print(Phone.all)

import imp
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)


item1=Item("Muy", 750)


item1.name="otherName"
print(item1.name)

#Tuples: ordered, inmutable, allows duplicate elements
mytuple=("Max", 28,"Boston")
mytuple2=("Max2",)

for i in mytuple:
    print(i)

my_list= list(mytuple)
mytuple=tuple(my_list)


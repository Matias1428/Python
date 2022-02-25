
#Tuples: ordered, inmutable, allows duplicate elements
mytuple=("Max", 28,"Boston")
mytuple2=("Max2",)

for i in mytuple:
    print(i)

my_list= list(mytuple)
mytuple=tuple(my_list)

#Dictionary: Key-value pairs, unordered, mutable
mydict={"name":"Max", "age":28}
print(mydict)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key,value in mydict.items():
    print(key,value)

# Sets: unordered, mutable, no duplicates
myset={1,2,3,1,3}
myset2=set()
myset.add(4)
myset.add(5)

myset.discard(2)
print(myset)

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print(u)

i=evens.intersection(primes)
print(i)

diff= primes.difference(evens)
print(diff)

diff2= primes.symmetric_difference(evens)
print(diff2)

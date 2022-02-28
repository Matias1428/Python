#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterartors
from itertools import product
from re import A
from timeit import repeat
from traceback import print_tb
a=[1,2]
b=[3,4]
prod=product(a,b, repeat=2)
print("Product: ",list(prod))

from itertools import permutations

c=[1,2]
d=[3,4]
perm=permutations(c,2)
print("Permutation: ",list(perm))

from itertools import combinations, combinations_with_replacement

e=[1,2,3,4]
comb=combinations(e, 2)
print("Combination: ",list(comb))

comb_wr=combinations_with_replacement(e,2)
print("combinations_with_replacement",list(comb_wr))

from itertools import accumulate
a=[1,2,3,4]
acc=accumulate(a)
print("accumulate",list(acc))


from itertools import groupby
def smaller_than_3(x):
    return x<3


a=[1,2,3,4]
group_obj= groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key,list(value))

persons= [{'name':'Tin','age':25},{'name':'Manuel','age':25},{'name':'Guadalupe','age':19},{'name':'Sofia','age':19}]

group_obj2= groupby(persons, key=lambda x:x['age'])
for key, value in group_obj2:
    print(key, list(value))


from itertools import count, cycle, repeat
#infite cicles
a=[1,2,3]
for i in count(10):
    print(i)
    if i==15:
        break


# Lambda arguments: expresions
add110= lambda x:x+10
print(add110(3))

mult=lambda x,y:x*y
print("Lamda mult ",mult(2,4))

#map(func, seq)
a=[1,2,3,4,5]
b=map(lambda x:x*2, a)
print(list(b))

c=[x*2 for x in a]
print(c)


# filter(func, seq)
a=[1,2,3,4,5,6]
b=filter(lambda x:x%2==0, a)
print(list(b))

c=[x for x in a if x%2==0]
print(c)

# reduce(func,seq)
from functools import reduce
a=[1,2,3,4,5,6]
product_a= reduce(lambda x,y:x*y,a)
print(product_a)
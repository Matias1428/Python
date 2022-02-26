#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterartors
from itertools import product
from re import A
from timeit import repeat
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
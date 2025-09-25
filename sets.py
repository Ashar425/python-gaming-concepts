#making the set
myset= set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(5)
myset.add(1)

#printing the set
print(myset)

#removing 2 from set so it does`nt come in output
myset.remove(2)

#discarding 4 
myset.discard(4)


"""
set operations
1-union - addition of sets
2- intersection
3- difference  
4- symmetric difference
"""

a={1,2,3,4,5,6}
b={4,5,6,7,8}

print(a.union(b))
###print(a | b)

#printing the intersecion så the output is same in sets
print(a.intersection(b))
print(a&b)

#printing the difference b to a
print(a.difference(b))
print(b-a)

#only printing the difference of the sets
print(a.symmetric_difference(b))
print(a ^ b)


print(a.union(b))
print(a&b)
print(a-b)
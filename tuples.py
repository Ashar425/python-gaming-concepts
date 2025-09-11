student_details=('Ashar',12)

packing_details=("33","apartment 3b","herlev","hovedstaden","123456")
for x in packing_details:
    print(x,end=" ")

houseno,apartment,city,state,pin=packing_details

print()
print("House No-",houseno)
print("Apartment-",apartment)
print(city)
print(state)
print(pin)

tuple1="dog",3,4,6,2
print (tuple1)

ntuple=(("apple","mango","orange"),("red","yellow","orange"),(20,40,60))

print(ntuple[0][2])
print(ntuple[1][1])

mytuple=('p','r','o','g','r','a','m','i','z')

print(mytuple[1:4])
print(mytuple[:-7])

print(mytuple[7:])
print(mytuple[:])
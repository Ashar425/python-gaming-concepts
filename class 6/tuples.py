student_details=('Ashar',12)

#making the packing details
packing_details=("33","apartment 3b","herlev","hovedstaden","123456")
for x in packing_details:
    print(x,end=" ")

#the packing details
houseno,apartment,city,state,pin=packing_details

#printing the packing details
print()
print("House No-",houseno)
print("Apartment-",apartment)
print(city)
print(state)
print(pin)

#making tuple1
tuple1="dog",3,4,6,2
print (tuple1)

#making a nestletuple (ntuple)
ntuple=(("apple","mango","orange"),("red","yellow","orange"),(20,40,60))

#printing ntuple
print(ntuple[0][2])
print(ntuple[1][1])

#making mytuple
mytuple=('p','r','o','g','r','a','m','i','z')

#printing mytuple
print(mytuple[1:4])
print(mytuple[:-7])

print(mytuple[7:])
print(mytuple[:])

ntuple=(["apple","mango"],["red","yellow"],["orange","pink"])

ntuple[0][1]="watermelon"
print(ntuple)

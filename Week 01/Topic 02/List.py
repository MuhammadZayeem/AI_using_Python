Fruits = ["Apple", "Strawberry", "Cherry", "Date", "Banana"]
print(Fruits)
print(Fruits[-1])
print(Fruits[-2])

Fruits.append("Orange")  #Add item to end
print(Fruits)
Fruits.insert(2,"Mango") #Add item to index
print(Fruits)
Fruits.remove("Date")    #Remove an item
print(Fruits)
Fruits.pop()             #Remove from last
print(Fruits)
Fruits.sort()
print(Fruits)            #Sorts in order

#Loop List
for fruit in Fruits:
   print(fruit)

Numbers=[1,3,2,4,4,3,8,0,9,7,65]
print(Numbers)
for number in Numbers:
   print(number)

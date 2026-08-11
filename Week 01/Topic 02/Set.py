my_set={1,3,5,7,9}
my_set2={2,4,6,8,10}
print(my_set)
print(my_set2)

my_set.add(11)
my_set2.add(0)
print(my_set)
print(my_set2)

my_set.remove(1)
my_set2.remove(10)
print(my_set)
print(my_set2)

print(my_set.intersection(my_set2))
print(my_set.difference(my_set2))
print(my_set.union(my_set2))
for i in my_set:
    print(i)
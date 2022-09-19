b = set()
print(type(b))
print(b)
# Adding values to an empty set

# Adding a value repeatedly does not change a set 
b.add(4)
b.add(4)
b.add(4)
b.add(5)
b.add(9)
b.add(9)
print(b)

# We can not add list and dictionary under set 
# b.add([4, 7, 1, 2, 5]) # TypeError: unhashable type: 'list' i.e List ko set k andar nahi daal sakte hai but tuples ko daal sakte hai.
# print(b) 
b.add((4, 7, 1, 2, 5))
# b.add({2, 3}) # TypeError: unhashable type: 'set' same resion as above
print(b)
print(b)
print(len(b)) # Print the length of this set
b.remove(9)
print(b)
b.pop() # Remove random value from the set
print(b)
# b.clear()
# print(b)
b.union({8, 6})
print(b)
b.intersection({8, 6})
print(b)
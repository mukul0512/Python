l1 = [1, 8, 4, 7, 2, 5]
print(l1)

l1.sort() # Tis is sorting the list
print(l1)

l1.reverse() # This is reversing the list
print(l1)

l1.append(10) # Add 10 at the end of the list
print(l1)

l1.append(11) # Add 11 at the end of the list
print(l1)

l1.insert(0, 100) # Add 100 at the index 0th of the list 
print(l1)

l1.insert(3, 100) # Add 100 at the index 3rd of the list 
print(l1) # Output is [100, 8, 7, 100, 5, 4, 2, 1, 10, 11]

l1.pop(2) # Remove element at index 2 that is 7 
print(l1) # Output is [100, 8, 100, 5, 4, 2, 1, 10, 11]

l1.remove(4) # Remove 4 from the list 
print(l1) # So the output is [100, 8, 100, 5, 2, 1, 10, 11]
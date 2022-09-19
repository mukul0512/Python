# Creating a tuples using ()  
t = (1, 2, 5, 7, 9, 4)
t1 = () # an empty tuple   
print(t1) 
# t1 = (1) # Wrong way to declare a tuple with single element

t1 = (1,) # Tuple with single element
print(t1) 

# We can printing the elements of tuple 
print(t[0])

# Tuples are immutable i.e. (Cannot change).
# We can not update the value of tuples. 
# t[0] = 17 # TypeError: 'tuple' object does not support item assignment.
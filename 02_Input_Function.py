a = input("Enter your name here: ") # by default input is a string data type
print("Your name is ", a)
print("The data type of a is ", type(a))

b = input("Enter the value of b here ")
print("The data type of b before typecasting is ", type(b))
b = int(b)
print("The data type of b after typecasting is ", type(b))
print("The value of b is ", b)

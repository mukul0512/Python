a = "1998"
# a = "1998mukul" # ValueError: invalid literal for int() with base 10: '1998mukul'
print("The value of a before typecasting is ", a)
print("The data type of a is ", type(a))
# print("The value of a is ", a + 2) # TypeError: can only concatenate str (not "int") to str
a = int(a)
print("The data type of a is ", type(a))
print("The value of a after typecasting is ", a + 2)

b = 1998
print("The value of b is ", b)
print("The data type of b is ", type(b))
print("The value of b before typecasting is ", b + 2)

b = str(b)
print("The data type of b is ", type(b))
# print("The value of b after typecasting is ", b + 2) # TypeError: can only concatenate str (not "int") to str
print("The value of b is ", b)

c = 1998.123
print("The value of c is ", c)
print("The data type of c is ", type(c))
print("The value of c before typecasting is ", c + 2)
c = float(c)
print("The data type of c is ", type(c))
print("The value of c after typecasting is ", c + 2)
a = input("Enter your 1st number: ")
a = int(a)
b = input("Enter your 2nd number: ")
b = int(b)
resG = a > b
resL = a < b
resGE = a >= b
resLE = a <= b
resEE = a == b
resN = a != b
print("The result of comparing a > b is: ", resG)
print("The result of comparing a < b is: ", resL)
print("The result of comparing a >= b is: ", resGE)
print("The result of comparing a <= b is: ", resLE)
print("The result of comparing a == b is: ", resEE)
print("The result of comparing a != b is: ", resN)
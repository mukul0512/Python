greeting = "Good Morning!, "
name = "Mukul"
print(type(name))
res = greeting + name # Concatenating two strings
# print(greeting + name)
print(res)

# String Slicing
myName = "Karnwal"
print(myName)
print(type(myName))
print(myName[0]) # [0]
print(myName[0: 3]) # [0 1 2]
print(myName[:4]) # Automatically opted the minimum index
print(myName[0: 4]) # [0 1 2 3]
print(myName[0:]) # Automatically opted the last index, same as myName[0: 7]
print(myName[0: 7]) # [0 1 2 3 4 5 6]
# print(myName[7]) # IndexError: string index out of range

print(myName[-7:-1]) # Same as myName[0: 6]
print(myName[1:4:1]) # kuch skip nahi hoga [1 2 3]
print(myName[1:4:2]) # 1 ko print karega fir 1 ko skip karega [1 3]
print(myName[0::4]) # 0 ko print karega fir 3 ko skip karega and 4 ko print karega
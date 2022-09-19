myDict = {
    "Fast": "Is a web developer. ",
    "Mukul": "A Developer.",
    "Marks": [90, 98, 91, 95, 89, 96],
    "yourDict": {
        'Karnwal': 'Haridwar'
    },
    1: 2
}

# Dictionary Methods 
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {
    "Fun": "Trip",
    "Venue": "Cristal World"
}
print(myDict.update(updateDict)) # By adding key value pair from updateDict  we can update the dictionary

print(list(myDict.keys())) # Prints the key of a dictionary
print(list(myDict.values())) # Prints the values of a dictionary
print(list(myDict.items())) # Prints the (keys, value) for all contents of a dictionary

print(list(myDict))
updateDict = {
    "Friends": "Cool",
    "Name": "Narayan"
}
# print(list(myDict.update(updateDict)))  # TypeError: 'NoneType' object is not iterable


print(myDict.get("Mukul2")) # No error although returns None as Mukul2 is not present in the dictionary
print(myDict["Mukul2"]) # KeyError: 'Mukul2' as Mukul2 is not present in the dictionary 
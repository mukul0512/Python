myDict = {
    "Fast": "In a web developer. ",
    "Mukul": "A Developer.",
    "Marks": [90, 98, 91, 95, 89, 96],
    "yourDict": {
        'Karnwal': 'Haridwar'
    }
}

print(myDict['Fast'])
print(myDict['Mukul'])
print(myDict['Marks'])
myDict['Marks'] = [45, 33]
myDict['Marks'] = [44, 33]
myDict['Marks'] = [33, 33]
print(myDict['Marks'])
print(myDict['yourDict'])
print(myDict['yourDict']['Karnwal'])
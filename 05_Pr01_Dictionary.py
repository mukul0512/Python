myDict = {
    "Mukul": "Khilna",
    "Piyush": "Amrit",
    "Vishakha": "Nakshaktra"
}
print("Options are: ", myDict.keys())
a = input("Enter the english word here: \n")
# print("The meaning of your word is:", myDict[a]) # KeyError: 'Any Unknown Word other then mention'
print("The meaning of your word is:", myDict.get(a)) # Will not through an error even if the key is not present in the dictionary while using this gives the output i.e. The meaning of your word is: None 
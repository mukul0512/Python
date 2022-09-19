story = "once upon a time there was a web developer named Karnwal and Karnwal has the great urge to learn new things and knows how to utilized time."

# String Functions 
print(len(story))
print(story.endswith("utilized time.")) # Return True
print(story.endswith("Once upon a time")) # Return False
print(story.startswith("Once upon a time")) # Return True
print(story.count("K")) # There are only one capital K so return 1
print(story.count("o")) # 3 small o are there
print(story.count("n")) # 8 n are there
print(story.count("time")) # we can count words also
print(story.capitalize())
print(story.find("Karnwal"))    
print(story.find("once"))    
print(story.find("upon"))
print(story.replace("Karnwal", "Mukul"))
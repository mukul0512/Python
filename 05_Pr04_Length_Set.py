s = {20, 20.0, "20"} # Under this case compiler opt only one value to interpret result i.e 20 and 20.0 counts only one
print(len(s))   # So the length of this set is 2 not 3.

s2 = {20, 20.5, "20"}
print(len(s2))   # the length of this set is 3.
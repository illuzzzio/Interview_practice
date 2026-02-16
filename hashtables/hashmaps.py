# Hasmaps -- basically python dictionaries 
d = {"pranjal":1, "steve":2, "robert":3}
print(d)

# adding 

d["pranjal"] = 4 
print(d)

#{'pranjal': 1, 'steve': 2, 'robert': 3}
# {'pranjal': 4, 'steve': 2, 'robert': 3}


# check presence of key in the dictionary 

if "pranjal" in d:
    print(True)
print(False)

# check the value corresponding to a key in a dictionary 

print(d["robert"])


# how do we loop over key value pair in the dictionary :


for key, val in d.items():
    print(f'key {key} val {val}')

    # Default dict 

from collections import defaultdict 

default = defaultdict(int)
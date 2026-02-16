#HashSets:
s = set()
print(s)

#adding 
s.add(1)
s.add(2)
print(s)

# lookup , if th item is in the set :
if 1 not  in s:
    print(True)
print(False)

# removing elements from the set :

s.remove(1)
print(s)

# example :
string = "aaaaabbbbbbbbbbccc"

n = len(string)
g = len(set(string))

if(n==g):
    print("No duplicates")
print("duplicates found")



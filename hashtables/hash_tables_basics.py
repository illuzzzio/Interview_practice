# hash tables : tthis topic mainly hum hash tables ke basic concepts ko samjhenge aur unke operations ko implement karenge. and it consists of hash fucntions , sets and maps..  worst time complexity is O(n) and avg is O(1)

# it basically works on the principle of key:value pairs

# linear probing -- if the collision occurs, we basically , keep on checking the next place to assigned... and keep looking untill we get an empty space to insert the given element , when we delete an element , dont leave the empty space , just mark it , so that the linear probing chain, doesn't get break...


# What data types are hashable ? 
# string , int , tuples

# What is not hashable :
#arrays , dict , dict -- are actually hashmaps , but cant be hashed 
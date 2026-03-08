array = [1,2,3,4,6,5]

def contain_duplicates(array):
    n = len(array)
    for i in range(0,n):
        for j in range(i+1,n):
            if(array[i]==array[j]):
                return True
    return False

# print(contain_duplicates(array))  # this is however a brute force solution with time complexity of O(n)^2


# more optimal solution 

def optimal(array):
    new_array = set(array)

    if(len(array)==len(new_array)):
        return False 
    return True 

print(optimal(array))# this is a bettter soltuion 


# input nums = [1,2,2,3]
# output = true 

array = [1,2,3,4,5,6,5]
def contains_duplicates(array):
    n = len(array)
    for i in range(0,n):
        for j in range(i+1,n):
            if(array[i]==array[j]):
                return True 
            # return False -- wrong becasue thi will return false after first comparision 
    return False 
print(contains_duplicates(array))


# more optimise solution 

list = [12,43,54,65,76,-12,21,-12]
def optimal(list):
    cut = set(list)
    if(len(cut)==len(list)):
        return False 
    else:
        return True
print(optimal(list))
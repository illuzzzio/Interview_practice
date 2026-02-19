
# this search method can be only applied on sortedarray
array = [1,2,3,4,5,6,7,8,21,43,65]

def Binary_Search(array,element):
    lefty = 0
    n = len(array)
    righty = n-1
    while(righty>=lefty):
        mid = (righty+lefty)//2
        if(element==array[mid]):
            return mid
        elif(element<array[mid]):
            right = mid -1
        else:
            left = mid+1
    return -1
print(Binary_Search(array,6))
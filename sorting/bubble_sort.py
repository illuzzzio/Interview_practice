array = [1,2,36,5,7,8,21,45,32,43,21,43]

def bubble_sort(array):
    n = len(array)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(array[j]>array[j+1]):
                temp = array[j]
                array[j]= array[j+1]
                array[j+1]= temp
    return array

print(bubble_sort(array))

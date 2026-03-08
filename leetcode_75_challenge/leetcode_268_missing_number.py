
array = [3,0,1]

# concept = sum of first n natural number upto to the length given - real sum of elemenets , thsi will help us to return true missign element 


def missing_num(array):
    n = len(array)

    natural_sum = n*(n+1)//2 # 12/2 == 6   # in pytho nwe use // instead of / , we we want a integer answer , not a decimal point answer 
    sum = 0
    for i in range(0,n):
        sum+=array[i]
    return natural_sum - sum

print(missing_num(array))


    
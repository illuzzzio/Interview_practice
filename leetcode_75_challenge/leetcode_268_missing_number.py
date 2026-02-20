# input nums = [3,0,1]
# output = 2

# my approach = sum of natural numebers upto  a certain lenght- the real sum 

array =  [3,0,1]

def missing_num(array):
    n = len(array)
    natural= n*(n+1)//2 # 6 in this case 
    count = 0
    for i in range(0,n):
        count+=array[i]
    miss = natural-count 
    return miss

print(missing_num(array))
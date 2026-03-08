nums = [1,2,3,4,5,67]
target = 69 

def two_sum(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return[i,j]
    return -1 

print(two_sum(nums))

# hashmap solution 





 




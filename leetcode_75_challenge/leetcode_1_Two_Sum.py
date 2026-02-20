# input = [2,7,11,15] target = 9
# output = [0,1]

nums = [2,7,11,15]
target = 13 

def two_sum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]== target:
                return [i,j]
    return -1

print(two_sum(nums,target))


# optimized version of two sum : 

array = [2,5,6,3,2,1,43] # 0,1,2,3,4,5,6 # target 8 
target = 8

def two_sum_opt(array,target):
    hashmap = {}
    for index,val in enumerate(array):
        difference = target - val
        if difference in hashmap:
            return index,hashmap[difference]
        hashmap[val] = index 
print(two_sum_opt(array,target))
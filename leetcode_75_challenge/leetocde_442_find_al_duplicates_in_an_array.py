# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# first we will try to do a brute force solution :
nums = [4,3,2,7,8,2,3,1]

def duplicates_Ad(nums):
    final = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]==nums[j]):
                final.append(nums[i])
                final.sort()
    return final 

print(duplicates_Ad(nums))

# more optimal approach :

def optimal(nums):
    seen = []
    final = []
    for i in nums:
        if i  in seen:
            final.append(i)
        else:
            seen.append(i)
    return final 

print(optimal(nums))
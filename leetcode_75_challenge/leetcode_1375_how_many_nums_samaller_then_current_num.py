nums = [8,1,2,2,3]

def fucntion(nums):
 
    list = []
    for i in range(0,len(nums)):
           count = 0
           for j in range(i+1,len(nums)):
               if(nums[j]<nums[i]):
                count +=1
           list.append(count)
    return list 

print(fucntion(nums))
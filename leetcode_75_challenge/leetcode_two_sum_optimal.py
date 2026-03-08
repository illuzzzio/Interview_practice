nums = [1,6,3,75]
target = 78 

def optimal(nums,target):
    hashmap = {}
    for index,value in enumerate(nums):
        difference = target - value 
        if difference in hashmap:
            return index,hashmap[difference]
        else:
            hashmap[value]= index
print(optimal(nums,target))


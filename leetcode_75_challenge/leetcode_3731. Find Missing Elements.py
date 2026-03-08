nums = [5,1]

# expected output = [2,3,4]
def ranged_missing(nums):
    answer = []
    new_num = sorted(set(nums)) # 1,5 

    for i in range(new_num[0], new_num[-1]): # 1,2,3,4,5 
        if i not in new_num:
            answer.append(i)
    return answer 


print(ranged_missing(nums))
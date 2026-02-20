# input = [4,3,2,7,8,2,3,1]
# output = [5,6]
answer = []
list = [1,1,2,2,3,3,4,5,6,7,8]

def all_missing(list,answer):
    set_nums = set(list) # 1,2,3,4,7,8
    for i in range(1,len(list)+1): #1,2,3,4,5,6,7,8
        if i not in set_nums:
            answer.append(i)
    return answer
print(all_missing(list,answer))
# we are actually appending index values 
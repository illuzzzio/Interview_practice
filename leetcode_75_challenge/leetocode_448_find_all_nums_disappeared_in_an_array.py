array = [4,3,2,7,8,2,3,1]

# 1,2,3,4,7,8
def all_missing_nums(array):
    n = len(array) # 8
    answer = []
    new_array = set(array) # 1,2,3,4,7,8

    for i in range(1,n+1):  # 1 to 9 , we have new array having 1,2,3,4,7,8 , so i will go till n0-1 ie 8 , we check these i numbers with new_array , in new loop we haev i= ,2,3,4,5,6,7,8 and checking with 1,2,3,4,7,8 if i not in new_array , we appedn it to new array , and that is our solution    
        if i not in new_array:
            answer.append(i)
    return answer 

print(all_missing_nums(array))

list = [1,2,3,4]
element = 5

def insertion_at_beginning(list,element):
    list.append(0)
    n = len(list) # this is 5 now 
    for i in range(n-1,0,-1): # starts from index 4 empty space to 0th index
        list[i] = list[i-1] # right shift 
    
    list[0]= element 

insertion_at_beginning(list,element)

print(list)
list =[1,2,4,5,6,3,2]
pos = 3 
element = 7

def anypos_insert(list,pos,element):
    list.append(0)
    n = len(list) # 8

    for i in range(n-1,pos,-1): # n-1 is 7th index which is khali 
        list[i]= list[i-1]
    list[pos] = element

anypos_insert(list,pos,element)

print(list)

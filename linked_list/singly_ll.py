#[]==>[]==>[]==>NULL ([] is node here) 
# each node has a value and a pointer pointing to next node address 
# head is a pointer which poinst towards first node 

# the traversal is O(n) but if we want to perform operation on the first element of the linked lsit , ist just O(1)

# class SinglyNode:
#     def __init__(self, val,next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)
#     # above is the printing method \

# Head = SinglyNode(1)
# A = SinglyNode(3)
# B = SinglyNode(4)
# C  =SinglyNode(5)

# # connection 
# Head.next = A
# A.next = B
# B.next =C
# C.next = None 

# print(Head)

class SingleNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    
Head = SingleNode(1)
A = SingleNode(2)
B = SingleNode(4)
C = SingleNode(6)

Head.next = A
A.next = B
B.next = C
C.next = None 


# for traversal 

curr = Head 
while(curr!=None):
    print(curr)
    curr = curr.next

#proper display of linekd list 

def display(Head):
    curr = Head
    elements = []
    while(curr!=None):
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

def Search(Head,val):
    curr = Head
    while(curr!=None):
        if val == curr.val:
            return True
        curr = curr.next
        
    return False 

Search(Head,4)

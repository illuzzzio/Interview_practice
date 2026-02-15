# here we will implement doubly linked lists 

class DoubleNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next 
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
# we will basically join head and tail 

head = tail = DoubleNode(1)

def display(head):
    curr = head
    elements = []
    while(curr!=None):
        elements.append(str(curr.val))
        curr = curr.next
    print('<->'.join(elements))

display(head)

def insert_at_beginning(head,tail,val):
    new_node = DoubleNode(val,next=head) 
    head.prev = new_node 

    return new_node , tail 
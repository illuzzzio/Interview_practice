# stack --> append and pop and peek to ask , what is at top of the stack it is lifo 
# queue --> append and pop and peek to ask , what is at front of the queue it is fifo enqueue and dequeue 

# stack 

stack = []

stack.append(5)
stack.append(4)
stack.append(3)
x = stack.pop()
print(x)
print(stack)

# ask , if something is in the stack :
if stack:
    print(True)
stack.pop()

# queueues 


from collections import deque

q = deque() # creating an object 
print(q) #deque([])

#Enqueue - Add an element to the right side 
q.append(5)
q.append(6) # this happens in O(1) time complexity 

print(q)

#Dequeue - remove an element from left sidde , which makes it different from the stack i.e fifo

q.popleft()
print(q)
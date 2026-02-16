from collections import deque
q = deque()
q.append(5)
q.append(6) 
print(q)
q.popleft()
print(q)   

# this is hwo we implement the peek operation in the queue , to check which element is on the left side of the queue , means the elemnt which is ready to come out of the queue 
q[0]    # this peak from the left side 
q[-1] # this is peek fro mthe right side 
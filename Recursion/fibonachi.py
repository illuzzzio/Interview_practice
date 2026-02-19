# basic concept of fibo series is we return f(n) = f(n-1)+f(n-2) , using recusrion 

def Fibonachi(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fibonachi(n-1)+Fibonachi(n-2)
print(Fibonachi(6))
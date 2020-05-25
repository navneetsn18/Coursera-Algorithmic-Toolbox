def pisano(m):
    a,b=0,1
    c=a+b
    for i in range(0,m*m):
        c=(a+b)%m
        a=b 
        b=c 
        if(a==0 and b==1):
            return i+1
def fib(n,m):
    if(n<2):
        return n 
    a,b,i,ans=0,1,1,0 
    while(i<n):
        ans=(a+b)%m 
        a=b 
        b=ans
        i+=1 
    return ans
n,m=map(int,input().split())
print(fib(n%pisano(m),m))
    
def sumofn(n):
    a=[]
    s=0
    a.append(0)
    a.append(1)
    if(n<=0):
        return a[0]
    elif(n==1):
        return a[1]
    else:
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        s=sum(a)
    return s
m,n=map(int,input().split())
m%=60
n%=60
print((sumofn(n)-sumofn(m-1))%10)
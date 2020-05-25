def sumofn(n):
    a=[]
    b=[]
    s=0
    a.append(0)
    b.append(0)
    a.append(1)
    b.append(1)
    if(n<=0):
        return b[0]
    elif(n==1):
        return b[1]
    else:
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
            b.append(a[i]**2)
        s=sum(b)
    return s
n=int(input())
n%=60
print(sumofn(n)%10)
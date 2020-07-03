def binarySearch(n,a,i):
    l=0
    r=n-1
    while(l<=r):
        s=(l+r)//2
        if(a[s]==i):
            return s
        elif(a[s]<i):
            l=s+1
        else:
            r=s-1
    return -1
if __name__=="__main__":
    a=list(map(int,input().split()))
    n=a[0]
    del a[0]
    b=list(map(int,input().split()))
    k=b[0]
    del b[0]
    for i in b:
        print(binarySearch(n,a,i),end=" ")
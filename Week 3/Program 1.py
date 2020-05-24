def coins(n):
    s=0
    s+=n//10
    n%=10
    s+=n//5
    n%=5
    s+=n//1
    return s
n=int(input())
print(coins(n))
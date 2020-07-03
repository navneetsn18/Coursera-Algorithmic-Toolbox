from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
arr=Counter(arr)
m=max(arr.values())
if(m>n//2):
    print(1)
else:
    print(0)
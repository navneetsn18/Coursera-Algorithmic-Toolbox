def solution(w,n,l):
    arr=[[0]*(w+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if(l[i-1]>j):
                arr[i][j]=arr[i-1][j]
            elif(l[i-1]==j):
                arr[i][j]=arr[i-1][j-l[i-1]]+l[i-1]
            else:
                if(arr[i-1][j-l[i-1]]+l[i-1]<=w):
                    arr[i][j]=max(arr[i-1][j-l[i-1]]+l[i-1],arr[i-1][j])
                else:
                    arr[i][j]=arr[i][j-1]
    return arr[-1][-1]
if __name__=="__main__":
    w,n=map(int,input().split())
    l=list(map(int,input().split()))
    print(solution(w,n,l))

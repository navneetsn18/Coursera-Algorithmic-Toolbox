def lcs(n1,arr1,n2,arr2):
    mat=[[0]*(n1+1) for _ in range(n2+1)]
    for i in range(n2):
        for j in range(n1):
            if(arr1[j]==arr2[i]):
                mat[i+1][j+1]=1+mat[i][j]
            else:
                mat[i+1][j+1]=max(mat[i][j+1],mat[i+1][j])
    return mat[-1][-1]

if __name__=="__main__":
    n1=int(input())
    arr1=list(map(int,input().split()))
    n2=int(input())
    arr2=list(map(int,input().split()))
    print(lcs(n1,arr1,n2,arr2))

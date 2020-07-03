def lcs(n1,arr1,n2,arr2,n3,arr3):
    mat=[[[0]*(n1+1) for _ in range(n2+1)] for __ in range(n3+1)]
    for i in range(n3):
        for j in range(n2):
            for k in range(n1):
                if(arr1[k]==arr2[j] and arr1[k]==arr3[i]):
                    mat[i+1][j+1][k+1]=1+mat[i][j][k]
                else:
                    mat[i+1][j+1][k+1]=max(mat[i][j+1][k+1],mat[i+1][j][k+1],mat[i+1][j+1][k])
    return mat[-1][-1][-1]

if __name__=="__main__":
    n1=int(input())
    arr1=list(map(int,input().split()))
    n2=int(input())
    arr2=list(map(int,input().split()))
    n3=int(input())
    arr3=list(map(int,input().split()))
    print(lcs(n1,arr1,n2,arr2,n3,arr3))

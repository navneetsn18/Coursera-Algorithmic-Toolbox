def solution(n,nums):
    if(sum(nums)%3!=0):
        return 0
    else:
        n=sum(nums)//3
        arr=[[False]*(n+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(n+1):
                if(j==0):
                    arr[i][j]=True
                elif(j<nums[i-1]):
                    arr[i][j]=arr[i-1][j]
                else:
                    arr[i][j]=(arr[i-1][j] or arr[i-1][j-nums[i-1]])
    return arr[-1][-1]
        
if __name__=="__main__":
    n=int(input())
    nums=list(map(int,input().split()))
    if solution(n,nums)==True:
        print('1')
    else:
        print('0')


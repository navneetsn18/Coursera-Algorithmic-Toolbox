def coins(n,c):
    minCoins=[0]+[9999]*n 
    for i in range(1,n+1):
        for j in c:
            if(i>=j):
                coins=minCoins[i-j]+1 
                if(coins<minCoins[i]):
                    minCoins[i]=coins
    return minCoins[n]
if __name__=="__main__":
    n=int(input())
    c=[1,3,4]
    print(coins(n,c))

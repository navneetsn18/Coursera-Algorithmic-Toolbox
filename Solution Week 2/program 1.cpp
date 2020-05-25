#include<iostream>
using namespace std;
int fib(int n)
{
    if(n==0){
        return 0;
    }
    else
    {
        int x=0,y=1,temp=0;
        for(int i=1;i<n;i++)
        {
            temp=y;
            y=x+y;
            x=temp;
        }
        return y;
    }
}
int main()
{
    int n;
    cin>>n;
    cout<<fib(n);
    return 0;
}
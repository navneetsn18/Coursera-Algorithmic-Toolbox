#include<iostream>
using namespace std;
int fib(int n)
{
    int a=0,b=1,c=0,i;
    if(n==0 || n==1)
    {
        return n;
    }
    for(i=2;i<=n;i++)
    {
        c=(a+b)%10;
        a=b;
        b=c;
    }
    return c;
}
int main()
{
    int n;
    cin>>n;
    cout<<fib(n);
    return 0;
}

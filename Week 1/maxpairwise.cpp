#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    long int n,i,arr[200000];
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    sort(arr,arr+n);
    cout<<arr[n-1]*arr[n-2];
    return 0;
}
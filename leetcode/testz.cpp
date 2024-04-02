#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int k;
    cin>>k;
    int l = 0, r = n-1;
    int m = -1;
    while(l<=r){
        m = (l+r)/2;
        if (a[m] == k) 
            break;
        else if(a[m] < k)
            l = m+1;
        else
            r = m-1;
    }
    cout<<m<<endl;
    return 0;
}
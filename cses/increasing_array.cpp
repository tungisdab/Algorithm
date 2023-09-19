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
    ll n;
    cin>>n;
    ll ans=0;
    ll a[n];
    for (int i=0;i<n;i++){
        cin>>a[i];
    }
    for (int i=1;i<n;i++){
        if(a[i-1]>a[i]){
            ans += a[i-1]-a[i];
            a[i] = a[i-1];
        }
    }
    cout<<ans<<endl;
    return 0;
}
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
    set<ll> s;
    for (int i=0;i<n;i++){
        ll x;
        cin>>x;
        s.insert(x);
    }
    cout<<s.size()<<endl;
    return 0;
}
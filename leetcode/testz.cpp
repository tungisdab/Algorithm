#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{
    int n;
    cin>>n;
    double a = log(n) / log(3);
    // cout<<log(243) / log(3)<<endl;
    cout<< a << endl;
    cout<<abs(a-int(a))<<endl;
    // if ( abs(a-int(a)) < 0.1   )
    //     cout<< "true";
    // else cout<< "false";
}
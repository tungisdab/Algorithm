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
    string s, t;
    getline(cin, s);
    getline(cin, t);
    string a = "";
    string b = "";
    int n = s.size();
    int m = t.size();
    // if (n != m)
    //     return false;
    for (int i=0; i<n; i++) {
        // a += (s[i] - s[0]);
        cout<<s[i]-s[0]<<endl;
    }
    for (int i=0;i<m;i++) {
        // b += (t[i] - t[0]);
        cout<<t[i]-t[0]<<endl;
    }
    cout<<a<<endl;
    cout<<b<<endl;
    // if (a != b) return false;
    // return true;
    return 0;
}
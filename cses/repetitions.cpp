#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{
    string s;
    cin>>s;
    int ans = 1;
    int cnt = 1;
    for(int i=1;i<s.length();i++){
        if(s[i-1] == s[i]){
            cnt++;
            ans = max(ans,cnt);
        }
        else{
            cnt = 1;
        }
    }   
    cout<<ans;
    return 0;
}
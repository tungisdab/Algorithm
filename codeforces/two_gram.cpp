#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{
    int n;
    cin>>n;
    string s;
    cin>>s;
    map<string,int> mp;
    for(int i=0;i<n-1;i++){
        string temp = "";
        temp += s[i];
        temp += s[i+1];
        mp[temp]++; 
    }
    int ans = 0;
    string ans1;
    for(auto i:mp){
        if(i.second > ans){
            ans = i.second;
            ans1 = i.first;
        }
    }
    cout<<ans1<<endl;
    return 0;
}
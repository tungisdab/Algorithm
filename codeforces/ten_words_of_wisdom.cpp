#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
bool cmp(pair<int, int> a, pair<int, int> b){
    return a.second > b.second;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    while (t--)
    {
        int n;
        cin>>n;
        vector<pair<int, int>> v;
        for(int i=0;i<n;i++){
            int a, b;
            cin>>a>>b;
            if(a<=10)
                v.push_back(make_pair(i+1,b));
        }   
        sort(v.begin(),v.end(), cmp);
        cout<<v[0].first<<endl;
    }
    return 0;
}
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
    cin>>n;
    set<int> a;
    for(int i=0;i<n-1;i++)
    {
        int x;
        cin>>x;
        a.insert(x);
    }
    int x = 1;
    for(auto i:a){
        if(i!=x){
            break;
        }
        else{
            x++;
        }
    }
    cout<<x;
    return 0;
}
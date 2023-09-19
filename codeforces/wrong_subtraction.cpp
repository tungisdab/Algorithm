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
    int k;
    cin>>k;   
    for(int i=0;i<k;i++){
        if(n%10 == 0){
            n = n/10;
        }
        else{
            n--;
        }
    }
    cout<<n;
    return 0;
}
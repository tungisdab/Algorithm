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
    vector<vector<int>> a(n,vector<int> (n, 0));
    int x = 1;
    for(int i=0;i<n/2;i++) {
        for (int j=i;j<n-i;j++) 
            a[i][j] = x++;
        for (int j=i;j<n-i;j++)
            a[j][n-1-i] = x++;
        for (int j=i;j<n-i;j++)
            a[n-1-i][n-1-j] = x++;
        for (int j=i;j<n-i;j++)
            a[n-1-j][i] = x++;
    }
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
    return 0;
}
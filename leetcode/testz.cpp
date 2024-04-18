#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{
    // vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    vector<vector<int>> grid = {{0,1}};
    for(auto i: grid) {
        for (auto j: i)
            cout<< j<< " ";
        cout<<endl;
    }
    int n = grid.size();
    vector<vector<int>> a(n+2, vector<int> (n+2, 0));
    for(int i =0;i<n;i++) {
        for (int j =0;j<n;j++){
            a[i+1][j+1] = grid[i][j];
        }
    }
    for (auto i: a) {
        for (int j : i) {
            cout << j << " ";
        }
        cout<<endl;
    }
    int ans = 0;
    for (int i=1;i<=n;i++){
        for (int j=1;j<=n;j++) {
            if (a[i][j] == 1) {
                ans += 4;
                if (a[i-1][j] == 1)
                    ans--;
                if (a[i+1][j] == 1)
                    ans--;
                if (a[i][j-1] == 1)
                    ans--;
                if (a[i][j+1] == 1)
                    ans--;
            }
        }
    }
}
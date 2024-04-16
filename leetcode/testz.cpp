#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man
int main()
{

    int n;
    cin >> n;
    double a = log(double(n));
    cout<<a;
    if ((int) a == a) 
        cout<<'1';
    else 
        cout<<'0';
    return 0;
}
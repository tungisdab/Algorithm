#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
//by KMA dil and man

static map<char, int> mp;
static bool cmp(char a, char b) {
    return mp[a] > mp[b];
}
string frequencySort(string s) {
    for (char i:s) {
        mp[i]++;
    }
    sort(s.begin(), s.end(), cmp);
    return s;
}

int main()
{
    string s = "tree";
    cout << frequencySort(s) << endl;
    return 0;
}
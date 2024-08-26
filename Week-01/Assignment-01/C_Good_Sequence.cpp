#include <bits/stdc++.h>
using namespace std;
int a[100000];
int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        mp[a[i]]++;
    }
    int ans = 0;
    for (auto p : mp)
    {
        int x = p.first;
        int n = p.second;
        if (n < x)
            ans += n;
        else
            ans += n - x;
    }

    cout << ans << endl;
    return 0;
}




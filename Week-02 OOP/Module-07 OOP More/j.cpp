

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        unordered_map<int, int> visit;
        sort(a, a + n);
        for (int i = 0; i < n; i++)
        {
            visit[a[i]]++;
        }
        for (auto i : visit)
        {
            if (i.second % 2 == 1)
            {
                cout << i.first;
            }
        }
        cout << endl;
    }
    return 0;
}
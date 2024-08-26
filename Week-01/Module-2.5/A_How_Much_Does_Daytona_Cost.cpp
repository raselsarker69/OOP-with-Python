/*#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> v(n);

        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }

        sort(v.begin(), v.end());

        bool flag = binary_search(v.begin(), v.end(), k);

        if (flag)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}*/

#include "bits/stdc++.h"
using namespace std;
int T, n, k;
int main()
{
    cin >> T;
    while (T--)
    {
        cin >> n >> k;
        int flag = 0;
        int t;
        for (int i = 1; i <= n; i++)
        {
            cin >> t;
            if (t == k)
                flag = 1;
        }
        if (flag == 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
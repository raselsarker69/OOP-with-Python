#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int x, y, n;
        cin >> x >> y >> n;
        int sum = 0;
        while (n > x && y < n && n % 2 != 0) 
        {
            sum+=n;
            // if (n % 2 != 0)
            // {
            //     sum += n;
            // }
            cout << sum << endl;
        }
    }
    return 0;
}
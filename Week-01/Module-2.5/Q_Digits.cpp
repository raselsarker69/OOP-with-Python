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
        while (n > 0)
        {
            int digit = n % 10;
            cout << digit << " ";
            n /= 10;
        }

        cout << endl;
    }

    return 0;
}
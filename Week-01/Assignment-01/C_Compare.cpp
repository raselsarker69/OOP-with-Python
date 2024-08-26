#include <bits/stdc++.h>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    if (a == b)
    {
        cout << a << endl;
    }
    else if (a > b)
    {
        cout << b << endl;
    }
    else
    {
        cout << a << endl;
    }
    return 0;
}
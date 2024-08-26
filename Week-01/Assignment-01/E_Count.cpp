#include <bits/stdc++.h>
using namespace std;
int main()
{
    char a[1000001];
    cin >> a;
    int sum = 0;
    for (int i = 0; i < strlen(a); i++)
    {
        sum = sum + (a[i] - '0');
    }
    cout << sum << endl;
    return 0;
}
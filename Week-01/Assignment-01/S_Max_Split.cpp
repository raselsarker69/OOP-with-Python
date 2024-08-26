#include <bits/stdc++.h>
using namespace std;

int main()
{
    char ar[1001][1001];
    string s;
    cin >> s;

    int row = 0, col = 0, r = 0, l = 0, cnt = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'R')
        {
            ar[row][col] = s[i];
            r++;
        }
        else
        {
            ar[row][col] = s[i];
            l++;
        }
        col++;
        if (r == l && r > 0)
        {
            row++;
            col = 0;
            cnt++;
            r = 0;
            l = 0;
        }
    }

    cout << cnt << endl;
    for (int i = 0; i < 1000; i++)
    {
        if (ar[i][0] != 'R' && ar[i][0] != 'L')
        {
            continue;
        }
        cout << ar[i] << endl;
    }

    return 0;
}
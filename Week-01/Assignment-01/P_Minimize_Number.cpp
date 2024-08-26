// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     int a[n];
//     for (int i = 0; i < n; i++)
//     {
//         cin >> a[i];
//     }

//     int result = 0;
//     for (int i = 0; i < n; i++)
//     {
//         int cnt = 0;
//         if (a[i] % 2 != 0)
//         {
//             cout << 0 << endl;
//             return 0;
//         }
//         while (a[i] % 2 == 0 && a[i]>0)
//         {
//             cnt++;
//             a[i] /= 2;
//         }
//         if (i == 0 || cnt < result)
//         {
//             result = cnt;
//         }
//     }
//     cout << result << endl;

//     return 0;
// }
//-------------------------------------------------//

// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     int a[n];
//     for (int i = 0; i < n; i++)
//     {
//         cin >> a[i];
//     }

//     int MIN = INT_MAX;
//     for (int i = 0; i < n; i++)
//     {
//         int cnt = 0;
//         if (a[i] % 2 != 0)
//         {
//             cout << 0 << endl;
//             return 0;
//         }
//         while (a[i] % 2 == 0 && a[i] > 0)
//         {
//             cnt++;
//             a[i] /= 2;
//         }

//         MIN = min(MIN, cnt);
//     }
//     cout << MIN << endl;

//     return 0;
// }

//--------------------------------------------------//

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        if (a[i] % 2 != 0)
        {
            cout << 0 << endl;
            return 0;
        }
    }

    int cnt = 0, flag = 0;
    while (flag == 0)
    {
        for (int i = 0; i < n; i++)
        {
            if (a[i] % 2 == 0 && a[i] > 0)
            { 
                a[i] /= 2;
            }
            else
            {
                flag = 1;
                break;
            }
        }
        cnt++;
    }
    cout << cnt - 1 << endl;

    return 0;
}

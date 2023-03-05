#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int a[2005][3], n, p[2005], todo, l, x, y;

long long c, ans;
bool flag;
struct e

{
    int x, y;
    long long cost;
};
bool cmp(e x, e y)
{
    return x.cost < y.cost;
}
int fi(int a)
{
    if (p[a] == a)
        return a;
    else
    {
        p[a] = fi(p[a]);
        return p[a];
    }
}
vector<e> v;
vector<int> towers;
vector<pair<int, int>> edge;

int main()
{
    while (cin >> n)
    {
        v.clear();
        towers.clear();
        todo = n;
        p[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            p[i] = i;
            cin >> a[i][1] >> a[i][2];
        }
        for (int i = 1; i <= n; i++)
        {
            cin >> c;
            v.push_back({0, i, c});
        }
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i][0];
        }
        for (int i = 1; i < n; i++)
        {
            for (int j = i + 1; j <= n; j++)
            {
                c = (a[i][0] + a[j][0]);
                c *= (abs(a[i][1] - a[j][1]) + abs(a[i][2] - a[j][2]));
                v.push_back({i, j, c});
            }
        }
        sort(v.begin(), v.end(), cmp);
        for (e tmp : v)
        {
            x = fi(tmp.x);
            y = fi(tmp.y);
            if (x == y)
                continue;
            if (tmp.x == 0)
                towers.push_back(tmp.y);
            else
                edge.push_back({tmp.x, tmp.y});
            p[y] = x;
            ans += tmp.cost;
            todo--;
            if (todo == 0)
                break;
        }
        cout << ans << "\n";
        l = towers.size();
        cout << l << "\n";
        sort(towers.begin(), towers.end());
        for (int i = 0; i < l; i++)
        {
            if (i != 0)
                cout << " ";
            cout << towers[i];
        }
        cout << "\n";
        l = edge.size();
        cout << l << "\n";
        for (int i = 0; i < l; i++)
        {
            cout << edge[i].first << " " << edge[i].second << "\n";
        }
    }
}
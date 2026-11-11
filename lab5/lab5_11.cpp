#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    constexpr long long MOD = 1000000000LL;
    int n; cin >> n;
    vector<int> values;
    bool previous_query = false;
    long long previous_answer = 0;
    for (int i = 0; i < n; ++i) {
        char op; long long x; cin >> op >> x;
        if (op == '+') {
            if (previous_query) x = (x + previous_answer + MOD) % MOD;
            if (find(values.begin(), values.end(), (int)x) == values.end())
                values.push_back((int)x);
            previous_query = false;
        } else {
            sort(values.begin(), values.end());
            auto it = lower_bound(values.begin(), values.end(), (int)x);
            int ans = it == values.end() ? -1 : *it;
            cout << ans << '\n';
            previous_answer = ans;
            previous_query = true;
        }
    }
}

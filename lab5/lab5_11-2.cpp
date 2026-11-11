#include <iostream>
#include <set>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    constexpr long long MOD = 1000000000LL;
    int n; cin >> n;
    set<int> values;
    bool previous_query = false;
    long long previous_answer = 0;
    for (int i = 0; i < n; ++i) {
        char op; long long x; cin >> op >> x;
        if (op == '+') {
            // missing conversion for dependent insert
            values.insert((int)x);
            previous_query = false;
        } else {
            auto it = values.lower_bound((int)x);
            int ans = it == values.end() ? -1 : *it;
            cout << ans << '\n';
            previous_answer = ans;
            previous_query = true;
        }
    }
}

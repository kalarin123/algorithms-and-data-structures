#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> values;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") values.clear();
        else if (cmd == "ADD") {
            long long x;
            cin >> x;
            values.push_back(x);
        } else if (cmd == "EXTRACT") {
            if (values.empty()) cout << "CANNOT\n";
            else {
                auto it = max_element(values.begin(), values.end());
                cout << *it << '\n';
                values.erase(it);
            }
        }
    }
}


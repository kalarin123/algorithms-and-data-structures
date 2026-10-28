#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> a;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") a.clear();
        else if (cmd == "ADD") {
            long long x;
            cin >> x;
            a.push_back(x);
        } else if (cmd == "EXTRACT") {
            if (a.empty()) cout << "CANNOT\n";
            else {
                auto it = min_element(a.begin(), a.end());
                cout << *it << '\n';
                a.erase(it);
            }
        }
    }
}


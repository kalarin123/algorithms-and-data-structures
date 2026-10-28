#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<long long> h;

void add(long long x) {
    h.push_back(x);
    int i = (int)h.size() - 1;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        swap(h[p], h[i]);
        i = p;
    }
}

long long extract() {
    long long result = h[0];
    h[0] = h.back();
    h.pop_back();
    int i = 0, n = (int)h.size();
    while (2 * i + 1 < n) {
        int j = 2 * i + 1;
        if (j + 1 < n && h[j + 1] > h[j]) ++j;
        if (h[i] >= h[j]) break;
        swap(h[i], h[j]);
        i = j;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") h.clear();
        else if (cmd == "ADD") {
            long long x;
            cin >> x;
            add(x);
        } else if (cmd == "EXTRACT") {
            if (h.empty()) cout << "CANNOT\n";
            else cout << extract() << '\n';
        }
    }
}


#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

class MinHeap {
    vector<long long> a;

public:
    void clear() { a.clear(); }
    bool empty() const { return a.empty(); }

    void add(long long x) {
        a.push_back(x);
        int i = (int)a.size() - 1;
        while (i > 0) {
            int p = (i - 1) / 2;
            if (a[p] <= a[i]) break;
            swap(a[p], a[i]);
            i = p;
        }
    }

    long long extract() {
        long long result = a[0];
        long long last = a.back();
        a.pop_back();
        if (a.empty()) return result;
        a[0] = last;
        int i = 0;
        int n = (int)a.size();
        while (2 * i + 1 < n) {
            int j = 2 * i + 1;
            if (j + 1 < n && a[j + 1] < a[j]) ++j;
            if (a[i] <= a[j]) break;
            swap(a[i], a[j]);
            i = j;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    MinHeap heap;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") heap.clear();
        else if (cmd == "ADD") {
            long long x;
            cin >> x;
            heap.add(x);
        } else if (cmd == "EXTRACT") {
            if (heap.empty()) cout << "CANNOT\n";
            else cout << heap.extract() << '\n';
        }
    }
}


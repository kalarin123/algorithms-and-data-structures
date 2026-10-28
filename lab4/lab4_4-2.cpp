#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    priority_queue<long long, vector<long long>, greater<long long>> heap;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            decltype(heap) empty;
            heap.swap(empty);
        } else if (cmd == "ADD") {
            long long x;
            cin >> x;
            heap.push(x);
        } else if (cmd == "EXTRACT") {
            if (heap.empty()) cout << "CANNOT\n";
            else {
                cout << heap.top() << '\n';
                heap.pop();
            }
        }
    }
}


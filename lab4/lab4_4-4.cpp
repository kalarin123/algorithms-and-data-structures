#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    priority_queue<long long> heap;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            priority_queue<long long> empty;
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


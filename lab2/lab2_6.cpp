#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long n, x, y;
    cin >> n >> x >> y;

    long long firstCopy = min(x, y);
    long long remaining = n - 1;

    long long left = -1;
    long long right = min(x, y) * remaining;

    while (right - left > 1) {
        long long mid = (left + right) / 2;
        long long copies = mid / x + mid / y;

        if (copies >= remaining)
            right = mid;
        else
            left = mid;
    }

    cout << firstCopy + right << '\n';
    return 0;
}

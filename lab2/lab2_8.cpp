#include <iostream>
#include <algorithm>
using namespace std;

bool canPlace(long long side, long long w, long long h, long long n) {
    return (side / w) * (side / h) >= n;
}

int main() {
    long long w, h, n;
    cin >> w >> h >> n;

    long long left = -1;
    long long right = max(w, h) * n;

    while (right - left > 1) {
        long long mid = (left + right) / 2;

        if (canPlace(mid, w, h, n))
            right = mid;
        else
            left = mid;
    }

    cout << right << '\n';
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool canCut(const vector<long long>& ropes, long long length, long long k) {
    long long pieces = 0;

    for (long long rope : ropes)
        pieces += rope / length;

    return pieces >= k;
}

int main() {
    int n;
    long long k;
    cin >> n >> k;

    vector<long long> ropes(n);
    long long maxLength = 0;

    for (int i = 0; i < n; ++i) {
        cin >> ropes[i];
        maxLength = max(maxLength, ropes[i]);
    }

    long long left = 0;
    long long right = maxLength + 1;

    while (right - left > 1) {
        long long mid = (left + right) / 2;

        if (canCut(ropes, mid, k))
            left = mid;
        else
            right = mid;
    }

    cout << left << '\n';
    return 0;
}

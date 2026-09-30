#include <iostream>
#include <vector>
using namespace std;

bool canPlace(const vector<long long>& stalls, int k, long long distance) {
    int cows = 1;
    long long last = stalls[0];

    for (int i = 1; i < (int)stalls.size(); ++i) {
        if (stalls[i] - last >= distance) {
            ++cows;
            last = stalls[i];
        }
    }

    return cows >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<long long> stalls(n);
    for (int i = 0; i < n; ++i) {
        cin >> stalls[i];
    }

    long long left = 0;
    long long right = stalls.back() - stalls.front() + 1;

    while (right - left > 1) {
        long long mid = (left + right) / 2;

        if (canPlace(stalls, k, mid))
            left = mid;
        else
            right = mid;
    }

    cout << left << '\n';
    return 0;
}

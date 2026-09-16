#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    int swaps = 0;

    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                swap(A[j], A[j + 1]);
                swaps++;
            }
        }
    }

    cout << swaps;

    return 0;
}

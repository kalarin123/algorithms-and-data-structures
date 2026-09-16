#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void QuickSort(vector<int>& A, int left, int right) {
    int i = left;
    int j = right;
    int pivot = A[(left + right) / 2];

    while (i <= j) {
        while (A[i] < pivot) {
            i++;
        }

        while (A[j] > pivot) {
            j--;
        }

        if (i <= j) {
            swap(A[i], A[j]);
            i++;
            j--;
        }
    }

    if (left < j) {
        QuickSort(A, left, j);
    }

    if (i < right) {
        QuickSort(A, i, right);
    }
}

int main() {
    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    if (N > 0) {
        QuickSort(A, 0, N - 1);
    }

    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }

    return 0;
}

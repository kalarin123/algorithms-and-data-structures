#include <iostream>
#include <vector>

using namespace std;

void Merge(vector<int>& A, int left, int mid, int right) {
    vector<int> temp;
    int i = left;
    int j = mid + 1;

    while (i <= mid && j <= right) {
        if (A[i] <= A[j]) {
            temp.push_back(A[i]);
            i++;
        } else {
            temp.push_back(A[j]);
            j++;
        }
    }

    while (i <= mid) {
        temp.push_back(A[i]);
        i++;
    }

    while (j <= right) {
        temp.push_back(A[j]);
        j++;
    }

    for (int k = 0; k < (int)temp.size(); k++) {
        A[left + k] = temp[k];
    }
}

void MergeSort(vector<int>& A, int left, int right) {
    if (left >= right) {
        return;
    }

    int mid = (left + right) / 2;

    MergeSort(A, left, mid);
    MergeSort(A, mid + 1, right);
    Merge(A, left, mid, right);
}

int main() {
    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    MergeSort(A, 0, N - 1);

    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }

    return 0;
}

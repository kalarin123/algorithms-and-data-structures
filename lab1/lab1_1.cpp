#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

void SelectionSort(vector<int>& A) {
    int n = (int)A.size();

    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }

        swap(A[i], A[maxIndex]);
    }
}

int main() {
    vector<int> A;
    string line;

    getline(cin, line);
    stringstream ss(line);

    int x;
    while (ss >> x) {
        A.push_back(x);
    }

    SelectionSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}

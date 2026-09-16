#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

void InsertionSort(vector<int>& A) {
    int n = (int)A.size();

    for (int i = 1; i < n; i++) {
        int x = A[i];
        int j = i - 1;

        while (j >= 0 && A[j] > x) {
            A[j + 1] = A[j];
            j--;
        }

        A[j + 1] = x;
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

    InsertionSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}

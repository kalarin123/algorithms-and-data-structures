#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

void CountSort(vector<int>& A) {
    int count[101] = {0};

    for (int i = 0; i < (int)A.size(); i++) {
        count[A[i]]++;
    }

    int k = 0;

    for (int value = 0; value <= 100; value++) {
        while (count[value] > 0) {
            A[k] = value;
            k++;
            count[value]--;
        }
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

    CountSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}

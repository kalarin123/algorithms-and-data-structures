#include <iostream>

using namespace std;

struct Point {
    int x;
    int y;
};

int DistanceSquared(Point p) {
    return p.x * p.x + p.y * p.y;
}

int main() {
    int n;
    cin >> n;

    Point A[100];

    for (int i = 0; i < n; i++) {
        cin >> A[i].x >> A[i].y;
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (DistanceSquared(A[j]) > DistanceSquared(A[j + 1])) {
                Point temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << A[i].x << " " << A[i].y << endl;
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <cstdint>
#include <utility>
using namespace std;

struct Node {
    int key;
    uint32_t priority;
    int left, right;
};

class Treap {
    vector<Node> nodes;
    int root = -1;
    uint32_t seed = 712367821U;

    uint32_t random_priority() {
        seed ^= seed << 13;
        seed ^= seed >> 17;
        seed ^= seed << 5;
        return seed;
    }

    int rotate_right(int p) {
        int q = nodes[p].left;
        nodes[p].left = nodes[q].right;
        nodes[q].right = p;
        return q;
    }

    int rotate_left(int p) {
        int q = nodes[p].right;
        nodes[p].right = nodes[q].left;
        nodes[q].left = p;
        return q;
    }

    int insert(int t, int x) {
        if (t == -1) {
            nodes.push_back({x, random_priority(), -1, -1});
            return (int)nodes.size() - 1;
        }
        if (x == nodes[t].key) return t;
        if (x < nodes[t].key) {
            nodes[t].left = insert(nodes[t].left, x);
            int child = nodes[t].left;
            if (nodes[child].priority > nodes[t].priority) t = rotate_right(t);
        } else {
            nodes[t].right = insert(nodes[t].right, x);
            int child = nodes[t].right;
            if (nodes[child].priority > nodes[t].priority) t = rotate_left(t);
        }
        return t;
    }

public:
    explicit Treap(int capacity) { nodes.reserve(capacity); }
    void add(int x) { root = insert(root, x); }
    int next(int x) const {
        int cur = root;
        int answer = -1;
        while (cur != -1) {
            if (nodes[cur].key >= x) {
                answer = nodes[cur].key;
                cur = nodes[cur].left;
            } else {
                cur = nodes[cur].right;
            }
        }
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    constexpr long long MOD = 1000000000LL;
    int n;
    cin >> n;
    Treap tree(n);
    bool previous_query = false;
    long long previous_answer = 0;
    for (int i = 0; i < n; ++i) {
        char op;
        long long x;
        cin >> op >> x;
        if (op == '+') {
            if (previous_query) x = (x + previous_answer + MOD) % MOD;
            tree.add((int)x);
            previous_query = false;
        } else {
            int answer = tree.next((int)x);
            cout << answer << '\n';
            previous_answer = answer;
            previous_query = true;
        }
    }
}

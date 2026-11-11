#include <iostream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

struct Node {
    long long data;
    Node *left, *right;
    explicit Node(long long n): data(n), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
    Node* root = nullptr;
public:
    bool add(long long x) {
        Node** at = &root;
        while (*at) {
            if ((*at)->data == x) return false;
            at = x < (*at)->data ? &(*at)->left : &(*at)->right;
        }
        *at = new Node(x);
        return true;
    }

    bool search(long long x) const {
        Node* at = root;
        while (at) {
            if (at->data == x) return true;
            at = x < at->data ? at->left : at->right;
        }
        return false;
    }

    bool erase(long long x) {
        Node** at = &root;
        while (*at && (*at)->data != x) {
            at = x < (*at)->data ? &(*at)->left : &(*at)->right;
        }
        if (!*at) return false;
        Node* node = *at;
        if (node->left && node->right) {
            Node** pred = &node->left;
            while ((*pred)->right) pred = &(*pred)->right;
            swap(node->data, (*pred)->data);
            Node* old = *pred;
            *pred = old->left;
            delete old;
        } else {
            *at = node->left ? node->left : node->right;
            delete node;
        }
        return true;
    }

    void print_tree() const {
        vector<pair<Node*, int>> st;
        Node* cur = root;
        int level = 0;
        while (cur || !st.empty()) {
            while (cur) {
                st.push_back({cur, level});
                cur = cur->left;
                ++level;
            }
            auto [node, depth] = st.back();
            st.pop_back();
            cout << string(depth, '.') << node->data << '\n';
            cur = node->right;
            level = depth + 1;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    BinarySearchTree tree;
    string command;
    while (cin >> command) {
        if (command == "PRINTTREE") tree.print_tree();
        else {
            long long value;
            cin >> value;
            if (command == "ADD")
                cout << (tree.add(value) ? "DONE" : "DONE") << '\n';
            else if (command == "DELETE")
                cout << (tree.erase(value) ? "DONE" : "CANNOT") << '\n';
            else if (command == "SEARCH")
                cout << (tree.search(value) ? "YES" : "NO") << '\n';
        }
    }
}

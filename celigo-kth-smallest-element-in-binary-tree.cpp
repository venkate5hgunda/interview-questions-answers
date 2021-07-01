#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <climits>
using namespace std;

vector<int> tree;
vector<int> inorder_vec;

void inorder(tree_node root) {
    if(root!=nullptr) {
        inorder(root.left);
        inorder_vec.push_back(root.val);
        inorder(root.right);
    }
}

struct tree_node {
    int val;
    tree_node *left;
    tree_node *right;
}

int main(tree_node root) {
    // tree = {5,3,6,2,4,-1,-1,1,-1};
    
    inorder(root);
    
    cout << inorder_vec[k-1] << endl;
    
    return 0;
}

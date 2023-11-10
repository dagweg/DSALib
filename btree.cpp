#include <iostream>

using namespace std;

template <typename T>
struct TreeNode
{
    T data;
    TreeNode<T> *left;
    TreeNode<T> *right;
    TreeNode(T data = T(), TreeNode<T> *left = nullptr, TreeNode<T> *right = nullptr) : data(data), left(left), right(right){};
};

template <typename T>
class BinaryTree
{
    TreeNode<T> *root;

public:
    BinaryTree() : root(nullptr) {}
    ~BinaryTree();
    void insert(const T value)
    {
        root = insertRecursive(root, value);
    }

    bool searchNBST(const T &value)
    {
        return _searchNBST(root, value);
    };

    bool searchBST(const T &value)
    {
        return _searchBST(root, value);
    };

    void remove(const T &value);

    void inorderTraversal()
    {
        _inorderTraversal(root);
    };
    void preorderTraversal(){

    };
    void postorderTraversal(){

    };

    int getHeight();
    int getSize();

private:
    bool _searchNBST(TreeNode<T> *root, T &value)
    {
        if (root == nullptr)
            return false;
        if (root->data == value)
            return true;
        return _searchNonBST(root->left, value) || _searchNonBST(root->right, value);
    }

    bool _searchBST(TreeNode<T> *root, T &value)
    {
        if (root == nullptr)
            return false;

        if (value > root->data)
        {
            return _searchBST(root->right, value);
        }
        else if (value < root->data)
        {
            return _searchBST(root->left, value);
        }
        return true;
    }

    TreeNode<T> *insertRecursive(TreeNode<T> *trav, T val)
    {
        if (trav == nullptr)
        {
            return new TreeNode<T>(val);
        }

        if (val >= trav->data)
        {
            trav->right = insertRecursive(trav->right, val);
        }
        else
        {
            trav->left = insertRecursive(trav->left, val);
        }

        return trav;
    }

    void _inorderTraversal(TreeNode<T> *root)
    {
        if (root == nullptr)
            return;
        _inorderTraversal(root->left);
        cout << root->data << " -> ";
        _inorderTraversal(root->right);
    }
};

int main(void)
{
    BinaryTree<int> *root = new BinaryTree<int>();
    root->insert(1);
    root->insert(2);
    root->insert(3);
    root->insert(4);
    root->insert(5);
    root->inorderTraversal();
    return 0;
}
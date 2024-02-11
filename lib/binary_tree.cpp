#include <iostream>
#include <deque>

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
    int height;
    int size;

public:
    BinaryTree() : root(nullptr), height(0) {}
    ~BinaryTree();
    /*
        Public Interfaces
    */
    void insert(const T value)
    {
        root = insertRecursive(root, value);
    }

    bool search(const T &value)
    {
        return _search(root, value) != nullptr;
    };

    void remove(const T &value);

    void inorderTraversal()
    {
        _inorderTraversal(root);
    };

    void preorderTraversal()
    {
        _preorderTraversal(root);
    };

    void postorderTraversal()
    {
        _postorderTraversal(root);
    };

    // The max depth of the tree
    int getHeight()
    {
        int currentHeight = 0;
        _getHeight(root, currentHeight);
        return height;
    }

    int getHeight(TreeNode<T> node)
    {
        int currentHeight = 0;
        _getHeight(node, currentHeight);
        return height;
    }

    /*
    @params T val
    @returns
        Whole number if valid val
        -1 for invalid val
    **/
    int getHeight(T val)
    {
        TreeNode<T> node = _search(root, val);
        if (node != nullptr)
            return _getHeight(node, 0);
        else
            return -1;
    }

    // Number of Edges
    int getSize()
    {
        int order = getOrder();
        return order - 1;
    }

    // Number of vertices
    int getOrder()
    {
        int tempOrder = 0;
        _getOrder(root, tempOrder);
        return tempOrder;
    }

    void levelOrderTraversal()
    {
        _levelOrderTraversal(root);
    }

private:
    /*
        Private Implementations
    */

    void _levelOrderTraversal(TreeNode<T> *root)
    {
        if (!root)
            return;

        deque<TreeNode<T> *> dq;
        dq.push_front(root);

        while (!dq.empty())
        {
            root = dq.front();
            dq.pop_front();
            cout << root->data << " ";

            if (root->left)
            {
                dq.push_back(root->left);
            }
            if (root->right)
            {
                dq.push_back(root->right);
            }
        }
    }

    void _getHeight(TreeNode<T> *root, int currentHeight = 0)
    {
        if (!root)
        {
            height = max(height, currentHeight - 1);
            return;
        }
        _getHeight(root->left, currentHeight + 1);
        _getHeight(root->right, currentHeight + 1);
    }

    void _getOrder(TreeNode<T> *root, int &order)
    {
        if (root)
            order++;
        if (!root)
            return;

        _getOrder(root->left, order);
        _getOrder(root->right, order);
    }

    void _getNode(TreeNode<T> *root, int val)
    {
    }

    void _getDepth()
    {
    }

    TreeNode<T> _search(TreeNode<T> *root, T &value)
    {
        if (root == nullptr)
            return nullptr;

        if (value > root->data)
        {
            return _searchBST(root->right, value);
        }
        else if (value < root->data)
        {
            return _searchBST(root->left, value);
        }
        return root;
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

    void _preorderTraversal(TreeNode<T> *root)
    {
        if (root == nullptr)
            return;
        cout << root->data << " -> ";
        _inorderTraversal(root->left);
        _inorderTraversal(root->right);
    }

    void _postorderTraversal(TreeNode<T> *root)
    {
        if (root == nullptr)
            return;
        _postorderTraversal(root->left);
        _postorderTraversal(root->right);
        cout << root->data << " -> ";
    }
};

int main(void)
{
    BinaryTree<int> *root = new BinaryTree<int>();
    root->insert(7);
    root->insert(4);
    root->insert(5);
    root->insert(9);
    root->insert(8);
    root->levelOrderTraversal();
    return 0;
}

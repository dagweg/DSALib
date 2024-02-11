#include <iostream>
#include <vector>
#include <map>

using namespace ::std;

// Unweighted & Undirected Graph Definition
template <class T>
class Graph
{
    map<T, vector<T>> adjacency;

public:
    Graph(){};
    ~Graph(){};

    // public interfaces
    void addVertex(const T vertex);
    void addEdge(const T vertex1, const T vertex2);
    void removeVertex(const T vertex);
    void removeEdge(const T vertex1, const T vertex2);
    bool hasVertex(const T vertex) const;
    bool hasEdge(const T vertex1, const T vertex2) const;
    int getDegree(const T vertex) const;
    vector<T> &getNeighbours(const T vertex) const;
    vector<T> &depthFirstTraversal(T sourceVertex);
    vector<T> &breadthFirstTraversal(T sourceVertex);

private:
    void _addVertex(const T vertex);
    void _addEdge(const T vertex1, const T vertex2);
    void _removeVertex(const T vertex);
    void _removeEdge(const T vertex1, const T vertex2);
    bool _hasVertex(const T vertex) const;
    bool _hasEdge(const T vertex1, const T vertex2) const;
    int _getDegree(const T vertex) const;
    vector<T> &_getNeighbours(const T vertex) const;
    vector<T> &_depthFirstTraversal(T sourceVertex);
    vector<T> &_breadthFirstTraversal(T sourceVertex);
};

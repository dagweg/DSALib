#include <iostream>
#include <graph.hpp>
#include <algorithm>

using namespace ::std;

// Implementation FIle

template <class T>
void Graph<T>::_addVertex(const T vertex)
{
    if (adjacency.count(vertex))
    {
        cerr << "Vertex already present in graph!";
        return;
    }

    // Initialize the adjacency for the new vertex with an empty vector
    adjacency[vertex] = vector<bool>();
}

template <class T>
void Graph<T>::_addEdge(const T vertex1, const T vertex2)
{
    if (!adjacency.count(vertex1) || !adjacency.count(vertex2))
    {
        cerr << "Vertices must be present within the graph!";
        return;
    }

    auto &neighbors1 = adjacency[vertex1];
    auto &neighbors2 = adjacency[vertex2];

    if (find(neighbors1.begin(), neighbors1.end(), vertex2) != neighbors1.end())
    {
        cerr << "The vertices you are trying to asscociate are already neighbors";
        return;
    }

    neighbors1.emplace_back(vertex2);
    neighbors2.emplace_back(vertex1);
}

template <class T>
void Graph<T>::_removeVertex(const T vertex)
{
    if (!adjacency.count(vertex))
    {
        cerr << "Vertex isn't present in the graph!";
        return;
    }

    // Remove any adjacency with other vertices
    for (auto &kv : adjacency)
    {
        auto &adjList = kv.second;
        kv.second.erase(remove(adjList.begin(), adjList.end(), vertex), adjList.end());
    }

    // Remove the actual vertex
    adjacency.erase(vertex);
}

template <class T>
void Graph<T>::_removeEdge(const T vertex1, const T vertex2)
{
    if (!adjacency.count(vertex1) || !adjacency.count(vertex2))
    {
        cerr << "Vertices must be present within the graph!";
        return;
    }

    auto &neighbors1 = adjacency[vertex1];
    auto &neighbors2 = adjacency[vertex2];

    auto iter1 = find(neighbors1.begin(), neighbors1.end(), vertex2);
    auto iter2 = find(neighbors2.begin(), neighbors2.end(), vertex1);

    if (iter1 == neighbors1.end() || iter2 == neighbors2.end())
    {
        cerr << "The edge you are trying to remove is not present.";
        return;
    }

    // Disassociate the vertices
    neighbors1.erase(it1);
    neighbors2.erase(it2);
}
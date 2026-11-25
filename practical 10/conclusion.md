In this practical, we learned how to find the Minimum Spanning Tree (MST) of a connected, undirected weighted graph using Kruskal's algorithm. We understood how the greedy approach sorts all edges in ascending order of their weights and uses the Disjoint Set (Union-Find) data structure to detect cycles and include only valid minimum-weight edges until V - 1 edges are added.

Time and Space Complexity:
- Time Complexity: O(E log E) or O(E log V) for sorting the edges and performing find/union operations, where E is the number of edges and V is the number of vertices.
- Space Complexity: O(V + E) for storing the edges and the parent array for union-find.

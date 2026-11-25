In this practical, we learned how to solve the Travelling Salesman Problem (TSP) using backtracking. We understood how the algorithm explores all possible Hamiltonian cycles starting from an initial city, tracks visited cities to avoid revisiting them, and backtracks to find the tour with the minimum total cost that visits every city exactly once and returns to the origin.

Time and Space Complexity:
- Time Complexity: O(n!) where n is the number of cities, as it explores permutations of unvisited cities.
- Space Complexity: O(n) for the visited array and recursion call stack.

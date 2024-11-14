# main.py

from graph import Graph

def main():
    # Create a graph instance
    g = Graph()

    # Add edges to the graph
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")

    # Perform BFS and DFS
    start_node = "A"
    print("BFS traversal starting from node", start_node + ":")
    print(" -> ".join(g.bfs(start_node)))

    print("\nDFS traversal starting from node", start_node + ":")
    print(" -> ".join(g.dfs(start_node)))

if __name__ == "__main__":
    main()

# graph.py

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_order

    def dfs(self, start, visited=None, dfs_order=None):
        if visited is None:
            visited = set()
        if dfs_order is None:
            dfs_order = []

        visited.add(start)
        dfs_order.append(start)

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, dfs_order)

        return dfs_order

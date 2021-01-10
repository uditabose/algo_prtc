from graph import Graph
from collections import deque


class DFSUtil:
    def __init__(self, graph: Graph):
        self.graph = graph

    def dfs(self, vertex: object):
        if self.graph is None or vertex is None:
            return

        visited = {v: False for v in graph.get_vertices()}
        edge_stack = [vertex]
        dfs_link = []
        while len(edge_stack) > 0:
            current = edge_stack.pop()
            if not visited[current]:
                visited[current] = True
                dfs_link.append(current)

            edges = graph.get_edges_for_vertex(current)
            if edges is None:
                break

            for e in edges:
                if e[1] is None:
                    continue

                if not visited[e[1]]:
                    edge_stack.append(e[1])

        return dfs_link

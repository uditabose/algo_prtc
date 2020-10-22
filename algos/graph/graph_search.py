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


def validate(graph: Graph):
    if graph is None:
        return (False, None)

    vertices = graph.get_vertices()
    if len(vertices) < 2:
        return (False, edges)

    edges = graph.get_edges()
    if len(edges) < 2:
        return (False, edges)

    return (True, None)


def dfs(graph: Graph):
    move_forward = validate(graph)
    if not move_forward[0]:
        return move_forward[1]

    vertices = graph.get_vertices()
    edges = graph.get_edges()
    visited = {e: False for e in edges}

    for vert_idx in range(0, len(vertices)):
        edge_stack = [vertices[vert_idx]]
        dfs_stack = []

        while len(edge_stack) > 0:
            parent = edge_stack.pop()

            if not visited[parent]:
                dfs_stack.append(parent)
            visited[parent] = True

            if parent not in edges or edges[parent] is None:
                continue

            for conn in edges[parent]:
                if not visited[conn]:
                    edge_stack.append(conn)

        print("DFS : ", parent, " # ", dfs_stack)


def bfs(graph: Graph):
    move_forward = validate(graph)
    if not move_forward[0]:
        return move_forward[1]

    vertices = graph.get_vertices()
    edges = graph.get_edges()
    visited = {e: False for e in edges}

    for vert_idx in range(0, len(vertices)):
        edge_queue = deque(vertices[vert_idx])
        bfs_queue = deque()

        while len(edge_queue) > 0:
            parent = edge_queue.popleft()

            if not visited[parent]:
                bfs_queue.append(parent)
            visited[parent] = True

            if parent not in edges or edges[parent] is None:
                continue

            for conn in edges[parent]:
                if not visited[conn]:
                    edge_queue.append(conn)

        print("BFS : ", parent, " # ", list(bfs_queue))


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "d")

    graph.add_edge("b", "c")

    graph.add_edge("c", "b")
    graph.add_edge("c", "c")
    graph.add_edge("c", "d")
    graph.add_edge("c", "d")

    graph.add_edge("d", "a")
    graph.add_edge("d", "c")

    graph.add_edge("e", "c")
    graph.add_edge("f", None)

    # dfs(graph)
    # print("=============")
    # bfs(graph)

    dfs_util = DFSUtil(graph)
    print(dfs_util.dfs("c"))
    print(dfs_util.dfs("b"))
    print(dfs_util.dfs("f"))

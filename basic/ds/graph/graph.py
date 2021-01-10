from typing import Set, List, Tuple


class Graph:
    def __init__(self, directed: bool = False):
        self.vertices = []
        self.edges = set()
        self.edge_map = {}
        self.directed = directed

    def __str__(self):
        return str(self.edges)

    def add_vertex(self, vertex: object):
        if vertex is None:
            return

        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def get_vertices(self):
        copy = self.vertices[:]
        return copy

    def add_edge(self, from_vertex: object, to_vertex: object, weight: int = 0):
        if from_vertex is None and to_vertex is None:
            return

        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        self.__add_the_edge(from_vertex, to_vertex, weight)

        if not self.directed:
            self.__add_the_edge(to_vertex, from_vertex, weight)

    def get_edges(self):
        return self.edges.copy()

    def get_edges_for_vertex(self, vertex: object):
        if vertex is None:
            return

        return self.edge_map[vertex] if vertex in self.edge_map else None

    def get_sorted_edges(self):
        return sorted(self.edges, key=lambda edge: edge[2])

    def __add_the_edge(self, from_vertex: object, to_vertex: object, weight: int):
        edge_tuple = (from_vertex, to_vertex, weight)
        self.edges.add((from_vertex, to_vertex, weight))

        if from_vertex in self.edge_map:
            self.edge_map[from_vertex].append(edge_tuple)
        else:
            self.edge_map[from_vertex] = [edge_tuple]


if __name__ == '__main__':
    graph = Graph(True)
    graph.add_edge("a", "d", 10)

    graph.add_edge("b", "c", 1)

    graph.add_edge("c", "b", 3)
    graph.add_edge("c", "c", 5)
    graph.add_edge("c", "d", 5)

    graph.add_edge("d", "a", 80)
    graph.add_edge("d", "c")

    graph.add_edge("e", "c", 2)
    graph.add_edge("f", None)

    print(graph)
    print(graph.get_edges_for_vertex("c"))
    # print(graph.get_sorted_edges())

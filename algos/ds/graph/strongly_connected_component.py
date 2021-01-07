from graph import Graph
from typing import NamedTuple, List

CC = NamedTuple("CC", [('v', object), ('idx', int),
                ('low_idx', int), ('on_stack', bool)])


def scc(graph: Graph):
    if graph is None:
        return

    vertices = graph.get_vertices()
    if vertices is None:
        return

    vertices_stack = []
    index = 0
    for v in vertices:
        index = find_scc(graph, vertices_stack, v, index)


def find_scc(graph: Graph, vertices_stack: List[CC], vertex: object, index: int):
    if vertex is None:
        return

    root_cc = CC(v=vertex, idx=index, low_idx=index, on_stack=True)
    vertices_stack.append(root_cc)

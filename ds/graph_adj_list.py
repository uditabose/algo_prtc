from collections import defaultdict

class Node(object):
    """
    a node in an adjacency list
    """
    def __init__(self, val=None):
        self.val = val
        self.visited = False

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return "(%s, )" % (self.val)

    def __repr__(self):
        return "(%s)" % (self.val)

        
class GraphAL(object):
    """
    adjacency list representation of graph
    """
    def __init__(self):
        self.adj_list = defaultdict(list) # adjacency list
        self.vertices = {} # vertices

    def add_edge(self, from_val, to_val=None):
        '''
        adds both values as vertices to vertices array
        and adds an edge if both from and to values are not 
        null
        '''
        if from_val == None:
            return

        from_node = None
        if from_val in self.vertices:
            from_node = self.vertices[from_val]
        else:
            from_node = Node(from_val)
            self.vertices[from_val] = from_node

        if to_val != None:
            to_node = Node(to_val)
            self.vertices[to_val] = to_node
            self.adj_list[from_node].append(to_node)


    def bfs(self):
        if len(self.adj_list) == 0:
            return

        for key in self.vertices:
            bfs_q = [self.vertices[key]]
            key.visited = True
            print(key, end = ' ')

            while len(bfs_q) > 0:
                bn = bfs_q.pop(0)
                if bn.visited == False:
                    print(bn, end = ' ')
                bn.visited = True
                if bn in self.adj_list:
                    for bnal in self.adj_list[bn]:
                        if bnal.visited == False:
                            bfs_q.append(bnal)

            print("")

    def dfs(self):
        if len(self.adj_list) == 0:
            return

        for key in self.vertices:
            key_node = self.vertices[key]
            dfs_s = [key_node]
            key_node.visited = True
            print(key, end = ' ')

            while len(dfs_s) > 0:
                bn = dfs_s.pop() # only difference
                if bn.visited == False:
                    print(bn, end = ' ')
                bn.visited = True
                if bn in self.adj_list:
                    for bnal in self.adj_list[bn]:
                        if bnal.visited == False:
                            dfs_s.append(bnal)

            print("")

    def connected_component(self):
        if len(self.adj_list) == 0:
            return []

        conn_components = []
        for key in self.vertices:
            key_node = self.vertices[key]
            dfs_q = [key_node]
            comp = set([])
            if key_node.visited == False:
                comp.add(key_node)
            key_node.visited = True

            while len(dfs_q) > 0:
                cp = dfs_q.pop()
                if cp.visited == False:
                    comp.add(cp)
                cp.visited = True
                if cp in self.adj_list:
                    for cpal in self.adj_list[cp]:
                        if cpal.visited == False:
                            dfs_q.append(cpal)

            if len(comp) > 0:
                conn_components.append(comp)

        return conn_components

def graph_adj_list():

    graphAl = GraphAL()
    graphAl.add_edge(0, 1)
    graphAl.add_edge(0, 2)
    graphAl.add_edge(1, 2)
    graphAl.add_edge(2, 0)
    graphAl.add_edge(2, 3)
    graphAl.add_edge(3, 3)
    graphAl.add_edge(4)

    #graphAl.bfs()
    #graphAl.dfs()
    print(graphAl.connected_component())
        
def run():
    graph_adj_list()

if __name__ == '__main__':
    run()


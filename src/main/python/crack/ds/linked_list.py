class Node :
    '''
    node for linked list
    '''
    def __init__(self, data=None, next_node=None) :
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def __str__(self):
        if self.data == None:
            return "None"
        return "%s->%s" % (str(self.data), str(self.next_node))

    def __repr__(self):
        return self.__str__()

class LinkedList:
    """
    implementation of singly linked list
    """
    def __init__(self, node=None):
        self.node = node
        #self.size = 0

    def get_head(self):
        return self.node

    def set_head(self, node):
        if self.node == None:
            self.node = node
        elif node == None:
            self.node = None
        else :
            node.set_next(self.node)
            self.node = node

    def insert_head(self, data):
        if self.node == None:
            self.node = Node(data)
        else:
            new_head = Node(data)
            old_head = self.node
            self.node = new_head
            self.node.set_next(old_head)

    def get_last(self):
        if self.node == None :
            return None
        else :
            curr_node = self.node
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
        return curr_node

    def get_prev(self, node) :
        prev_node = None
        curr_node = self.node

        while curr_node != node:
            prev_node = curr_node
            curr_node = curr_node.get_next()
        return prev_node

    def insert(self, data):
        new_node = Node(data)

        if (self.node == None) :
            self.node = new_node
        else :
            curr_node = self.node
            while (curr_node.get_next() != None) :
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

        #self.size = self.size + 1

    def delete(self, node):

        if (self.node == None) :
            return None

        prev_node = None
        curr_node = self.node

        while (curr_node != node) :
            prev_node = curr_node
            curr_node = curr_node.get_next()

        if (curr_node != None):
            prev_node.set_next(curr_node.get_next())
            #self.size = self.size - 1
            return curr_node
        else :
            return None
    
    def _size_(self, node) :
        if node != None :
            return 1 + self._size_(node.get_next())
        else :
            return 0

    def size(self) :
        return self._size_(self.node)

    def search(self, data):

        prev_node = None
        curr_node = self.node
        while (curr_node != None):
            if (curr_node.get_data() != data) :
                prev_node = curr_node
                curr_node = curr_node.get_next()
            else :
                break;

        return curr_node, prev_node

    def build(self, vals):
        curr_node = self.node
        for v in vals:
            self.insert(v)

    def dump(self):
        print("\n**************")
        print("List of size %i" % self.size())
        print("----------------")
        if (self.node == None) :
            print("empty list")
            return

        curr_node = self.node
        repr_str = ""
        while (curr_node != None):
            repr_str = "%s->%s" % (repr_str, curr_node.get_data())
            curr_node = curr_node.get_next()

        return repr_str

    def __repr__(self):    
        return self.dump()



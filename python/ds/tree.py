#!/usr/local/bin/python3


import random
class Node(object):
    """ a tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __dump__(self):
        return self.value

    def __str__(self):
        return self.__dump__()

    def __repr__(self):
        return self.__dump__()

class BinaryTree(Node):
    """ binary tree"""
    def __init__(self, value):
        super(BinaryTree, self).__init__(value)

    def add_left(self, value):
        self.left = BinaryTree(value)
        return self.left

    def add_right(self, value):
        self.right = BinaryTree(value)
        return self.right

    def add_node(self, value, to_left=True):
        if to_left:
            self.add_left(value)
        else:
            self.add_right(value)

    def random_node(self):
        # an utility method, to find a node with 
        # an empty child at any random level
        # to aide building a non-deterministic binary tree
        curr = self
        prev = None
        while curr:
            # determine if any child is missing
            if not curr.left or not curr.right:
                level = random.random() * 10
                # if the random number is more than 5, 
                # then this is the node
                if level > 5:
                    return curr

            # we traverse down, randomly to left or right
            lor = random.random() * 10
            prev = curr # ease of return
            if lor < 5:
                # predicate random value is less than 5, 
                # so go down left
                curr = curr.left
            else:
                curr = curr.right

        # current is None, so previous must have at least
        # one child node free
        return prev
            
    def __dump__(self, dump=""):
        if not self:
            return dump
        dump = "%s << %s >> %s" % (self.left.__dump__(dump) if self.left else "*", 
                                   str(self.value),
                                   self.right.__dump__(dump) if self.right else "#")
        return dump

    def __str__(self):
        return self.__dump__()

    def __repr__(self):
        return self.__dump__()
            
class BinarySearchTree(BinaryTree):
    """Binary Search Tree, left is less, right is more"""
    def __init__(self, value):
        super(BinarySearchTree, self).__init__(value)

    def add_node(self, value):
        curr = self
        prev = None
        while curr:
            prev = curr
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left

        if value > prev.value:
            prev.right = BinarySearchTree(value)
        else:
            prev.left = BinarySearchTree(value)

def make_binary_tree(num_arr):
    if not num_arr:
        return None

    bnt = BinaryTree(num_arr[0])
    curr = bnt
    for x in num_arr[1:]:
        if not curr.left and not curr.right:
            to_left = (random.random() * 10 < 5)
            curr.add_node(x, to_left)
        elif not curr.left:
            curr.add_node(x)
        else:
            curr.add_node(x, False)
        
        curr = bnt.random_node()

    return bnt

def make_binary_search_tree(num_arr):
    if not num_arr:
        return None

    bst = BinarySearchTree(num_arr[0])
    for x in num_arr[1:]:
        bst.add_node(x)

    return bst
    
def inorder(node):
    if not node:
        print('-', end='')
        return

    inorder(node.left)
    print(node.value, end='#')
    inorder(node.right)
    print()

def preorder(node):
    if node == None:
        print('-', end='')
        return

    print(node.value, end='#')
    preorder(node.left)
    preorder(node.right)
    print()

def postorder(node):
    if not node:
        print('-', end='')
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value, end='#')
    print()

def run():
    num_arr = list(range(2, 27, 3))
    random.shuffle(num_arr)
    bnt = make_binary_tree(num_arr)
    bst = make_binary_search_tree(num_arr)

    print(num_arr)
    print("===================")
    print(bnt)
    print("-------------------")
    print(bst)

    print("%%%%%%%%%%%%%%%%%%")
    inorder(bst)
    #print("%%%%%%%%%%%%%%%%%%")
    #bst.preorder()
    #print("%%%%%%%%%%%%%%%%%%")
    #bst.postorder()

if __name__ == '__main__':
    run()
        
              
    

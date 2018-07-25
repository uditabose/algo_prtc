#!/usr/local/bin/python3

class TreeNode(object):
    """ a node in a tree """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __dump__(self, level):
        dump = "" 
        #* level
        dump = "%s%s" % (dump, "^" * level)
        return "%s%s" % (dump, self.value)

    def __str__(self):
        print(self.value, end=' ')
        
    def inorder(self, level=0):
        if self.left:
            self.left.inorder(level+1)
        
        print(self.__dump__(level), end=' ')
        
        if self.right:    
            self.right.inorder(level+1)

class BinarySearchTree(TreeNode):
    """ BinarySearchTree """
    def __init__(self, value):
        super(BinarySearchTree, self).__init__(value)
    
    def add_node(self, value):
        curr = self
        prev = None
        while curr:
            if value <= curr.value:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        node = BinarySearchTree(value)
        if value <= prev.value:
            prev.left = node
        else:
            prev.right = node

def make_bst(arr):
    if not arr:
        return None

    bst = BinarySearchTree(arr[0])
    for v in arr[1:]:
        bst.add_node(v)
    return bst
            
def run():
    arr = [10,7,14,45,2,8,9,12,23]
    bst = make_bst(arr)
    bst.inorder()
    print()

if __name__ == '__main__':
    run()
    
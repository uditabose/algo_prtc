
# Write a function to see if a binary tree 
# is "super-balanced" (a new tree property we just made up).
# A tree is "super-balanced" if the difference 
# between the depths of any two leaf nodes ↴ 
# is no greater than one.

# https://www.interviewcake.com/question/python/balanced-binary-tree

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __repr__(self):
        tree_rep = " (%s) " % str(self.value)
        left_repr = ""
        right_repr = ""
        
        if self.left != None:
            left_repr = "%s <- " % str(self.left)

        tree_rep = " (%s) " % str(self.value)

        if self.right != None:
            right_repr = " -> %s" % str(self.right)

        return "%s%s%s" % (left_repr, tree_rep, right_repr)

class BalancedBinaryTree(BinaryTreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.left_depth = 0
        self.right_depth = 0

    def insert(self, value):
        if (self.left_depth - self.right_depth == 0):
            self.insert_left(value)
            self.left_depth += 1
        elif (self.left_depth - self.right_depth > 0):
            self.insert_right(value)
            self.left_depth += 1
        else:
            self.insert_left(value)
            self.left_depth += 1

if __name__ == '__main__':
    bbt = BalancedBinaryTree(0)
    bbt.insert(10)
    bbt.insert(11)
    bbt.insert(12)
    bbt.insert(13)
    bbt.insert(14)
    bbt.insert(15)
    bbt.insert(16)
    bbt.insert(17)
    bbt.insert(18)
    bbt.insert(19)

    print(bbt)


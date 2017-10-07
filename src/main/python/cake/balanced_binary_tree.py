
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



class BalancedBinaryTree(BinaryTreeNode):
    def __init__(self):
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
    bbt = BalancedBinaryTree()
    bbt.insert(10)



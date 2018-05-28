
import sys
sys.path.append('./ds/')

from stack_queue import Node, Stack 

def stack_min():
    '''
    3.2 Design a stack with an additional function
    `min` that returns minimum value of the stack at O(1)

    Time :
    Space:
    Note :
    '''
    pass

class StackMin(Stack):
    '''
    3.2 Design a stack with an additional function
    `min` that returns minimum value of the stack at O(1)

    Time :
    Space:
    Note :
    '''

    def __init__(self):
        '''
        overridden to add a new variable to store the minimum
        value of the stack
        '''
        super().__init__()
        self.min_val = None

    def push(self, data):
        super().push(data)
        self.min_val = data if self.min_val == None else min(data, self.min_val)

    def pop(self):
        ret_val = super().pop()
        self.__find_min__()

    def get_min(self):
        return self.min_val

    def __find_min__(self):
        self.min_val = self.head.data 
        curr = self.head
        while curr != None:
            if self.min_val > curr.data:
                self.min_val = curr.data
            curr = curr.next

def make_stack(num_arr):
    stack_min = StackMin()
    for x in num_arr:
        stack_min.push(x)
    return stack_min

def run():
    num_arr = [700, 56, 811, 76, 34, 12, 9, 981]
    stack_min = make_stack(num_arr)
    print("min 1 %d" % stack_min.get_min())
    stack_min.pop()
    print("min 2 %d" % stack_min.get_min())
    stack_min.pop()
    stack_min.pop()
    print("min 3 %d" % stack_min.get_min())


if __name__ == '__main__':
    run()


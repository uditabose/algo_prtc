import sys

class MinStack(object):
    '''
    Design a stack that supports push, pop, top, 
    and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

    https://leetcode.com/problems/min-stack/description/

    Time : O(N)
    Space: O(N)
    Note :
    at every value a `local` min value is kept
    `local` min value is the minimum up until current value 
    '''
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val):
        if self.min_val == None or self.min_val > val:
            self.min_val = val

        self.stack.append((val, self.min_val))

    def pop(self):
        last = self.stack.pop()
        if len(self.stack) > 0:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = None
        return last[0]

    def getMin(self):
        return self.min_val

    def top(self):
        return self.stack[-1][0]


def run():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())

    print("-------------------")
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(4)
    min_stack.push(6)
    min_stack.push(7)
    min_stack.push(1)
    min_stack.push(2)

    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.pop())
    print(min_stack.pop())
    print(min_stack.pop())
    print(min_stack.getMin())


if __name__ == '__main__':
    run()


#!/usr/local/bin/python3

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def __repr__(self):
        return str(self.items)

class Queue(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        while True:
            item = self.in_stack.pop()
            if item == None:
                break
            self.out_stack.push(item)

        return self.out_stack.pop()

    def __repr__(self):
        return str(self.in_stack) + "\n" + str(self.out_stack)


def queue_two_stacks():
    """
    https://www.interviewcake.com/question/python3/queue-two-stacks

    Time :
    Space:
    Note :
    """
    queue = Queue()
    for item in [1, 3, 4, 5, 6]:
        queue.enqueue(item)

    for i in range(0, 2):
        print(queue.dequeue())

    # this will screw it up
    for item in [500, 100]:
        queue.enqueue(item)

    while True:
        item = queue.dequeue()
        if item == None:
            break
        print(item)



def run():
    queue_two_stacks()


if __name__ == '__main__':
    run()

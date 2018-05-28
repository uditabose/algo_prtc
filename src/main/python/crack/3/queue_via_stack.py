import sys
sys.path.append('./ds/')

from stack_queue import Node, Stack 

class QueueViaStack(object):
    '''

    Time :
    Space:
    Note :
    '''
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def push(self, data):
        self.input.push(data)

    def pop(self):
        if self.input.empty() and self.output.empty():
            return None
        
        curr = self.input.pop()
        while curr != None:
            self.output.push(curr.data)
            curr = self.input.pop()
        
        return self.output.pop()

def run():
    qvs = QueueViaStack()
    qvs.push(10)
    qvs.push(20)
    qvs.push(30)
    print(qvs.pop())
    qvs.push(100)
    qvs.push(200)
    print(qvs.pop())
    print(qvs.pop())

if __name__ == '__main__':
    run()


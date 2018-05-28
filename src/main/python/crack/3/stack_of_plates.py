
import sys
sys.path.append('./ds/')

from stack_queue import Node, Stack 

class SetOfStacks(object):
    """
    3.3 Implement SetOfStacks which spills after a threshold

    Time :
    Space:
    Note :
    """
    def __init__(self, threshold):
        self.__threshold__ = threshold
        self.__stack_list__ = []

    def push(self, data):
        if len(self.__stack_list__) == 0:
            self.__stack_list__.append(Stack())
        else:
            last = self.__stack_list__[-1]
            if last.length() >= self.__threshold__:
                self.__stack_list__.append(Stack())
        
        self.__stack_list__[-1].push(data)
        #print(self.__stack_list__)

    def pop(self):
        if len(self.__stack_list__) == 0:
            return None

        last = self.__stack_list__[-1]
        if last == None or last.length() == 0:
            return None
        
        ret_val = last.pop()

        if last == None or last.length() == 0:
            self.__stack_list__.pop(-1)

        return ret_val

    def pop_at(self, stack_idx):
        stacks_len = len(self.__stack_list__)
        if stacks_len == 0 or stack_idx >= stacks_len:
            return None

        last = self.__stack_list__[stack_idx]
        if last == None or last.length() == 0:
            return None
        
        ret_val = last.pop()

        if last == None or last.length() == 0:
            self.__stack_list__.pop(stack_idx)

        return ret_val

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__stack_list__)

        

def stack_of_plates():
    plates = [23,67,323,976,213,6,78,85]

    stack = Stack()
    for x in plates:
        stack.push(x)

    print(stack)
    print(stack.length())
    
    threshold = 2

    set_of_stacks = SetOfStacks(threshold)
    for x in plates:
        set_of_stacks.push(x)

    print(set_of_stacks)

    set_of_stacks.push(100)
    print(set_of_stacks)

    set_of_stacks.push(200)
    print(set_of_stacks)

    set_of_stacks.pop()
    print(set_of_stacks)

    set_of_stacks.pop_at(0)
    print(set_of_stacks)

    

def run():
    stack_of_plates()

if __name__ == '__main__':
    run()



class ArrayStack():
    ''' 
    Stacks via array, multiple arrays 
    with fixed length
    '''
    def __init__(self, no_of_stacks=3):
        self.no_of_stacks = no_of_stacks
        self.backing_array = []
        for x in range(0, 10 * no_of_stacks):
            self.backing_array.append(None)

        self._stack_const_pos_ = []
        self.stack_pos = []
        for x in range(0, no_of_stacks):
            self._stack_const_pos_.append((x * 10, x * 10 + 9))
            self.stack_pos.append((-1, -1))

    def push(self, stack_id, data):
        
        if self.stack_pos[stack_id][0] < 0:
            # it's the first element
            self.backing_array[self._stack_const_pos_[stack_id][0]] = data
            self.stack_pos[stack_id] = (self._stack_const_pos_[stack_id][0], 
                 self._stack_const_pos_[stack_id][0])

        next_idx = self.stack_pos[stack_id][1] + 1
        if next_idx > self._stack_const_pos_[stack_id][1]:
            next_idx = next_idx - self._stack_const_pos_[stack_id][1] + self._stack_const_pos_[stack_id][0]

        if self.backing_array[next_idx] != None:
            print("overflowing")
            return
        
        self.backing_array[next_idx] = data
        self.stack_pos[stack_id] = (self.stack_pos[stack_id][0], next_idx)

    def pop(self, stack_id):
        curr_top_idx = self.stack_pos[stack_id][0]
        if curr_top_idx < 0:
            return None

        top_idx = curr_top_idx + 1
        if top_idx > self._stack_const_pos_[stack_id][1]:
            top_idx = self._stack_const_pos_[stack_id][0]

        data = self.backing_array[curr_top_idx]
        if data == None:
            print("underflowing")
            return
        
        self.backing_array[curr_top_idx] = None
        self.stack_pos[stack_id] = (top_idx, self.stack_pos[stack_id][1])
        return data


    def peek(self, stack_id):
        if self.stack_pos[stack_id][0] < 0:
            return None

        top_idx = self.stack_pos[stack_id][0] + 1
        if top_idx > self._stack_const_pos_[stack_id][1]:
            top_idx = self._stack_const_pos_[stack_id][0]

        return self.backing_array[top_idx]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.backing_array)

def three_stacks():
    '''
    3.1 use single array to implement 3 stacks
    '''
    array_stack = ArrayStack()
    for x in range(0, 3):
        for y in range(x * 10, x * 10 + 9):
            array_stack.push(x, y)

    print(array_stack)

    print(array_stack.peek(0))
    print(array_stack.peek(1))
    print(array_stack.peek(2))

    print(array_stack.pop(0))
    print(array_stack.pop(1))
    print(array_stack.pop(2))

    print(array_stack.pop(0))
    print(array_stack.pop(1))
    print(array_stack.pop(2))

    print(array_stack.pop(0))
    print(array_stack.pop(1))
    print(array_stack.pop(2))

    print(array_stack.push(0, 200))
    print(array_stack.push(1, 300))
    print(array_stack.push(2, 400))

    print(array_stack)

def run():
    three_stacks()

if __name__ == '__main__':
    run()

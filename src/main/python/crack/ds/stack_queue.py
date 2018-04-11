class Node :

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.data == None:
            return "None"
        return str(self.data)

class Stack (object):
    """
    Stack is a linear data structure which follows a particular 
    order in which the operations are performed. The order may be 
    LIFO(Last In First Out) or FILO(First In Last Out).

    Mainly the following three basic operations are performed in the stack:
    
    Push: Adds an item in the stack. If the stack is full, 
          then it is said to be an Overflow condition.

    Pop: Removes an item from the stack. The items are popped 
         in the reversed order in which they are pushed. If the 
         stack is empty, then it is said to be an Underflow condition.
    
    Peek: Get the topmost item.
    """
    def __init__(self):
        self.head = None


    def push(self, data):
        if data == None:
            return

        if self.head == None:
            self.head = Node(data)
        else :
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop(self):
        if self.head == None:
            return None
        else :
            ret = self.head
            new_head = self.head.next

            if new_head != None:
                new_head.prev = None
            
            ret.next = None
            self.head = new_head
            return ret

    def peek(self):
        if self.head == None:
            return None
        else :
            return self.head.data

    def empty(self):
        return (self.head == None)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        rpr = None
        if self.head == None:
            rpr = "None"
        else :
            rpr = str(self.head)
        return "<%s>" % (rpr)

    def dump(self):
        if self.head == None:
            return "None"

        curr = self.head
        d_str = ""  
        while curr != None:
            d_str = "%s:%s" % (str(curr), d_str)
            curr = curr.next
        return d_str

class Queue(object):
    """Queue implements FIFO ordering"""
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data=data)
            self.last = self.head
        elif self.last == None:
            self.last = Node(data=data)
        else:
            new_last = Node(data=data)
            self.last.next = new_last
            self.last = new_last

    def remove(self):
        if self.head == None:
            return None
        else:
            old_head = self.head
            self.head = self.head.next

            return old_head

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.dump()

    def dump(self):
        if self.head == None:
            return "None"

        curr = self.head
        d_str = ""  
        while curr != None:
            d_str = "%s:%s" % (str(curr), d_str)
            curr = curr.next
        return d_str

        
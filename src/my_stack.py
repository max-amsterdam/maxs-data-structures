from src.my_linked_list import MyLinkedList

class MyStack(object):

    def __init__(self):
        self.stack = MyLinkedList() 

    def push(self, val):
        self.stack.addLast(val)
    
    def pop(self):
        if self.isEmpty():
            raise 
        return self.stack.removeLast()
    
    def peek(self):
        return self.stack.getLast()  # Returns the last element

    def isEmpty(self):
        return len(self) == 0

    def __eq__(self, other):
        return self.stack.__eq__(other.stack) 

    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self)
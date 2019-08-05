from src.my_linked_list import MyLinkedList

class MyQueue(object):

    def __init__(self):
        self.queue = MyLinkedList()

    def enqueue(self, val):
        self.queue.addFirst(val)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.removeLast()

    def isEmpty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue) 
    
    def __repr__(self):
        return str(self) 
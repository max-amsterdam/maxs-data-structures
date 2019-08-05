class Node(object):

    def __init__(self, val, prev = None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return "Node with value {}".format(self.val)

    def __repr__(self):
        return self.__str__ 


class MyLinkedList(object):

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 

    def get(self, pos):
        self.checkValidPos(pos)
        temp = self.head.next
        for _ in range(pos):
            temp = temp.next
        return temp.val

    def getFirst(self):
        return self.head.next.val
    
    def getLast(self):
        return self.tail.prev.val
    
    def set(self, pos, val):
        self.checkValidPos(pos)
        temp = self.head.next
        for _ in range(pos):
            temp = temp.next
        # Does this work because of pass by reference? Does changing temps value change the actual value of the Node?
        temp.val = val

    def contains(self, val):
        temp = self.head.next
        while temp.next is not None:
            if temp.val == val:
                return True 
            temp = temp.next
        return False

    def add(self, pos, val):
        self.checkValidPos(pos)
        if pos == 0:
            self.addFirst(val)
        elif pos == self.size-1:
            self.addLast(val)
        else:
            temp = self.head
            for _ in range(pos):
                temp = temp.next
            node = Node(val)
            node.next = temp.next
            node.prev = temp
            temp.next = node
            node.next.prev = node 
            self.size += 1

    def addFirst(self, val):
        node = Node(val)
        node.prev = self.head        
        node.next = self.head.next
        self.head.next = node 
        node.next.prev = node 
        self.size += 1
    
    def addLast(self, val):
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        self.size += 1

    def remove(self, pos):
        self.checkValidPos(pos)
        temp = self.head.next
        for _ in range(pos):
            temp = temp.next
        toRemoveVal = temp.val
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.size -= 1
        return toRemoveVal
    
    def removeFirst(self):
        toRemoveVal = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return toRemoveVal

    def removeLast(self):
        toRemoveVal = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return toRemoveVal

    def checkValidPos(self, pos):
        if pos < 0 or pos >= self.size:
            raise IndexError("The given index is out of bounds.")
    
    def __len__(self):
        return self.size

    def __eq__(self, other):
        tempSelf = self.head.next
        tempOther = other.head.next
        while tempSelf is not None and tempOther is not None:
            if tempSelf.val != tempOther.val:
                return False
            tempSelf, tempOther = tempSelf.next, tempOther.next
        return True

    def __str__(self):
        strList = list()
        strList.append("[")
        currNode = self.head.next
        while currNode.next is not None:
            strList.append(str(currNode.val))
            currNode = currNode.next
            if currNode.next is not None:
                strList.append(", ")
        strList.append("]")
        return "".join(strList)

    def __repr__(self):
        return str(self)

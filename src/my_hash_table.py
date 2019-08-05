from src.my_linked_list import MyLinkedList
import math

class MyHashTable(object):

    # Large Prime
    MAX_LOAD_FACTOR = .7

    def __init__(self, numBuckets):
        self.buckets = numBuckets
        self.hashtable = self.getEmptyHashTable()
        self.size = 0
    
    def getEmptyHashTable(self):
        hashtable = list()
        for i in range(self.buckets):
            hashtable.append(MyLinkedList())
        return hashtable

    def hash(self, string):
        # Note: this hash function only works for strings 
        sum = 0
        # Sum of the ASCII value of each character times it's position in the array (starting at 1)
        for i, c in enumerate(string):
            sum += (i+1) * ord(c)
        result = sum % self.buckets
        return sum % self.buckets

    def get(self, key):
        index = self.hash(key)
        desiredList = self.hashtable[index]
        for i in range(len(desiredList)):
            currKey, currValue = desiredList.get(i)
            if(currKey == key):
                return currValue
        return None
    
    def put(self, key, value):
        self.checkLoadFactor()
        index = self.hash(key)
        # Inserts tuple of key, value
        self.hashtable[index].addFirst((key, value))
        self.size += 1
    
    def pop(self, key):
        index = self.hash(key)
        desiredList = self.hashtable[index]
        for i in range(len(desiredList)):
            currKey, currValue = desiredList.get(i)
            if(currKey == key):
                desiredList.remove(i)
                self.size -= 1
                return currValue
        return None

    def contains(self, val):
        for list in self.hashtable:
            for i in range(len(list)):
                currKey, currVal = list.get(i)
                if currVal == val:
                    return True
        return False

    def containsKey(self, key):
        index = self.hash(key)
        desiredList = self.hashtable[index]
        for i in range(len(desiredList)):
            currKey, currValue = desiredList.get(i)
            if(currKey == key):
                return True 
        return False 

    def checkLoadFactor(self):
        if self.size/self.buckets > self.MAX_LOAD_FACTOR:
            self.rehash()

    def rehash(self):
        print("Rehashing...")
        newHashTable = MyHashTable(self.getNextLargestPrime(self.buckets*2))
        for list in self.hashtable:
            for i in range(len(list)):
                currKey, currValue = list.get(i)
                newHashTable.put(currKey, currValue)
        self.hashtable = newHashTable.hashtable
        self.size = newHashTable.size
        self.buckets = newHashTable.buckets
    
    def getNextLargestPrime(self, num):
        currNum = num
        while True:
            if self.isPrimeNumber(num):
                print("Next largest prime is: {}".format(num))
                return num
            num += 1
        
    def isPrimeNumber(self, num):
        if num < 0:
            raise ArithmeticError("Cannot evaluate negative prime numbers.")

        if num <= 2 or num % 2 == 0:
            return False

        for divisor in range(3, round(math.sqrt(num)), 2):
            if num % divisor == 0:
                return False
        return True

    def isEmpty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        strToPrint = [] 
        strToPrint.append("[")
        for list in self.hashtable:
            for i in range(len(list)):
                key, value = list.get(i)
                strToPrint.append("{} : {}, ".format(key, value))
        strToPrint.append("]")
        return "".join(strToPrint)
            
    
    def __repr__(self):
        return str(self)
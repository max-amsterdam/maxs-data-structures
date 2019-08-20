class MyMinHeap(object):
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, val):
        self.heap.append(val)
        self.percUp()
        self.size += 1

    def removeMin(self):
        min_val = self.heap[1]
        self.heap[1] = self.heap.pop()  # Move last element in heap to the root
        self.percDown()
        self.size -= 1
        return min_val

    def percDown(self):
        currIndex = 1
        while currIndex * 2 < len(self.heap):
            l_index, r_index = currIndex * 2, currIndex * 2 + 1
            if r_index == len(self.heap):
                left = self.heap[l_index]
                if self.heap[currIndex] > left:
                    self.swap(currIndex, l_index)
                    currIndex = l_index 
                else:
                    break
            else:
                left, right = self.heap[l_index], self.heap[r_index]
                if left < right and self.heap[currIndex] > left:
                    self.swap(currIndex, l_index)
                    currIndex = l_index
                elif right < left and self.heap[currIndex] > right:
                    self.swap(currIndex, r_index)
                    currIndex = r_index
                else:
                    break


    def percUp(self):
        currIndex = len(self.heap) - 1
        parentIndex = currIndex // 2
        while parentIndex > 0 and self.heap[currIndex] < self.heap[parentIndex]:
            self.swap(currIndex, parentIndex)
            currIndex = parentIndex
            parentIndex = currIndex // 2

    def swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp



    def peekMin(self):
        pass


heap = MyMinHeap()
heap.insert(21)
heap.insert(11)
heap.insert(9)
heap.insert(5)
heap.insert(2)
print(heap)
print(heap.removeMin())
print(heap)
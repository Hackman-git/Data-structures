import math
class HeapBuilder:
    
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        self._data = [int(s) for s in input().split()]
        self.size = len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        i = math.floor(self.size)
        while i >= 0:
            self.SiftDown(i)
            i -= 1

    def LeftChild(self, i):
        return (2*i + 1)

    def RightChild(self, i):
        return (2*i + 2)    

    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        if l < self.size and self._data[l] > self._data[maxIndex]:
            maxIndex = l
        r = self.RightChild(i)
        if r < self.size and self._data[r] > self._data[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            temp = self._data[i]
            self._data[i] = self._data[maxIndex]
            self._data[maxIndex] = temp
            self._swaps.append((i,maxIndex))
            self.SiftDown(maxIndex)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()


def HeapSort():
    heap = HeapBuilder()
    heap.Solve()
    print(heap._data)
    for i in range(len(heap._data) - 1):
        temp = heap._data[0]
        heap._data[0] = heap._data[heap.size - 1]
        heap._data[heap.size - 1] = temp
        heap.size -= 1
        heap.SiftDown(0)

    print(heap._data)

    
HeapSort()
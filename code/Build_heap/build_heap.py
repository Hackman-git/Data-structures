# python3
import math


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        i = math.floor(len(self._data))
        while i >= 0:
            self.SiftDown(i)
            i -= 1

    def LeftChild(self, i):
        return (2 * i + 1)

    def RightChild(self, i):
        return (2 * i + 2)

    def SiftDown(self, i):
        minIndex = i
        l = self.LeftChild(i)
        if l < len(self._data) and self._data[l] < self._data[minIndex]:
            minIndex = l
        r = self.RightChild(i)
        if r < len(self._data) and self._data[r] < self._data[minIndex]:
            minIndex = r
        if i != minIndex:
            temp = self._data[i]
            self._data[i] = self._data[minIndex]
            self._data[minIndex] = temp
            self._swaps.append((i, minIndex))
            self.SiftDown(minIndex)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

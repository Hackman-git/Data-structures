# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        min_heap = MinHeap(self.num_workers)
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = min_heap._data[0][0]
            self.start_times[i] = min_heap._data[0][1]
            min_heap.ChangePriority(0, min_heap._data[0][1] + self.jobs[i])


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

class MinHeap:
    def __init__(self, num_workers):
        # each worker contains (rank(index), next_free_time)
        self._data = []
        self.n = num_workers
        for i in range(num_workers):
            self._data.append((i, 0))

    def ChangePriority(self, index, p):
        old_p = self._data[index][1]
        self._data[index] = (self._data[index][0], p)
        if p < old_p:
            pass
        else:
            self.SiftDown(index)


    def LeftChild(self, i):
        return (2*i + 1)

    def RightChild(self, i):
        return (2*i + 2)  

    def CompareThreads(self, thread1, thread2):
        if thread1[1] != thread2[1]:
            return thread1[1] < thread2[1]
        else:
            return thread1[0] < thread2[0]


    def SiftDown(self, i):
        minIndex = i
        left = self.LeftChild(i)
        if left < self.n and self.CompareThreads(self._data[left], self._data[minIndex]):
            minIndex = left

        right = self.RightChild(i)
        if right < self.n and self.CompareThreads(self._data[right], self._data[minIndex]):
            minIndex = right
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
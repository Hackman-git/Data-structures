#uses Python3

class JobQueue():
    
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in self.result:
          print(i[0], i[1],sep=' ')

    def Child(self,i):
        return i+1

    def Parent(self,i):
        return i-1

    def assign_jobs(self):
        # list for storing the priority queue
        self.pairs = []
        # list for storing the result to be printed out
        self.result = []
        # initialize all end times for all threads to zero
        for i in range(self.num_workers):
            self.pairs.append((i,0))
        # loop through each job and extract minimum end time from the queue
        for i in range(len(self.jobs)):
            x = self.ExtractMin()
            self.result.append(x)
            self.pairs = self.pairs[1:]
            y = (x[0],x[1]+self.jobs[i])
            # insert the new value of the current thread's end time into the queue and Sift Up
            self.Insert(y)
            self.SiftUp(len(self.pairs) - 1)

    def ExtractMin(self):
        return self.pairs[0]

    def Insert(self, i):
        self.pairs.append(i)

    def SiftUp(self, i):
        while i > 0 and self.pairs[i][1] < self.pairs[self.Parent(i)][1]:
            if self.pairs[i][1] == self.pairs[self.Parent(i)][1] and self.pairs[i][0] < self.pairs[self.Parent(i)][0]:
                temp = self.pairs[self.Parent(i)]
                self.pairs[self.Parent(i)] = self.pairs[i]
                self.pairs[i] = temp
            else:
                temp = self.pairs[self.Parent(i)]
                self.pairs[self.Parent(i)] = self.pairs[i]
                self.pairs[i] = temp

            i = self.Parent(i)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
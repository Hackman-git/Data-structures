# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def Find(self,k):
        L = self.elems[self._hash_func(k)]
        if k in L:
            return True
        else:
            return False

    def Add(self, k):
        L = self.elems[self._hash_func(k)]
        if k in L:
            pass
        else:
            self.elems[self._hash_func(k)].insert(0,k)

    def Del(self,k):
        L = self.elems[self._hash_func(k)]
        if k in L:
            self.elems[self._hash_func(k)].remove(k)

    def Check(self, i):
        if len(self.elems[i]) != 0:
            print(' '.join(self.elems[i]))
        else:
            print('')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            self.Check(query.ind)
        elif query.type == 'find':
            if self.Find(query.s) == True:
                print('yes')
            else:
                print('no')
        elif query.type == 'add':
            self.Add(query.s)
        else:
            self.Del(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

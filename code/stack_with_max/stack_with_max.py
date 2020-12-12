#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def peek(self):
         return self.__stack[len(self.__stack)-1]

    # def Max(self):
    #     assert(len(self.__stack))
    #     return max(self.__stack)

class AuxStack():
    def __init__(self):
        self.items = []

    def Push(self, i):
        self.items.append(i)

    def Pop(self):
        assert(len(self.items))
        self.items.pop()

    def Max(self):
        assert(len(self.items))
        return self.items[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    stack2 = AuxStack()
    arr = []
    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
            if len(stack2.items) == 0:
                stack2.Push(int(query[1]))
                continue
            if int(query[1]) >= stack2.items[-1]:
                stack2.Push(int(query[1]))
        elif query[0] == "pop":
            x = stack.peek()
            stack.Pop()
            if int(x) < stack2.items[-1]:
                pass
            elif int(x) == stack2.items[-1]:
                stack2.Pop()
        elif query[0] == "max":
            arr.append(stack2.Max())
        else:
            assert(0)

    for i in arr:
        print(i)

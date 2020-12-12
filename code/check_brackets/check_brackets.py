# python3
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    openBrackStack = []
            
    for i, nex in enumerate(text, 1):
        if nex not in "([{}])":
            continue
        
        if nex in "([{":
            openBrackStack.append((nex,i))
            continue

        if nex in ")]}":
            if len(openBrackStack) == 0:
                return i
            char = openBrackStack.pop()
            match = are_matching(char[0],nex)
            if match == True:
                continue
            else:
                return i

    if len(openBrackStack) == 0:
        return False
    else:
        return openBrackStack[0][1]

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch != False:
        print(mismatch)
    else:
        print('Success')


if __name__ == "__main__":
    main()
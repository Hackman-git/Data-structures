# python3
import sys
import threading

def depthCalc(parents, i, depth):
    # If depth[i] is already filled 
    if depth[i] != 0:
        return

    # If node at index i is root
    if parents[i] == -1:
        depth[i] = 1
        return

    # If depth of parent is not evaluated before, 
    # then evaluate depth of parent first
    if depth[parents[i]] == 0:
        depthCalc(parents, parents[i], depth)

    # Depth of this node is depth of parent plus 1
    depth[i] = depth[parents[i]] + 1

def compute_height(parents):
    n = len(parents)

    # Create an array to store depth of all nodes and  
    # initialize depth of every node as 0
    depth = [0 for i in range(n)]

    # fill depth of all nodes
    for i in range(n):
        depthCalc(parents, i, depth)

    height = depth[0]
    for i in range(1,n):
        height = max(height, depth[i])

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))

    print(compute_height(parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
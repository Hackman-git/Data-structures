#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

n = int(input().strip())
key = [0 for i in range(n)]
left_ind = [0 for i in range(n)]
right_ind = [0 for i in range(n)]

for i in range(n):
  [a, b, c] = map(int, input().strip().split())
  key[i] = a
  left_ind[i] = b
  right_ind[i] = c

inorderResult = []

def inOrder(root = 0):
  global left_ind, right_ind,n
  if  n != 0:
    if left_ind[root] != -1:
        inOrder(left_ind[root])
    if len(inorderResult) >= 1 and key[root] > inorderResult[-1]:
        inorderResult.append(key[root])
    elif len(inorderResult) == 0:
        inorderResult.append(key[root])
    else:
        return
    if right_ind[root] != -1:
        inOrder(right_ind[root])


def IsBinarySearchTree(arr):
  # Implement correct algorithm here
  global n
  if len(arr) == n:
    return True
  else:
      return False


def main():
  inOrder()
#   print(" ".join(str(x) for x in inorderResult))
  if IsBinarySearchTree(inorderResult):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

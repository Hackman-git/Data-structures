# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

n = int(input())
key = [0 for i in range(n)]
left_ind = [0 for i in range(n)]
right_ind = [0 for i in range(n)]

for i in range(n):
  [a, b, c] = map(int, input().split())
  key[i] = a
  left_ind[i] = b
  right_ind[i] = c

inorderResult = []
preorderResult = []
postorderResult = []

def inOrder(root = 0):
  global left_ind, right_ind
  if left_ind[root] != -1:
    inOrder(left_ind[root])
  inorderResult.append(key[root])
  if right_ind[root] != -1:
    inOrder(right_ind[root])


def preOrder(root = 0):
  global left_ind, right_ind
  preorderResult.append(key[root])
  if left_ind[root] != -1:
    preOrder(left_ind[root])
  if right_ind[root] != -1:
    preOrder(right_ind[root])


def postOrder(root = 0):
  global left_ind, right_ind
  if left_ind[root] != -1:
    postOrder(left_ind[root])
  if right_ind[root] != -1:
    postOrder(right_ind[root])
  postorderResult.append(key[root])


def main():
  inOrder()
  preOrder()
  postOrder()
  print(" ".join(str(x) for x in inorderResult))
  print(" ".join(str(x) for x in preorderResult))
  print(" ".join(str(x) for x in postorderResult))

threading.Thread(target=main).start()

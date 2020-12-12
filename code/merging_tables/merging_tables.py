# python3

import sys

n, m = map(int, input().split())
lines = list(map(int, input().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        print(ans)
        return

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] = lines[realSource] + lines[realDestination]
        lines[realSource] = 0
        ans = max(ans, lines[realDestination])
    else:
        parent[realDestination] = realSource
        lines[realSource] = lines[realSource] + lines[realDestination]
        lines[realDestination] = 0
        ans = max(ans, lines[realSource])
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1

    print(ans)
    

for i in range(m):
    destination, source = map(int, input().split())
    merge(destination - 1, source - 1)
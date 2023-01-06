from collections import Counter


def minMax(a, b):
    if a < b: 
        return a, b
    else: 
        return b, a


def union(p, q):
    id1, id2 = minMax(root[p], root[q])
    for i in range(com):
        if root[i] == id2: 
            root[i] = id1


com = int(input())
edge = int(input())
root = [i for i in range(com)]
for i in range(edge):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

cnt = Counter(root)
print(cnt[0] - 1)
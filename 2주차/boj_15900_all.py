import sys
input = sys.stdin.readline


n = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
q = [[1, 0]]
leaf = []
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

while q:
    a, b = q.pop()
    visit[a] = 1
    
    if a != 1 and len(graph[a]) == 1:
        leaf.append(b)
        continue

    for nei in graph[a]:
        if visit[nei] == 0:
            q.append([nei, b + 1])


if sum(leaf) % 2 == 0:
    print('No')
else:
    print('Yes')
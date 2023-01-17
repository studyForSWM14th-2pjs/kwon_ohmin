import sys
sys.setrecursionlimit(10**5)


def dfs(n):
    visit[n] = 1
    for next_n in graph[n]:
        if visit[next_n] == 0:
            dist[next_n] = dist[n] + 1
            dfs(next_n)    


n = int(input())
Sum = 0
graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for g, d in zip(graph, dist):
    if len(g) == 1:
        Sum += d

if Sum % 2 == 0:
    print('No')
else:
    print('Yes')
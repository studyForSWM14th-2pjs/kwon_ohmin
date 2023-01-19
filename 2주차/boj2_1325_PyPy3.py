import sys
from collections import deque
input = sys.stdin.readline


def bfs(a):
    queue = deque([a])
    cnt = 1
    visit = [0 for _ in range(n + 1)]
    visit[a] = 1

    while queue:
        node = queue.popleft()
        
        for nei in arr[node]:
            if visit[nei] == 0:
                cnt += 1
                visit[nei] = 1
                queue.append(nei)

    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
max_cnt = 0
answer = []

for i in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

for i in range(1, n + 1):
    count = bfs(i)
    if max_cnt < count:
        max_cnt = count
        answer.clear()
        answer.append(i)
    elif max_cnt == count:
        answer.append(i)

print(*answer)
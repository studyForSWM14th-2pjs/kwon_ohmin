from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, 0))

    visit = [0 for _ in range(n + 1)]
    visit[x] = 1

    while queue:
        cur, cur_d = queue.popleft()
        if cur == y:
            return cur_d

        for nei, dist in arr[cur]:
            if visit[nei] == 0:
                visit[nei] = 1
                queue.append((nei, cur_d + dist))


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
answer = []

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    answer.append(bfs(a, b))

for ans in answer:
    print(ans)

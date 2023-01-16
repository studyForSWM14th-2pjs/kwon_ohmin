from collections import deque

def bfs(n):
    q = deque([n])
    visit[n] = 1
    while q:
        tmp = q.popleft()
        if tmp == g:
            return count[g]
        
        for next_n in (tmp + u, tmp - d):
            if 1 <= next_n <= f and visit[next_n] == 0:
                visit[next_n] = 1
                count[next_n] = count[tmp] + 1
                q.append(next_n)

    if count[g] == 0:
        return 'use the stairs'
        

f, s, g, u, d = map(int, input().split())
visit = [0 for _ in range(f + 1)]
count = [0 for _ in range(f + 1)]

print(bfs(s))
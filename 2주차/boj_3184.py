from collections import deque


def bfs(a, b):
    global o, v
    queue = deque()
    queue.append([a, b])
    cnt_o, cnt_v = 0, 0
    if arr[a][b] == 'o':
        cnt_o += 1
    if arr[a][b] == 'v':
        cnt_v += 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            aa = a + dx[i]
            bb = b + dy[i]

            if 0 <= aa < r and 0 <= bb < c and visit[aa][bb] == 0 and arr[aa][bb] != '#':
                if arr[aa][bb] == 'o':
                    cnt_o += 1
                if arr[aa][bb] == 'v':
                    cnt_v += 1
                
                visit[aa][bb] = 1
                queue.append([aa, bb])
    if cnt_o > cnt_v:
        v -= cnt_v
    else:
        o -= cnt_o

        
r, c = map(int, input().split())

arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0 for _ in range(c)] for _ in range(r)]
o, v = 0, 0
for i in range(r):
    tmp = list(input().strip())
    for t in tmp:
        if t == 'o':
            o += 1
        if t == 'v':
            v += 1
    arr.append(tmp)
for i in range(r):
    for j in range(c):
        if (arr[i][j] == 'o' or arr[i][j] == 'v') and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j)

print(o, v)

def bfs(x, y):
    queue = set([(x, y, arr[x][y])])
    global cnt    
    while queue:
        a, b, tmp = queue.pop()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in tmp:
                queue.add((nx, ny, tmp + arr[nx][ny]))
                cnt = max(cnt, len(tmp) + 1)


r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

bfs(0, 0)
print(cnt)
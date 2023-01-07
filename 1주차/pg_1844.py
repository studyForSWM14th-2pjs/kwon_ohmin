from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visit[0][0] = 1
    
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] == 1:
                if visit[x][y] == 0:
                    queue.append([x, y])
                    visit[x][y] = visit[a][b] + 1
                
    if visit[-1][-1] == 0:
        return -1
    return visit[-1][-1]
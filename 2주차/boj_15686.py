from itertools import combinations

n, m = map(int, input().split())
arr = []
answer = 99999
for i in range(n):
    arr.append(list(map(int, input().split())))

# 치킨집과 가정집의 좌표를 저장
c, h = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            h.append([i, j])
        elif arr[i][j] == 2:
            c.append([i, j])

# m개의 치킨집 선정
for a in combinations(c, m):
    tmp = 0
    # 집의 좌표를 하나씩 가져와
    for h_x, h_y in h:
        dist = 99999
        # 선정된 치킨집과의 최소 거리를 구한다.
        for c_x, c_y in a:
            dist = min(dist, abs(h_x - c_x) + abs(h_y - c_y))
        tmp += dist
    answer = min(answer, tmp)

print(answer)
from collections import deque

n = int(input())

if n == 1:
    print(0)
    print(1)
    exit()

arr = [-1 for _ in range(n + 1)]
answer = []
que = deque()
que.append(n)

while que:
    tmp = que.popleft()
    if tmp == 1:
        break
    
    if arr[tmp - 1] < 0:
        arr[tmp - 1] = tmp
        que.append(tmp - 1)
    if tmp % 2 == 0 and arr[tmp // 2] < 0:
        arr[tmp // 2] = tmp
        que.append(tmp // 2)
    if tmp % 3 == 0 and arr[tmp // 3] < 0:
        arr[tmp // 3] = tmp
        que.append(tmp // 3)

tmp = 1
while True:
    answer.append(tmp)
    tmp = arr[tmp]
    if tmp == n:
        answer.append(tmp)
        break

answer.sort(reverse=True)
print(len(answer) - 1)
print(*answer)
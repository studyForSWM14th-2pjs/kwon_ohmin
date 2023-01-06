t = int(input())
answer = []

for i in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    target = [0 for _ in range(n)]
    target[m] = 1

    order = 0
    while True:
        if queue[0] == max(queue):
            order += 1
            if target[0] == 1:
                answer.append(order)
                break
            else:
                queue.pop(0)
                target.pop(0)
        
        else:
            queue.append(queue.pop(0))
            target.append(target.pop(0))

for ans in answer:
    print(ans)
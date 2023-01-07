from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 1])
    queue.append([-numbers[0], 1])
    
    while queue:
        num, cnt = queue.popleft()
        if cnt != len(numbers):
            queue.append([num + numbers[cnt], cnt + 1])
            queue.append([num - numbers[cnt], cnt + 1])
        else:
            if num == target:
                answer += 1
    
    return answer
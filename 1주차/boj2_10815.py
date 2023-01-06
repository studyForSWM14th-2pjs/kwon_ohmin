def check(card, start, end):
    while start <= end:
        mid = (start + end) // 2

        if sang[mid] == card:
            return mid
        elif sang[mid] > card:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

n = int(input())
sang = list(map(int, input().split()))
sang.sort()

m = int(input())
arr = list(map(int, input().split()))

answer = []
for a in arr:
    if check(a, 0, n - 1) != -1:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
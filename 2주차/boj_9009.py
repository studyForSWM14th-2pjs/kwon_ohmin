t = int(input())

fibo = [0, 1]
result = []
# n은 10억 이하의 수
# -> fibo[45]가 약 11억이라 미리 만들어 놓음
for i in range(2, 46):
    fibo.append(fibo[i - 1] + fibo[i - 2])

for _ in range(t):
    n = int(input())
    answer = []
    for i in range(len(fibo) - 1, 0, -1):
        if fibo[i] > n:
            continue
        n -= fibo[i]
        answer.append(fibo[i])
    answer.sort()
    result.append(answer)

for re in result:
    print(*re)
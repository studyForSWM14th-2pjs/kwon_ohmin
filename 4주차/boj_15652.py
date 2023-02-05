def solve(a):
    if a == m:
        print(*answer)
        return
    for i in range(n):
        if len(answer) == 0 or answer[-1] <= i + 1:
            answer.append(i + 1)
            solve(a + 1)
            answer.pop()


n, m = map(int, input().split())
answer = []
solve(0)
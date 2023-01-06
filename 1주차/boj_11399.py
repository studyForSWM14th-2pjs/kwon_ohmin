n = int(input())
arr = list(map(int, input().split()))
arr.sort()

s = 0
for i in range(n):
    s += sum(arr[:i + 1])

print(s)
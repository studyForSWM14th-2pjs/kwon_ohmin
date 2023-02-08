import sys
input = sys.stdin.readline


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        print(sum(arr[i:i+3]))
        exit(0)

print(-1)
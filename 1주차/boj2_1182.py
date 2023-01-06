def dfs(idx, Sum):
    global cnt
    if idx >= n:
        return
    Sum += arr[idx]
    if Sum == s:
        cnt += 1

    dfs(idx + 1, Sum - arr[idx])
    dfs(idx + 1, Sum)
    
    return cnt


cnt = 0
n, s = map(int, input().split())
arr = list(map(int, input().split()))

print(dfs(0, 0))
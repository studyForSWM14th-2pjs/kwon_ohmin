def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


v, e = map(int, input().split())
root = [i for i in range(v + 1)]
arr = []
answer = 0

for _ in range(e):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[2])

for a, b, c in arr:
    ar = find(a)
    br = find(b)

    if ar != br:
        if ar > br:
            root[ar] = br
        else:
            root[br] = ar
        
        answer += c

print(answer)
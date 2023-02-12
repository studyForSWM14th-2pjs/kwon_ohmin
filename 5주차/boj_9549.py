n = int(input())
answer = []

for _ in range(n):
    a = input()
    b = input()
    if len(a) == len(b):
        sort_a = sorted(a)
        sort_b = sorted(b)
        if sort_a == sort_b:
            answer.append('YES')
        else:
            answer.append('NO')
    else:
        check = 0
        sort_b = sorted(b)
        for i in range(0, len(a) - len(b) + 1):
            sort_a = sorted(a[i : i + len(b)])
            if sort_a == sort_b:
                answer.append('YES')
                check = 1
                break
        if check == 0:
            answer.append('NO')

for ans in answer:
    print(ans)
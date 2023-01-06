t = int(input())
answer = []

dp_z = [0 for _ in range(41)]
dp_o = [0 for _ in range(41)]
dp_z[0] = 1
dp_o[1] = 1

for i in range(2, 41):
    dp_z[i] = dp_z[i - 1] + dp_z[i - 2]
    dp_o[i] = dp_o[i - 1] + dp_o[i - 2]

for i in range(t):
    n = int(input())
    answer.append([dp_z[n], dp_o[n]])

for ans in answer:
    print(*ans)
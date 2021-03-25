n = int(input())
data = []

for _ in range(n):
    # [a, b] = input().split()
    # data.append([a, b])
    data.append(list(input().split()))

data.sort(key=lambda x:x[0])

for i in range(n):
    print(data[i][0],data[i][1])

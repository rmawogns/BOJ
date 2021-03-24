n = int(input())
num = []

for i in range(n):
    [x, y] = map(int, input().split())
    rev = [y, x]
    num.append(rev)

num.sort()

for i in range(n):
    print(num[i][1], num[i][0])

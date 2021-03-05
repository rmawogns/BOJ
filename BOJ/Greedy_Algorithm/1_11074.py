n, k = map(int, input().split())
cnt = 0
result = 0
coin = []
for i in range(n):
    data = int(input())
    coin.append(data)

while k != 0:
    if k >= coin[n-1]:
        cnt = k // coin[n-1]
        k -= cnt * coin[n-1]
        result += cnt
    else:
        n -= 1

print(result)
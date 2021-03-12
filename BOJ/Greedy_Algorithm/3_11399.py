n = int(input())
pi = list(map(int, input().split()))
pi.sort()
sum = 0
result = 0
for i in pi:
    sum += i
    result += sum

print(result)
n = int(input())
result = 1

if n > 0:
    while n!=1:
        result *= n
        n -= 1

print(result)
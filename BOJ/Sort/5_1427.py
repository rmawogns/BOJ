n = int(input())
result = list(map(int, str(n)))
result.sort(reverse=True)

for i in result:
    print(i, end = "")

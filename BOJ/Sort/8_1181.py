n = int(input())
data = []

for i in range(n):
    a = input()
    data.append(a)

data_s = sorted(set(data))
result = sorted(data_s, key=len)

for i in result:
    print(i)
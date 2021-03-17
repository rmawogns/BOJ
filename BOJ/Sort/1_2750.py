n = int(input())
num = []
for i in range(n):
    i = int(input())
    num.append(i)

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for i in num:
    print(i)
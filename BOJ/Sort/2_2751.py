n = int(input())
num = []
k = 0
min = 999
for i in range(n):
    i = int(input())
    num.append(i)

print(num)
for i in range(len(num) - 1):
    for j in range(len(num) - 1):        
        if num[i] < num[j]:
            k = num[i]
            num[i] = num[j]
            num[j] = k

# for i in num:
#     print(i)

print(num)
            
l = []
for i in range(9):
    i = int(input())
    l.append(i)

max_num = max(l)
print(max_num)
print(l.index(max_num) + 1)
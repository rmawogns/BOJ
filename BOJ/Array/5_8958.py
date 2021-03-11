n = int(input())
score = []
for i in range(n):
    i = input()
    sum = 0
    cnt = 0
    for j in i:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    score.append(sum)

for i in score:
    print(i)

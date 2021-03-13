n = int(input())
score = list(map(int, input().split()))
m = max(score)
sum = 0

for i in score:
    new_score = i / m * 100
    sum += new_score

print(sum / n)


c = int(input())
result = []

def avg(data):
    score = 0
    for i in range(len(data) - 1):
        score += data[i + 1]
    avg_score = score / data[0]
    return avg_score

def good(data, avg_score):
    cnt = 0
    for i in range(len(data) - 1):
        if data[i + 1] > avg_score:
            cnt += 1
    result = cnt / data[0] * 100
    return round(result, 3)

for data in range(c):
    data = list(map(int, input().split()))
    avg_score = avg(data)
    result.append(good(data, avg_score))

for i in result:
    print(format(i, ".3f")+'%')
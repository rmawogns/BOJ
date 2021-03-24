from collections import Counter
n = int(input())
data = []

for i in range(n):
    num = int(input())
    data.append(num)

data.sort()
data_counter = Counter(data).most_common()

print(round(sum(data) / n))     # 산술평균
print(data[n // 2])             # 중앙값

if len(data_counter) > 1:
    if data_counter[0][1] == data_counter[1][1]:
        print(data_counter[1][0])
    else:
        print(data_counter[0][0])
else:
    print(data_counter[0][0])   # 최빈값

print(data[-1] - data[0])       # 범위

A = int(input())
B = int(input())
C = int(input())
i = 0
num = [int(i) for i in str(A * B * C)]

for i in range(10):
    print(num.count(i))
    i += 1
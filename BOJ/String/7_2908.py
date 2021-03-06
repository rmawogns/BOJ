A, B = map(int, input().split())

Num1 = int(str(A)[::-1])
Num2 = int(str(B)[::-1])

if Num1 > Num2:
    print(Num1)
else:
    print(Num2)

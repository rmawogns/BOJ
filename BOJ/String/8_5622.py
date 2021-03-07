s = input()
time = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in s:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3

print(time)



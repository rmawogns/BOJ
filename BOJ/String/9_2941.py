s = input()
# cnt = 0
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    if i in s:
        # cnt += s.count(i)
        s = s.replace(i, 'x')
        
# cnt += len(s)
print(len(s))

t = int(input())

for _ in range(t):
  r, s = input().split()
  result = ''
  for i in s:
    result += int(r) * i
  print(result)
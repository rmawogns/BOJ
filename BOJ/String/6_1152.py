s = input()
blank_space = s.count(" ")

if s[0] == " " and s[-1] == " ":
  blank_space -= 2
elif s[0] == " " or s[-1] == " ":
  blank_space -= 1

print(blank_space + 1)
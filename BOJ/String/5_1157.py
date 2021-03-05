words = input().upper()
words2 = list(set(words))
max_list = []

for i in words2:
  cnt = words.count(i)
  max_list.append(cnt)

if max_list.count(max(max_list)) > 1:
  print("?")
else:
  max_index = max_list.index(max(max_list))
  print(words2[max_index])
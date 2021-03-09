n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    group = True
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]
            if new_word.count(word[i]) > 0:
                group = False
    
    if group == True:
        cnt += 1

print(cnt)

        

check = "abcdefghijklmnopqrstuvwxyz"
temp = []
word = []

S = str(input())

for i in S:
    word.append(i)

for i in check:
    for j in range(len(word)):
        if i == word[j]:
            temp.append(j)
            break
        elif j < len(word) - 1:
            continue
        else:
            temp.append(-1)
for i in temp:
    print(i, end=" ")
N = int(input())
temp = []

for i in range(N):
    sen = input()
    num = 0
    check = 1
    for j in range(sen.__len__()):
        if sen[j] == 'O':
            num += check
            check += 1
        else:
            check = 1
    temp.append(num)

for i in temp:
    print(i)
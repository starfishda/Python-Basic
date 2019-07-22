word = input().upper()
temp = [i for i in range(0,26)] #알파벳 길이 만큼의 리스트

#count가 중요한 부분
for i in range(0,26):
    temp[i] = word.count(chr(i+65))

num = max(temp)

if temp.count(num) >= 2:
    print("?")
else:
    print(chr(temp.index(num) + 65))

'''
#결과값을 제대로 나옴 / 실행시간 문제 발생...
temp = []

for i in range(len(word)):
    if len(temp) > 0:
        flag = 0
        for j in range(len(temp)):
            if word[i] == temp[j][1]:
                temp[j] = (temp[j][0] + 1, word[i])
                flag = 1
        if flag == 0:
            temp.append((1, word[i]))
    else:
        temp.append((1,word[i]))

temp.sort()
if temp[-1][0] == temp[-2][0]:
    print("?")
else:
    print(temp[-1][1])
'''
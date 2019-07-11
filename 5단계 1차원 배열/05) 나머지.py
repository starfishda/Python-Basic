temp = []
answer = 0

for i in range(10):
    N = int(input())
    temp.append(int(N % 42))

temp = sorted(temp)

for i in range(temp.__len__()):
    if temp[i] != temp[i-1]:
        answer += 1

print(answer)
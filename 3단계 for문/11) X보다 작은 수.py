N, X = map(int, input().split())

temp = []
temp = input().split()

answer = ""

for i in range(N):
    if int(temp[i]) < X:
        answer += temp[i] + " "

answer = answer[:-1]
print(answer)
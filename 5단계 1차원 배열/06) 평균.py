N = int(input())
temp = list(map(int, input().split()))

max_score = max(temp)
num = 0

for i in range(temp.__len__()):
    temp[i] = temp[i] / max_score * 100
    num += temp[i]

print(num / N)
temp = list(map(int, input().split()))
answer = ''

for i in range(temp.__len__()):
    if i != 0 and temp[i] == temp[i-1] + 1:
        answer = 'ascending'
    elif i != 0 and temp[i] == temp[i-1] - 1:
        answer = 'descending'
    elif i != 0:
        answer = 'mixed'
        break

print(answer)

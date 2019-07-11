N = int(input())
answer = []

for i in range(N):
    temp = list(map(int,input().split()))
    avg = (sum(temp) - temp[0]) / (len(temp) - 1)
    num = 0
    for j in range(len(temp) - 1):
        if temp[j+1] > avg:
            num += 1
    answer.append(num/temp[0] * 100)

for i in answer:
    print("%0.3f"%i,end='')
    print('%')
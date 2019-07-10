A = int(input())
B = int(input())
C = int(input())

num = A * B * C
temp = [0,0,0,0,0,0,0,0,0,0]

while num != 0:
    val = num % 10
    temp[val] += 1
    num = num - val
    num = int(num / 10)

for i in temp:
    print(i)
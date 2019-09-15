x = int(input())
i = 0

while x > 0:
    x -= i
    i += 1

x = i + x -1
temp = str(x) + '/' + str(i - x)

if i % 2 == 0:
    temp = str(i - x) + '/' + str(x)

print(temp)
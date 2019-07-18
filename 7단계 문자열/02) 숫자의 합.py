N = int(input())
num = int(input())
sum = 0

for i in range(N, 0, -1):
    sum += int(num / (10**i))
    num = int(num % (10 ** i))

sum += num
print(sum)
N = int(input())

a = int(N / 10)
b = int(N % 10)

cycle = 1
c = b
d = a + b

while c != a or d != b:

    temp = c
    c = d
    d = int((temp + d) % 10)
    cycle += 1

print(cycle)
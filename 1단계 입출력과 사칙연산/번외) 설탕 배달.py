a = int(input())

b = 0 #5
c = 0 #3

if a % 5 == 0:
    b += int(a/5)
else:
    for i in range(1, int(a/3) + 1):
        if (a - (i * 3)) % 5 == 0:
            c += int(i)
            b += int((a - (i * 3)) / 5)
            break

if b != 0 or c != 0:
    print(b + c)
else:
    print(int(-1))
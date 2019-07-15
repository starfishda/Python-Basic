N = int(input())
temp = []

def hanoi(num, a, b, c, temp):
    if num == 1:
        temp.append([a,c])
        return None
    hanoi(num - 1, a, c, b, temp)
    temp.append([a,c])
    hanoi(num - 1, b, a, c, temp)

hanoi(N, 1, 2, 3, temp)

print(len(temp))
for a, b in temp:
    print('{} {}'.format(a, b))
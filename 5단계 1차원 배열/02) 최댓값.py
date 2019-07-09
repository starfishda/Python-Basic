max = 0
max_posi = 0

for i in range(9):
    N = int(input())
    if N > max:
        max = N
        max_posi = i + 1

print(max)
print(max_posi)
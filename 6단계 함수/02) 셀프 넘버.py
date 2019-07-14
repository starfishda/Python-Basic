number = set(range(1, 10001))
answer= set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    answer.add(i)

temp = number - answer

for i in sorted(temp):
    print(i)
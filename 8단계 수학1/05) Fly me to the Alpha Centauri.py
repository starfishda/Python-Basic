T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    num = y - x
    check = 0
    while num > 0:
        check += 1
        num = num - 2 * check
    num = num * -1
    num2 = 0
    if num >= check:
        num2 = 1
    print(check * 2 - num2)
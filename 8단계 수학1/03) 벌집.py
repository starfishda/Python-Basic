n = int(input())
temp = 1
add = 6
answer = 1

if n == 1:
    print(answer)
else:
    while True:
        temp += add
        answer += 1
        if n <= temp:
            print(answer)
            break
        add += 6
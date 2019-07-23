S = input()
num = S.count(" ") + 1

if S[0] == " ":
    num -= 1
if S[-1] == " ":
    num -= 1

print(num)
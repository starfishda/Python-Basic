num = input()
alpha = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
time = 0

for i in range(len(num)):
    for j in range(len(alpha)):
        for k in range(len(alpha[j])):
            if alpha[j][k] == num[i]:
                time += j + 3

print(time)
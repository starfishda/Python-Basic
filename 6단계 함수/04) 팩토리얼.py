'''def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)
'''

N = int(input())
#num = fac(N) 팩토리얼 코드
num = 1
for i in range(N,0,-1):
    num *= i
print(num)
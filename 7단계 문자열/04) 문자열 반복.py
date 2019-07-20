T = int(input())

for i in range(T):
    R, P = input().split( )
    R = int(R)
    for j in range(len(P)):
        for k in range(R):
            print(P[j],end="")
    print()
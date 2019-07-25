word = input()
temp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in range(len(temp)):
    word = word.replace(temp[i],str(i))

print(len(word))
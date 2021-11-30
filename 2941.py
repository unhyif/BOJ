I = input()
for k in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    I = I.replace(k, "*")
print(len(I)) # 입력된 단어의 알파벳 개수
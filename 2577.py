A = int(input())
B = int(input())
C = int(input())
for i in range(10):
    print(str(A*B*C).count(str(i)))  # "A*B*C" 안에 포함된 "0"~"9"의 갯수

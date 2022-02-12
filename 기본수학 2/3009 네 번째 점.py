X = [] # x좌표 리스트
Y = [] # y좌표 리스트
for _ in range(3):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
# X에 하나만 존재하고 있는 x좌표와 Y에 하나만 존재하고 있는 y좌표
print(*(x for x in X if X.count(x) == 1), *(y for y in Y if Y.count(y) == 1)) 
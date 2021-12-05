line = 0 # n이 속한 i번째 라인
cnt = 0 # 1 ~ i번째 라인에 속해 있는 분수의 총 개수
n = int(input())
for i in range(1, 10000):
    cnt += i
    if cnt - i < n <= cnt:
        line = i
        break
if line % 2 == 1:
    print(f"{cnt-n+1}/{line-(cnt-n)}")
else:
    print(f"{line-(cnt-n)}/{cnt-n+1}")
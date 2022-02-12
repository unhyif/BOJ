done = 0
N = int(input())
for i in range(N//5, -1, -1): # 총 봉지 개수를 최소화 하기 위해서는 먼저 5kg 봉지 개수를 최대화 해야 함
    if (N - 5*i) % 3 == 0: # 5kg 봉지 또는 3kg 봉지로 N kg을 구성할 수 있을 때
        print(i + (N - 5*i)//3) # 5kg 봉지 수 + 3kg 봉지 수
        done += 1 # 봉지 구성 결정됨
        break
if done == 0: # N kg이 5kg 봉지 또는 3kg 봉지로 구성될 수 없을 때
    print(-1)
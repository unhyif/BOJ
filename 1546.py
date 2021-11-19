n = int(input())  # 과목 수
g = list(map(int, input().split()))  # 점수 리스트
print(sum(g)/max(g)*100/n)

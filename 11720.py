N = int(input()) # 숫자의 개수
numbers = input()
c = 0
for n in range(N): c += int(numbers[n]) # 모든 숫자들의 합 구하기
print(c)
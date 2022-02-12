i = 1 # n이 속한 띠가 몇 번째 띠인지
n = int(input())
if n == 1:
    print(i) 
for k in range(100000):
    i += 1
    if 2+3*k*(k+1) <= n < 2+3*(k+1)*(k+2): # n이 속한 띠에 접근했을 때
        print(i)
        break
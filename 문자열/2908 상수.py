q = list(map(lambda x: int(x[::-1]), input().split())) # 입력된 두 수를 거꾸로 뒤집어 정수화 시킨 후, 리스트화 함
print(max(q)) # 둘 중 큰 수 선택
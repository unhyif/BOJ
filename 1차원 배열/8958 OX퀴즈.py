for i in range(int(input())):
    res = input().split("X") # 입력된 문자열을 X를 기준으로 나눈 리스트 생성
    res = [len(r) for r in res] # 리스트의 각 요소를 요소의 길이(O의 갯수)로 변환
    res = [r*(r+1)/2 for r in res] # 각 요소를 등차수열의 합(r+r+1+r+2...)으로 변환
    print(int(sum(res)))
while True:
    nums = sorted(map(int, input().split())) # 오름차순으로 변의 길이 정렬
    if 0 in nums: break
    if nums[2]**2 == nums[0]**2 + nums[1]**2: # 피타고라스 정리가 성립할 때
        print("right")
    else:
        print("wrong")
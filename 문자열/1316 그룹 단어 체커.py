l = []
for i in range(int(input())):
    l.append(input()) # 입력받은 단어들의 리스트
for k in range(len(l)):
    for s in set(l[k]): # 한 단어를 이루는 각 알파벳들에 대해
        n = l[k].count(s) # 한 단어에 포함된 해당 알파벳의 수
        if s*n not in l[k]: # 그 수만큼 연속된 해당 알파벳 문자열이 해당 단어에 존재하지 않으면 (그룹 단어 X)
            l[k] = "*" # 해당 단어를 *로 변경
            break # 다음 단어로 넘어감
for r in range(l.count("*")):
    l.remove("*") # 리스트에서 * 삭제
print(len(l)) # 그룹 단어들의 수
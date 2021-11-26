for i in range(int(input())):
    R,S = input().split()
    l = [s*int(R) for s in S]
    print("".join(l))
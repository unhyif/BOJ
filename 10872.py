def f(N):
    if N == 0 or N == 1:
        return 1
    return N * f(N-1)
print(f(int(input())))
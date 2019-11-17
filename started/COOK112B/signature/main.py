print("#############")
T = int(input())
print(T)

for i in range(T):
    N, M = map(int, input().split())
    print(N, M)
    A = []
    B = []

    for i in range(N):
        A.append(input())

    for i in range(N):
        B.append(input())

    print(A)
    print(B)
    print("#############")
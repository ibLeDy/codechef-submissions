T = int(input())

for i in range(T):
    N, Z = map(int, input().split())
    A = [int(j) for j in input().split()]
    A.sort()
    print(A)

    if A[0] * 2 < A[1]:
        print(A[0] * 2)
    else:
        print(A[1])

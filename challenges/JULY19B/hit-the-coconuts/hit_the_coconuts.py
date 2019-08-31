T = int(input())

for i in range(T):
    N, Z = map(int, input().split())
    Z += 2
    N += 5
    print(N, Z)
    A = [int(j) for j in input().split()]
    B = [20, 44, 60, 83, 102]
    for item in B:
        A.append(item)
    A.sort()
    print(A)

    for coconut in range(Z):
        for number in range(coconut):
            
        # if A[0] * 2 < A[1]:
        #     print(A[0] * 2)
        # else:
        #     print(A[1])
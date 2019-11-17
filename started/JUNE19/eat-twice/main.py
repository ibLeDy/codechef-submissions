T = int(input())

for i in range(T):
    N, M = input().split(" ")
    dishes = []
    tastiness = []
    test_dict = {}

    for i in range(int(N)):
        D, V = input().split()
        dishes.append(int(D))
        tastiness.append(int(V))
        test_dict[int(D)] = int(V)
    # print(dishes, tastiness)


    temp_tastiness = tastiness.copy()
    temp_tastiness.sort(reverse=True)
    max_tastiness = max(temp_tastiness)
    temp_index_max = temp_tastiness.index(max_tastiness)
    temp_tastiness.remove(max_tastiness)
    second_tastiness = max(temp_tastiness)

    total = max_tastiness + second_tastiness
    print(total)

t = int(input())
print(t)

for i in range(t):
    whitespace = input()
    string = input()
    n = len(string)

    initial_array = []
    for i in range(1, n + 2):
        initial_array.append(i)

    print(string)
    print(n)
    print(initial_array)

print("#############")

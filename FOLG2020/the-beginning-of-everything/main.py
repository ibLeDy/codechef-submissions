T = int(input())
result_test = [i for i in 'helloworld']

for i in range(T):
    s = [i for i in input()]
    print('Yes' if all(char in result_test for char in s) else 'No')

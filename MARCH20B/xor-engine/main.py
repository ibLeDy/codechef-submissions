from sys import stdin, stdout

T = int(stdin.readline())
for _ in range(T):
    N, Q = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    for _ in range(Q):
        P = int(stdin.readline())
        test = [True if '{0:b}'.format(num).count('1') % 2 == 0 else False for num in A]
        stdout.write(f'{test.count(True)} {test.count(False)}')

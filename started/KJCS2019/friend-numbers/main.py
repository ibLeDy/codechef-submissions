import cProfile

def mine():
    T = int(input())
     
    for case in range(T):
        N = int(input())
        S = input().split(' ')

        result = [i for i in S if S.count(i) == 1]
        print(result[0] if result else str(-1))

def correct():
    test = int(input())
    for i in range(test):
        n = int(input())
        a = input().split(' ')
        if(n%2==0):
            print(-1)
        else:
            a = [int(i) for i in a]
            a = sorted(a)
            for i in range(0,len(a),2):
                try:
                    if(a[i]!=a[i+1]):
                        print(a[i])
                        break
                except:
                    print(a[i])

cProfile.run('mine()')
cProfile.run('correct()')

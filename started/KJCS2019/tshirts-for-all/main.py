from collections import *
import profile

def elegant():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        s = list(map(int, input().split()))

        x = []

        for __ in range(q):
            x.append(int(input()))

        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1

        l = [0]

        for i in sorted(d.values(), reverse=True):
            l.append(i + l[-1])

        for k in x:
            print(l[min(k, len(l) - 1)])

def correct():
    t=int(input())
    for _ in range(t):
        n,q=map(int,input().split())
        s=list(map(int,input().split()))
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        l=list(d.values())
        l.sort(reverse=True)
        pref=[0]*(len(l))
        pref[0]=l[0]
        for i in range(1,len(l)):
            pref[i]=pref[i-1]+l[i]
        for i in range(q):
            k=int(input())
            if k==1:
                print(pref[0])
            else:
                if k>=len(pref):
                    print(pref[len(pref)-1])
                else:
                    print(pref[k-1])

profile.run('elegant()')
profile.run('correct()')
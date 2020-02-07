ar1 = input().split()
ar2 = input().split()
ar3 = input().split()
print('Common Elements are ' + ' '.join(set(ar1).intersection(ar2, ar3)))

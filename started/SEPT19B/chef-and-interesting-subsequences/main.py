# cook your dish here
def sum_it(minimum_sum, x, y):
    return True if x + y == minimum_sum else False

def get_subsequences(sequence):
    subsequences = []
    for seq in range(len(sequence)):
        for sub in range(seq, len(sequence)):
            try:
                subsequences.append((sequence[seq], sequence[sub + 1]))
            except:
                continue

    return subsequences

def get_result(subsequences, minimum_sum):
    result  = []
    for subseq in subsequences:
        if sum_it(minimum_sum, subseq[0], subseq[1]) == True:
            result.append(subseq)

    print(len(result))


t = int(input())

for i in range(t):
    n, k = map(int, input().split(" "))
    sequence = [int(j) for j in input().split(" ")]
    
    subsequences = get_subsequences(sequence)
    minimum_sum = sum(min(subsequences))
    get_result(subsequences, minimum_sum)

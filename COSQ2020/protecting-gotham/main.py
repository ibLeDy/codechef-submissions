from collections import deque, Counter


def is_substring(string_counter):
    check = [True if string_counter[l] >= letters[l] else False for l in letters]
    if all(check):
        return True
    return False


def remove_characters(string, count):
    string[indices.popleft() - 1] = ''
    if not is_substring(Counter(string)):
        return count
    else:
        return remove_characters(string, count + 1)


A = [i for i in input()]
B = [i for i in input()]
letters = Counter(B)
indices = deque(int(i) for i in input().split())
print(remove_characters(A, 0))

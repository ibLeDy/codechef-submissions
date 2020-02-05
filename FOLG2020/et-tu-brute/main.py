def decipher(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    rot = len(s)
    result = ''

    for char in s:
        prev = letters.index(char)
        new_pos = prev + rot
        result += letters[new_pos]

    return result


T = int(input())

for _ in range(T):
    s = input()
    result = decipher(s)

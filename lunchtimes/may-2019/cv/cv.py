T = int(input())

string = []
for i in range(T):
    N = input()
    S = input()
    string.append(S)

vowels = ["a", "e", "i", "o", "u"]

result = ""
count = {}
for s in string:
    count[s] = 0
    num = 0
    for ch in s:
        num += 1
        if ch in vowels:
            try:
                if s[num - 2] not in vowels:
                    count[s] += 1
                else:
                    pass
            except Exception as e:
                print("Error ", e)

for k, v in count.items():
    print(int(v))

# for s in string:
#     if s.isalpha():
#         print(int(count[s]))


# from sys import stdin

# for line in stdin:
#   print(line)


# from sys import stdin

# lines = []
# for line in stdin:
#     lines.append(line.lower())
#     # print(line)


# while True:
#     try:
#         T = int(input())
#         for i in range(T):
#             S = input()
#             string.append(S.lower())
#     except EOFError:
#         print("EOF")
#         break
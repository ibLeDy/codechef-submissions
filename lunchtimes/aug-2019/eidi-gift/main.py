# cook your dish here

test_cases = int(input())

for i in range(test_cases):
    a1, a2, a3, c1, c2, c3 = input().split(" ")

    ages = sorted([int(a1), int(a2), int(a3)])

    ages_coins = [
        (ages[ages.index(int(a1))], int(c1)),
        (ages[ages.index(int(a2))], int(c2)),
        (ages[ages.index(int(a3))], int(c3))
    ]
    print(ages_coins)

    result = "NOT FAIR"
    for i in range(len(ages_coins)):
        try:

            if ages_coins[i][1] < ages_coins[i + 1][1]:
                result = "FAIR"
            else:
                result = "NOT FAIR"

            if ages_coins[i][0] == ages_coins[i + 1][0] and ages_coins[i][1] == ages_coins[i + 1][1]:
                result = "FAIR"
            else:
                result = "NOT FAIR"
        except:
            if ages_coins[i][0] == ages_coins[i - 1][0] and ages_coins[i][1] == ages_coins[i - 1][1]:
                result = "FAIR"
            else:
                result = "NOT FAIR"

            if ages_coins[i][1] > ages_coins[i - 1][1]:
                result = "FAIR"
            else:
                result = "NOT FAIR"


    print(result)

print("####################")
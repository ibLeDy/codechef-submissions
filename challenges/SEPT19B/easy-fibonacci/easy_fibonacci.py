def fib(num):
  a,b = 0, 1
  for i in range(0, num):
    yield a
    a, b = b, a + b

test_cases = int(input())

for i in range(test_cases):
    first_n = int(input())

    numbers = [item for item in fib(9)]
    modulo_numbers = [i % 10 for i in numbers if i != 0]
    result = [modulo_numbers[i] for i in range(1, len(modulo_numbers)) if not i%2]
    final_result = [result[i] for i in range(1, len(result)) if i % 2 == 0]

    print(final_result[0])

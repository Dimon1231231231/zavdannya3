def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ввід числа
n = int(input("Введіть натуральне число (або 0): "))

if n < 0:
    print("Факторіал для від'ємних чисел не визначений")
else:
    result = factorial(n)
    print(f"{n}! = {result}")
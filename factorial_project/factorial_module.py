def factorial(n):
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

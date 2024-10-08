def is_prime(func):
    def wrapper(*args, **kwargs):
        # Вызываем оригинальную функцию и получаем результат
        result = func(*args, **kwargs)

        # Проверка, является ли результат простым числом
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result  # Возвращаем результат оригинальной функции

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
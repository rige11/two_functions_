
def end_to_end(n_customers):
    result = dict()  # словарь с группами
    for i in range(int(n_customers)):  # создание цикла + подстраховка, что в функцию передано число
        sum = 0
        num = i
        while (num != 0):  # вычисление суммы цифр числа
            sum = sum + num % 10
            num = num // 10
        result[str(sum)] = result.get(str(sum), 0) + 1  # запись в словарь
    return result  # возвращение значения функции


def start_to_end(n_customers=0, n_first_id=0):
    result = dict()  # словарь с группами
    for i in range(int(n_first_id), int(n_first_id) + int(n_customers)):
        # создание цикла + подстраховка, что в функцию переданы числа
        sum = 0
        num = i
        while (num != 0):  # вычисление суммы цифр числа
            sum = sum + num % 10
            num = num // 10
        result[str(sum)] = result.get(str(sum), 0) + 1  # запись в словарь
    return dict(sorted(result.items(), key=lambda x: int(x[0])))
    # сортировка словаря и возвращение значения функции


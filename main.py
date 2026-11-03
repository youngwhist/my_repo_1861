"""Учебный модуль: пример функции и расчёт среднего значения."""


def example_function():
    """Выводит пример строки."""
    print('Это пример функции')


def average(numbers):
    """Возвращает среднее арифметическое; для пустого списка — 0."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    example_function()
    print(average([4, 5, 3]))

#!/usr/bin/env python3
"""Простой калькулятор с консольным интерфейсом."""

def add(x, y):
    """Сложение двух чисел."""
    return x + y

def subtract(x, y):
    """Вычитание двух чисел."""
    return x - y

def multiply(x, y):
    """Умножение двух чисел."""
    return x * y

def divide(x, y):
    """Деление двух чисел."""
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

def get_number(prompt):
    """Запрос числа у пользователя с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_operation():
    """Запрос операции у пользователя."""
    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide)
    }
    
    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    
    while True:
        choice = input("Введите номер операции (1-4): ").strip()
        if choice in operations:
            return operations[choice]
        else:
            print("Ошибка: выберите операцию от 1 до 4.")

def main():
    """Основная функция калькулятора."""
    print("=== Калькулятор ===")
    
    while True:
        # Получаем первое число
        num1 = get_number("\nВведите первое число: ")
        
        # Получаем операцию
        symbol, operation_func = get_operation()
        
        # Получаем второе число
        num2 = get_number("Введите второе число: ")
        
        # Выполняем вычисление
        try:
            result = operation_func(num1, num2)
            print(f"\nРезультат: {num1} {symbol} {num2} = {result}")
        except ValueError as e:
            print(f"\nОшибка: {e}")
        
        # Спрашиваем о продолжении
        continue_calc = input("\nХотите продолжить? (да/нет): ").strip().lower()
        if continue_calc not in ['да', 'д', 'yes', 'y']:
            print("Спасибо за использование калькулятора!")
            break

if __name__ == "__main__":
    main()

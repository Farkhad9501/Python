# Задача 16: 

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint


def get_count_value_in_list(list_of_values: list, value) -> int:
    
    return list_of_values.count(value)


def get_list_of_values(upper_bound: int, min_value: int = 0, max_value: int = 9) -> list:
    
    return [randint(min_value, max_value) for _ in range(upper_bound)]


def get_user_values(list_length=None, search_value=None) -> tuple:
    
    if list_length is None:
        list_length = input('Введите длину списка:\n>>> ')
    try:
        list_length = int(list_length)
    except ValueError:
        print('Не удалось преобразовать строку к числу. Повторите ввод.')
        return get_user_values()
    except Exception as ex:
        print('Произошла непредвиденная ошибка:', ex)
        return get_user_values()

    if search_value is None:
        search_value = input('Введите искомое значение:\n>>> ')
    try:
        search_value = int(search_value)
    except ValueError:
        print('Не удалось преобразовать строку к числу. Повторите ввод.')
        return get_user_values(list_length=list_length)
    except Exception as ex:
        print('Произошла непредвиденная ошибка:', ex)
        return get_user_values()

    return list_length, search_value


def main() -> None:

    length, desired_value = get_user_values()
    list_with_randint = get_list_of_values(length)
    count = get_count_value_in_list(list_with_randint, desired_value)
    print(f'{list_with_randint}\nЗначение "{desired_value}" встретилось {count} раз.')


if __name__ == '__main__':
    main()
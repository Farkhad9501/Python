# Задача 18:
 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint


def get_value_close_to_desired(list_of_values: list, looking_for: int) -> tuple:
    
    sorted_values = sorted(list_of_values)
    lower = sorted_values[0]
    bigger = sorted_values[-1]

    if looking_for <= lower:
        return lower,
    elif bigger <= looking_for:
        return bigger,

    for index in range(1, len(sorted_values)):

        current = sorted_values[index]

        if current == looking_for:
            return current,
        elif current < looking_for:
            continue

        previous = sorted_values[index - 1]
        if abs(previous - looking_for) < abs(current - looking_for):
            return previous,
        elif abs(previous - looking_for) == abs(current - looking_for):
            return previous, current
        else:
            return current,


def get_list_of_values(upper_bound: int, min_value: int = -10, max_value: int = 10) -> list:
    
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

    length_of_list,  desired_value = get_user_values()
    list_of_randint = get_list_of_values(length_of_list)
    values = get_value_close_to_desired(list_of_randint, desired_value)
    temp_text = 'Наиболее близкое(ие) по величине: '
    print(sorted(list_of_randint), f'\nСамое близкое значение к "{desired_value}" ->',
          f'{temp_text}{values[0]}' if len(values) == 1 else f'{temp_text} {values[0]} и {values[1]}')


if __name__ == '__main__':
    main()

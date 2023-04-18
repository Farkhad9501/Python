# Задача №17.
# Дан список чисел. Определите, 
# сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6

# from random import randint
# values_list = [1, 1, 2, 0, -1, 3, 4, 4]
# without_duplication = set(values_list)
# print(f'В списке:\n{values_list}\nвстречается {len(without_duplication)} разных значений')

# def cyclic_shift(lst, k):
#     l = len(lst)
#     k = k % l
#     if k == 0:
#         return lst
#     lst[k:], lst[:k] = lst[:l-k], lst[l-k:]
#     return lst

# # Пример использования:
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(cyclic_shift(arr, k))  # Output: [4, 5, 1, 2, 3]

# n = int(input('Укажите сдвиг:\n>>> '))
# values = [1, 2, 3, 4, 5]
# length = len(values)
# n = n % length 
# print(values[-n:] + values[:-n])

# Input: any

# [
#         {"V": "S001"},
#         {"V": "S002"},
#         {"VI": "S001"},
#         {"VI": "S005"},
#         {"VII": "S005"},
#         {"V": "S009"},
#         {"VIII": "S007"}
# ]
# Output: any

# {'S005', 'S002', 'S007', 'S001', 'S009'}


# list_of_dicts = [
#                  {"V": "S001"},
#                  {"V": "S002"},
#                  {"VI": "S001"},
#                  {"VI": "S005"},
#                  {"VII": "S005"},
#                  {"V": "S009"},
#                  {"VIII": "S007"}
#                 ]

# values = list(map(lambda el: tuple(el.values())[0], list_of_dicts))
# unique_values = [x for x in values if values.count(x) == 1]

# print('Значения без повторений ->', set(values))
# print('Уникальные значения ->', unique_values)

# def unique_values(dct_lst):
#     unique_set = set()
#     for dct in dct_lst:
#         for val in dct.values():
#             unique_set.add(val.strip())
#     return unique_set

# # Пример использования:
# dct_lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# print(unique_values(dct_lst))  # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# array = [0, -1, 5, 2, 3]
# counter_list = [1 for x in range(1, len(array)) if array[x - 1] < array[x]]
# print(f'В массиве:\n{array} -> {sum(counter_list)} элемента больше предыдущего.')

# def count_greater(lst):
#     count = 0
#     for i in range(1, len(lst)):
#         if lst[i] > lst[i-1]:
#             count += 1
#     return count

# # Пример использования:
# arr = [0, -1, 5, 2, 3]
# print(count_greater(arr))  # Output: 2

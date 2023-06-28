# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов

duplicates_list = [1, 2, 3, 2, 4, 3, 5, 6, 1, 7, 8, 7]

unique_list1 = []
for item in duplicates_list:
    if duplicates_list.count(item) > 1 and item not in unique_list1:
        unique_list1.append(item)
print(unique_list1)

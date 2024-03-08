def binary_search(sequence, start_element, key):
    end_element = len(sequence) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if sequence[middle_element] == key:
            return middle_element
        elif sequence[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1


# Можно было еще элегантно создать sequence = [i for i range(1, 31)],
# но для наглядности перечислил все элементы
sequence = [i for i in range(1, 310000)]
# Число которое мы ищем
find_element = 100000

result = binary_search(sequence=sequence, start_element=0, key=find_element)
print(result)
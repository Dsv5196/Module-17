list1 = input('Введите последовательность чисел, через пробел: ')
list2 = list1.split()
int_list = list(map(int, list2))

number = int(input('Введите целое число: '))
int_list.append(number)

print(int_list)

for i in range(len(int_list)):
    idx_min = i
    for j in range(i, len(int_list)):
        if int_list[j] < int_list[idx_min]:
            idx_min = j
    if i != idx_min:
        int_list[i], int_list[idx_min] = int_list[idx_min], int_list[i]

print(int_list)

def binary_search(int_list, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if int_list[middle] == number:
        return middle
    elif number < int_list[middle]:
        return binary_search(int_list, number, left, middle - 1)
    else:
        return binary_search(int_list, number, middle + 1, right)

value = binary_search(int_list, number, 0, len(int_list))
print('При добавлении целого числа в последовательность, индекс числа в последовательности будет равен: ', value)
print('Индекс числа, меньшего введенного равен: ', value - 1)
print('Индекс числа, равного или больше введенного равен: ', value + 1)

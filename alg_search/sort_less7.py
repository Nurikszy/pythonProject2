
array = [64, 23, 89, 6, 1, 12, 33]


def bubble_sort(array):
    swapped = False
    for num1 in range(len(array) -1, 0, -1):
        for num2 in range(num1):
            if array[num2] > array[num2 + 1]:
                array[num2], array[num2 + 1] = array[num2 + 1], array[num2]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array
print((f'sort:{bubble_sort(array)}'))
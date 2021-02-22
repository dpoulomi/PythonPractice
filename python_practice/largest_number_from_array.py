import random


def quick_sort(input_array, start_index, end_index):

    if start_index < end_index:
        partition_index = partition(input_array, start_index, end_index)
        quick_sort(input_array, start_index, partition_index -1)
        quick_sort(input_array, partition_index + 1, end_index)



def partition(array, start_index, end_index):
    pivot_index = random.randint(start_index, end_index)
    swap_array_element(array, pivot_index, end_index)

    loop_index = 0
    smaller_element_index = -1

    while loop_index < end_index:
        if append_compare(array[loop_index], array[end_index]):
            smaller_element_index = smaller_element_index + 1
            swap_array_element(array, smaller_element_index, loop_index)
        loop_index = loop_index + 1

    swap_array_element(array, smaller_element_index + 1, end_index)

    return smaller_element_index + 1


def compare(element1, element2):
    if element1 < element2:
        return True
    else:
        return False


def append_compare(element1, element2):
    xy = "{}{}".format(element1, element2)
    yx = "{}{}".format(element2, element1)

    if xy > yx:
        return True
    else:
        return False


def swap_array_element(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def find_largest_number(input_array):
    pass


def print_appending_array(array):
    result = ''
    for element in array:
        result = "{}{}".format(result, element)

    print(result)


if __name__ == '__main__':
    input_array = [ 4, 3, 2, 1, 5 ]
    quick_sort(input_array, 0, len(input_array) - 1)
    print_appending_array(input_array)



def insertion_sort(input_list: list):
    instance = input_list.copy()

    current = 1
    while current < len(instance):
        print(F'Pre-processing {instance}')
        key = instance[current]
        i = current
        while key < instance[i - 1] and i >= 0:
            instance[i] = instance[i - 1]
            instance[i - 1] = key
            i -= 1

        current += 1
        print(F'Sorting value: {key}, output: {instance}')

    return instance


# Selection Sort
#
# For first n - 1 elements, at i-th element
#   - Find the least element from i to the last
#   - Swap the final least value with i-th element
def selection_sort(input_list: list):
    instance = input_list.copy()

    current = 0
    while current < len(instance) - 1:
        selected = current
        checking = current + 1
        key = instance[current]

        while checking < len(instance):
            if key > instance[checking]:
                key = instance[checking]
                selected = checking
            checking += 1

        instance[selected] = instance[current]
        instance[current] = key

        current += 1
        print(F'Sorting value: {key}, output: {instance}')

    return instance

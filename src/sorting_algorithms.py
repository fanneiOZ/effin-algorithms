import logging
logging.basicConfig(level=logging.INFO)


def insertion_sort(input_list: list):
    """ Insertion Sort
    For 2nd to n elements, at i-th element
      - Given i-th element is the key
      - While key is less than i-1 th element
        - Swap the current position of key with i-1 th element
        - Break the loop immediately when key reach the 1st position

    :param input_list: list of problem elements
    :return: sorted list
    """
    instance = input_list.copy()

    current = 1
    while current < len(instance):
        key = instance[current]
        i = current - 1
        while key < instance[i] and i >= 0:
            instance[i + 1] = instance[i]
            instance[i] = key
            i -= 1

        current += 1
        logging.debug(F'Sorting value: {key}, output: {instance}')

    return instance


def selection_sort(input_list: list):
    """ Selection Sort
    For first n - 1 elements, at i-th element
      - Find the least element from i to the last
      - Swap the final least value with i-th element

    :param input_list: list of problem elements
    :return: sorted list
    """
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
        logging.debug(F'Sorting value: {key}, output: {instance}')

    return instance

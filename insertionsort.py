def insertion_sort(collection, print_probe=True, asc=True):
    if not (type(collection) in (list, tuple, set, frozenset)):
        raise ValueError

    for probe in range(1, len(collection)):
        actual_key = collection[probe]
        index = probe - 1
        sort_statement = is_bigger if asc else is_smaller

        while index >= 0 and sort_statement(actual_key, collection, index):
            collection[index + 1] = collection[index]
            index -= 1  # Zurück an Anfang des Teilsortierten Arrays
        collection[index + 1] = actual_key
        if print_probe:
            print(probe, collection)

    return collection


def is_bigger(actual_key, collection, index):
    return collection[index] > actual_key


def is_smaller(actual_key, collection, index):
    return collection[index] < actual_key


liste = [31, 29, 59, 26, 41, 58]
print(liste)
print('asc', insertion_sort(liste))
print('desc', insertion_sort(liste, asc=False))

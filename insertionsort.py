def insertion_sort(collection, print_probe=True):
    if not (type(collection) in (list, tuple, set, frozenset)):
        raise ValueError

    for probe in range(1, len(collection)):
        actual_key = collection[probe]
        index = probe - 1

        while index >= 0 and collection[index] > actual_key:
            collection[index + 1] = collection[index]
            index -= 1  # Zurück an Anfang des Teilsortierten Arrays
        collection[index + 1] = actual_key
        if print_probe:
            print(probe, collection)

    return collection


liste = [31, 29, 59, 26, 41, 58]
print(liste)
insertion_sort(liste)

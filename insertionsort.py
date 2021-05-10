def insertion_sort(collection):
    if not (type(collection) in (list, tuple, set, frozenset)):
        raise ValueError

    for j in range(1, len(collection)):
        key = collection[j]
        i = j - 1

        while i >= 0 and collection[i] > key:
            collection[i + 1] = collection[i]
            i -= 1  # Zurück an Anfang des Teilsortierten Arrays
        collection[i + 1] = key
        print(j, collection)

    return collection


liste = [31, 29, 59, 26, 41, 58]
print(liste)
insertion_sort(liste)

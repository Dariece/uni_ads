def insertion_sort(collection, print_probe=True, asc=True):
    if not (type(collection) in (list, tuple, set, frozenset)):
        raise ValueError

    for probe in range(1, len(collection)):  # Für Anzahl Versuche in Mengengröße
        actual_key = collection[probe]  # aktuellen Schlüssel durch Versuchanzahl ziehen
        index = probe - 1  # Index berechnen
        sort_statement = is_bigger if asc else is_smaller  # Fallunterscheidung Auf-, oder Absteigend

        while index >= 0 and sort_statement(
                actual_key, collection, index):  # Solange Index > 0 und Zahl in Menge größer als Schlüssel
            collection[index + 1] = collection[index]  # Zahl in Menge eins nach oben setzen
            index -= 1  # Zurück an Anfang des Teilsortierten Arrays
        collection[index + 1] = actual_key  # Schlüssel in Menge an Stelle des Indexes +1 setzen
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

import random

from integer import Integer


class Slot:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"


class DirectAddressTable:

    def __init__(self, slots=None):
        self.slots: list = slots

    def __str__(self):
        ret_val = "{"
        ret_val += "".join(s for s in self.slots)
        return ret_val + "}"

    def insert(self, slot: Slot):
        if self.slots is None:
            self.slots = [slot]
        else:
            self.slots.append(slot)

    def search(self, key):
        return [s for s in self.slots if s.key is key]

    def delete(self, key):
        search_index = self.slots.index(self.search(key)[0])
        self.slots.pop(search_index)


# def char_to_int(key):
#     tmp_int = Integer()
#     return key if isinstance(key, int) else \
#         [tmp_int.add(ord(s) * 128 ** len(key) - i) for i, s in enumerate(key)] if isinstance(key, str) else None


def char_to_int(key):
    return key if isinstance(key, int) else \
       Integer().addAll(*((ord(s) * (128 ** len(key) - i)) for i, s in enumerate(key))) \
           if isinstance(key, str) else None


class HashDirectAddressMultiplication:

    def __init__(self, size, keys=None):
        self.payload = dict()
        self.size = size
        self.constant = random.randint(1, 999) * 0.001

        if keys is not None and type(keys) in (tuple, list, set):
            [self.insert(key) for key in keys]

    def hash_multiplicate(self, key: int) -> int:
        return int(self.size * (key * self.constant % 1))

    def hash(self, key, probe=0) -> int:
        return (self.hash_multiplicate(key) + (probe ** 2 if probe is not 0 else probe)) % self.size

    def insert(self, key) -> int:
        key = char_to_int(key)
        probe = 0
        while probe is not self.size:
            actual_hash = self.hash(key, probe)
            if self.payload.get(actual_hash) is None:
                self.payload[actual_hash] = key
                return actual_hash
            probe += 1
        print("Overflow")

    def search(self, key):
        probe = 0
        actual_hash = 0
        while self.payload.get(actual_hash) is not None \
                or probe is not self.size:
            actual_hash = self.hash(key, probe)

            if self.payload.get(actual_hash) == key:
                return actual_hash
            probe += 1
        return None


def get_max(hashtabelle: dict, max=None):
    ret_val = None
    for i in hashtabelle.items():
        if ret_val is None or i[1] > ret_val[1]:
            ret_val = i
        if max is not None and ret_val[1] >= max:
            break

    return ret_val


adressTable = DirectAddressTable()
adressTable.insert(Slot("key", 2))
adressTable.insert(Slot("key", 3))
adressTable.insert(Slot("ke2", 5))
adressTable.delete("key")
print(adressTable.search("key")[0])

hashTable = HashDirectAddressMultiplication(11, (10, 22, 31, 4, 15, 28, 17, 88, 59))
print(hashTable.payload)
hashTable.insert(10)
hashTable.insert("abc")
print(hashTable.payload)
print(hashTable.search(10))

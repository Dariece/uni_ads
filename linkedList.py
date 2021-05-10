# class DoubleLinkedList:
#     key = None
#     before = None
#
#     def __init__(self, value=None):
#         if type(value) in (tuple, list, set, frozenset):
#             [self.insert(x) for x in value]
#         else:
#             self.key = value
#
#     def insert(self, x):
#         if self.key is not None:
#             new_linked_list = DoubleLinkedList(self.key)
#             new_linked_list.before = self.before
#             self.before = new_linked_list
#         self.key = x
#
#     def delete(self, x):
#         if self.key is x and isinstance(self.before, DoubleLinkedList):
#             self.key = self.before.key
#             self.before = self.before.before
#         else:
#             message = f'Key {x} not in linkedList'
#             raise KeyError(message)
#
#     def __str__(self):
#         return f'{self.before}, {self.key}'

class DoubleLinkedPointerWatcherList:
    key = None
    watcher = None
    after = None
    before = None

    def __init__(self, value=None):
        if type(value) in (tuple, list, set, frozenset):
            [self.insert(x) for x in value]
        else:
            self.key = value

    def search(self, key):
        x = self.watcher.after
        while x is not self.watcher and x.key is not key:
            x = x.after
        return x

    def insert(self, key):
        if self.watcher is None:
            self.watcher = DoubleLinkedPointerWatcherList()
            self.watcher.after = self
        key = DoubleLinkedPointerWatcherList(key)
        key.after = self.watcher.after
        self.watcher.after.before = key
        self.watcher.after = key
        key.before = self.watcher

    def delete(self, key):
        key = self.search(key)
        try:
            if key is not None:
                key.before.after = key.after
                key.after.before = key.before
            else:
                message = f'Key {key} not found in doubleLinkedList'
                raise ValueError(message)
        except Exception as e:
            print(e)

    def __str__(self):
        if self.watcher is not None:
            e = self.watcher
        else:
            e = self
        ret_val = f'[{e.key}'
        while e.after is not None:
            e = e.after
            ret_val += f', {e.key}'
        ret_val += ']'
        return ret_val


class LinkedList(object):
    head = None
    key = None
    after = None

    def __init__(self, value=None):
        if type(value) in (tuple, list, set, frozenset):
            [self.insert(x) for x in value]
        else:
            self.key = value

    def insert(self, x):
        self.key = x
        x = LinkedList(x)
        x.after = self.head
        self.head = x

    def delete(self, x):
        x = LinkedList(x)
        e: LinkedList = self.head
        while e is not None:
            if e.key is x.key:
                x.after = e.after
                self.head = x.after
                break
            e = e.after
        else:
            message = f'Value {x} not in linkedList'
            raise ValueError(message)

    def __str__(self):
        if self.head is not None:
            e = self.head
        else:
            e = self
        ret_val = f'[{e.key}'
        while e.after is not None:
            e = e.after
            ret_val += f', {e.key}'
        ret_val += ']'
        return ret_val

    def search(self, search_key):
        ret_val: LinkedList = self.head
        while ret_val is not None and ret_val.key is not search_key:
            ret_val = ret_val.after
        return ret_val

    def __getitem__(self, search_index):
        index = 0
        e: LinkedList = self.head
        while e is not None:
            if index is search_index:
                return e.key
            e = e.after
            index += 1
        else:
            message = f'Index {search_index} out of linkedList'
            raise IndexError(message)

    def setitem_slice(self, new_key: tuple, start, stop=None, step=1):
        new_key = new_key[0]
        search_index_range = None
        range_index = None
        search_index = start
        if stop is not None:
            range_index = 0
            search_index_range = range(start, stop)
            search_index = search_index_range[range_index]

        e: LinkedList = self.head if self.head is not None else self
        index = 0

        while e is not None or index is not stop:
            if index is search_index and index >= start:
                if e is None and self.after is None:
                    e = self
                    e.insert(new_key)
                else:
                    e.key = new_key
                if search_index_range is not None:
                    range_index += 1
                    search_index = search_index_range[range_index]
                    if search_index_range.stop is range_index:
                        break
                else:
                    break
            e = e.after
            index += step
        else:
            message = f'Index {search_index} out of linkedList'
            raise IndexError(message)

    def __setitem__(self, search_index, new_key):
        if isinstance(search_index, slice):
            start = search_index.start
            stop = search_index.stop if search_index.stop is not None else None
            step = search_index.step if search_index.step is not None else 1
            self.setitem_slice(new_key, start, stop, step)
        else:
            index = 0
            e: LinkedList = self.head if self.head is not None else self
            while e is not None:
                if index is search_index:
                    e.key = new_key
                    break
                e = e.after
                index += 1
            else:
                message = f'Index {search_index} out of linkedList'
                raise IndexError(message)

    def __delitem__(self, key):
        self.delete(self.__getitem__(key))

    def __len__(self):
        index = 0
        e: LinkedList = self.head
        while e is not None:
            e = e.after
            index += 1
        return index

from linkedList import LinkedList


class CustomStack:

    def __init__(self, length):
        self.length = length
        self.payload = []
        top = 0

    def is_empty(self):
        return 0 == self.top

    def check_overflow(self):
        return self.top >= self.length

    def push(self, value):
        if self.check_overflow():
            raise OverflowError(f"StackOverflow: top {self.top}, length {self.length}")

        if not self.is_empty():
            self.payload[self.top:] = value,
            self.top += 1
        else:
            self.top = 1
            self.payload = [value]

    def pop(self):
        if not self.is_empty():
            ret_val = self.payload[self.top - 1]
            self.top -= 1
        else:
            raise ValueError('Underflow')

        return ret_val

    def print_push(self, value):
        self.push(value)
        print("push", value)
        print(self)

    def print_pop(self):
        print("pop", self.pop())
        print(self)

    def print_detailed(self):
        print(self, 'top:', self.top, 'length:', self.length)

    def __str__(self):
        p = self.payload
        str_payload = [p[i] if i < len(p) else '' for i in range(self.length)]
        if not self.is_empty():
            str_payload = [x if not x == p[self.top - 1] else f'{x}' for x in str_payload]

        return f"{str_payload}"


class LinkedListStack(CustomStack):
    payload = LinkedList()

    def push(self, value):
        if self.check_overflow():
            raise OverflowError(f"StackOverflow: top {self.top}, length {self.length}")

        if not self.is_empty():
            self.payload[self.top:] = value,
            self.top += 1
        else:
            self.top = 1
            self.payload.insert(value)

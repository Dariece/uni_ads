from customStack import CustomStack


class InterfaceQueue:
    def is_empty(self) -> bool:
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def print_enqueue(self, value):
        pass

    def print_dequeue(self):
        pass

    def print_detailed(self):
        pass

class DefaultQueue(InterfaceQueue):
    payload = []
    head = 0
    end = 0
    length = 0

    def __init__(self, length):
        self.length = length

    def is_empty(self):
        return self.head == self.end

    def enqueue(self, value):
        if self.is_empty():
            self.head = 1
            self.end = 1

        self.payload[self.end - 1:] = value,

        if self.end == self.length:
            self.end = 1
        else:
            self.end += 1

    def dequeue(self):
        value = self.payload[self.head - 1]

        if self.head == self.length:
            self.head = 1
        else:
            self.head += 1

        return value

    def print_enqueue(self, value):
        self.enqueue(value)
        print("enqueue", value)
        print(self)

    def print_dequeue(self):
        print("dequeue", self.dequeue())
        print(self)

    def print_detailed(self):
        print(self, 'head:', self.head, 'end:', self.end, 'length:', self.length)

    def __str__(self):
        p = self.payload
        end = self.end - 1
        str_payload = [p[i] if i < len(p) else '' for i in range(self.length)]
        str_payload = [x if not x == p[self.head - 1] else f'[{x}]' for x in str_payload]
        str_payload[end] = f'|{str_payload[end]}|'

        return f"{str_payload}"


class StackQueue(InterfaceQueue):
    length = 1
    head = CustomStack(length)
    end = CustomStack(length)

    def __init__(self, length):
        self.length = length
        self.head = CustomStack(length)
        self.end = CustomStack(length)

    def is_empty(self):
        return self.end.is_empty() and self.head.is_empty()

    def enqueue(self, value):
        self.end.push(value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Underflow')

        if self.head.is_empty():
            while not self.end.is_empty():
                self.head.push(self.end.pop())
        return self.head.pop()

    def print_enqueue(self, value):
        self.enqueue(value)
        print("enqueue", value)
        print(self)

    def print_dequeue(self):
        print("dequeue", self.dequeue())
        print(self)

    def print_detailed(self):
        print(self, 'end_top:', self.end.top, 'head_top:', self.head.top, 'length:', self.length)

    def __str__(self):
        return f"end: {self.end}, head:{self.head}"

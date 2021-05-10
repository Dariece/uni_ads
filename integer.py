class Integer:
    value = 0

    def __init__(self, num=0):
        self.value = num

    def add(self, num):
        self.value += num
        return self.value

    def addAll(self, *numbers):
        [self.add(n) for n in numbers]
        return self.value

    def sub(self, num):
        self.value -= num

    def __str__(self):
        return f'{self.value}'

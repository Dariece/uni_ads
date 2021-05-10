import time

from customQueue import DefaultQueue
from customQueue import InterfaceQueue
from customQueue import StackQueue
from customStack import CustomStack
from customStack import LinkedListStack


def test_all():
    q = DefaultQueue(6)
    test(q, False)

    q = StackQueue(6)
    test(q, False)

    s = CustomStack(6)
    test(s, False)

    s = LinkedListStack(6)
    test(s, False)

    # initList = [15, 6, 2, 9]
    # [s.push(x) for x in initList]
    # print('Initialer Zustand Stack:', s)
    # s.print_push(17)
    # s.print_push(13)
    # s.print_pop()
    # s.print_push(18)
    # s.print_detailed()


def test(test_object, prnt=True):
    if isinstance(test_object, InterfaceQueue):
        if prnt:
            test_object.print_enqueue(4)
            test_object.print_enqueue(1)
            test_object.print_enqueue(3)
            test_object.print_dequeue()
            test_object.print_enqueue(8)
            test_object.print_dequeue()
            test_object.print_detailed()
            print()
        else:
            start = time.time()
            test_object.enqueue(4)
            test_object.enqueue(1)
            test_object.enqueue(3)
            test_object.dequeue()
            test_object.enqueue(8)
            test_object.dequeue()
            end = time.time()
            print(f'{type(test_object).__name__}Time: {end - start:5.20f}s')
    else:
        if prnt:
            test_object.print_push(4)
            test_object.print_push(1)
            test_object.print_push(3)
            test_object.print_pop()
            test_object.print_push(8)
            test_object.print_pop()
            test_object.print_detailed()
            print()
        else:
            start = time.time()
            test_object.push(4)
            test_object.push(1)
            test_object.push(3)
            test_object.pop()
            test_object.push(8)
            test_object.pop()
            end = time.time()
            print(f'{type(test_object).__name__}Time: {end - start:5.20f}s')
    pass


test_all()

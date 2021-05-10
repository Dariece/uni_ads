from linkedList import LinkedList
from linkedList import DoubleLinkedPointerWatcherList

liste = LinkedList((1, 'bla', 3, 4, 5))
print(liste)
liste.delete(5)  # del liste[0] #or

print(liste)
liste[0] = 3
print(liste.search(3))

liste = DoubleLinkedPointerWatcherList((1, 'bla', 3, 4, 5))
print(liste)
INFINITY = float('infinity')


def merge_sort(collection: list, start: int, end: int):
    if start < end:
        dividend = (start + end) // 2
        merge_sort(collection, start, dividend)
        merge_sort(collection, dividend + 1, end)
        merge(collection, start, dividend, end)


def merge(A, p, q, r):
    left_length = q - p + 1
    right_length = r - q

    left_array = A[p:p + left_length]
    right_array = A[q + 1:q + right_length + 1]
    left_array.append(INFINITY)
    right_array.append(INFINITY)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if left_array[i] <= right_array[j]:
            A[k] = left_array[i]
            i += 1
        else:
            A[k] = right_array[j]
            j += 1


A = [4, 7, 2, 6, 1, 4, 7, 3, 5, 2, 6]
print(A)
merge_sort(A, 0, 10)
print(A)

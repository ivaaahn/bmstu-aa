from .types import ArrayInt


def bubble_sort(a: ArrayInt, n: int) -> None:
    i = 0
    while i < n - 1:

        j = 0
        while j < n - i - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1

        i += 1


def insertion_sort(a: ArrayInt, n: int) -> None:
    i = 1
    while i < n:
        key = a[i]

        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

        i += 1


def selection_sort(a: ArrayInt, n: int) -> None:
    i = 0
    while i < n - 1:
        min_idx = i

        j = i + 1
        while j < n:
            if a[j] < a[min_idx]:
                min_idx = j
            j += 1

        a[min_idx], a[i] = a[min_idx], a[i]

        i += 1

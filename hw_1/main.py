from random import randint
import numpy as np


def main():
    size = 5                                                    # (1)
    a = np.empty(size)                                          # (2)

    # consider as "for (k = 0; k < size; k++)"
    for k in range(size):                                       # (3)

        # For the history a case
        # "a = [5, 4, 3, 2, 1]" is considered
        a[k] = randint(-99, 99)                                 # (4)

    n = len(a)                                                  # (5)
    gap = n // 2                                                # (6)

    while gap > 0:                                              # (7)
        i = gap                                                 # (8)
        while i < n:                                            # (9)
            temp = a[i]                                         # (10)
            j = i                                               # (11)
            while j >= gap and a[j - gap] > temp:               # (12)
                a[j] = a[j - gap]                               # (13)
                j -= gap                                        # (14)
            a[j] = temp                                         # (15)

            i += 1                                              # (16)
        gap //= 2                                               # (17)


if __name__ == '__main__':
    main()

from termcolor import cprint, colored
import csv

from dicts import Dictionary, SegDictionary, Pair

PATH = './data'


def stat(m: Dictionary, sm: SegDictionary):
    _scnd_ver1: list[tuple[int, Pair]] = []
    _scnd_ver2 = []
    _scnd_ver3 = []

    f1 = open(f'{PATH}/stat1.csv', 'w')
    f2 = open(f'{PATH}/stat2.csv', 'w')
    f3 = open(f'{PATH}/stat3.csv', 'w')

    fieldnames = ['value']

    w1 = csv.DictWriter(f1, fieldnames=fieldnames)
    w2 = csv.DictWriter(f2, fieldnames=fieldnames)
    w3 = csv.DictWriter(f3, fieldnames=fieldnames)

    for w in (w1, w2, w3):
        w.writeheader()

    length = len(m.data)
    for idx, pairs in enumerate(zip(m.data, sorted(m.data, key=lambda x: x.key))):
        res1, res2, res3 = m.find1(pairs[0].key), m.find2(pairs[1].key), sm.find(pairs[1].key)

        w1.writerow({'value': res1[1]})  # По возрастанию
        w2.writerow({'value': res2[1]})  # По алфавиту
        w3.writerow({'value': res3[1]})  # По алфавиту

        _scnd_ver1.append((idx, res1))
        _scnd_ver2.append((idx, res2[1]))
        _scnd_ver3.append((idx, res3[1]))

        if (idx + 1) % 500 == 0:
            print(f'Completed on {round((idx + 1) / length * 100, 2)} %')

    _scnd_ver1.sort(key=lambda x: x[1][0].key)  # По алфавиту
    _scnd_ver2.sort(key=lambda x: x[1])  # По возрастанию
    _scnd_ver3.sort(key=lambda x: x[1])

    f1.close()
    f2.close()
    f3.close()

    f1 = open(f'{PATH}/stat11.csv', 'w')
    f2 = open(f'{PATH}/stat22.csv', 'w')
    f3 = open(f'{PATH}/stat33.csv', 'w')

    w1 = csv.DictWriter(f1, fieldnames=fieldnames)
    w2 = csv.DictWriter(f2, fieldnames=fieldnames)
    w3 = csv.DictWriter(f3, fieldnames=fieldnames)

    for w in (w1, w2, w3):
        w.writeheader()

    for idx, items in enumerate(zip(_scnd_ver1, _scnd_ver2, _scnd_ver3)):
        w1.writerow({'value': items[0][1][1]})  # По возрастанию
        w2.writerow({'value': items[1][1]})  # По алфавиту
        w3.writerow({'value': items[2][1]})  # По алфавиту

        if (idx + 1) % 500 == 0:
            print(f'Completed on {round((idx + 1) / length * 100, 2)} %')

    f1.close()
    f2.close()
    f3.close()


def main():
    filename = f'{PATH}/test2.txt'
    m = Dictionary(filename=filename)
    sm = SegDictionary(m)

    cprint("1. Поиск\n2. Эксперимент", color='yellow', attrs=['bold'])

    try:
        choice = int(input())
    except:
        print("Введено некорректное число")
        return -1

    if choice not in (1, 2):
        print("Введено некорректное число")
        return -1

    if choice == 1:
        key = str(input("Введите key: ")).strip()

        print(f'Перебор: {colored(m.find1(key), color="red", attrs=["bold"])}')
        print(f'Бинарный поиск: {colored(m.find2(key), color="red", attrs=["bold"])}')
        print(f'Сегментация: {colored(sm.find(key), color="red", attrs=["bold"])}')
    else:
        stat(m, sm)


if __name__ == '__main__':
    main()

from ants.benchmarks import Benchmark
from ants.brute_force import brute_force
from ants.colony import Colony
from interaction import UserInteraction
from termcolor import colored, cprint

if __name__ == '__main__':
    cprint("1. Ручной режим\n2. Benchmark", color='yellow', attrs=['bold'])

    try:
        choice = int(input())
    except:
        print("Введено некорректное число")
        exit(-1)

    if choice not in (1, 2):
        print("Введено некорректное число")
        exit(-1)

    if choice == 1:
        if m := UserInteraction().start():
            try:
                days = int(input(colored('Введите количество дней жизни колонии: ', color='red', attrs=['bold'])))
            except:
                print("Введено некорректное число")
                exit(-1)

            if days <= 0:
                print("Введено некорректное число")
                exit(-1)

            print()
            print(colored("Муравьиный алгоритм: ", color='red', attrs=['bold']), Colony(path_map=m, days=100).live())
            print(colored("Полный перебор: ", color='red', attrs=['bold']), brute_force(m))

    else:
        Benchmark().run()
# from matrix import Matrix
#
# if __name__ == '__main__':
#     matrix = Matrix.generate(nodes_count=5)
#     table = []
#
#     for days in (10, 11, 12):
#         for alpha in np.arange(0, 1.1, 0.2):
#             for p in np.arange(0.2, 1.1, 0.2):
#                 brute, _ = brute_force(matrix)
#                 ant, _ = Colony(path_map=matrix, days=days, alpha=alpha, beta=1 - alpha, p=p).live()
#                 diff = abs(brute - ant)
#                 table.append([days, alpha, p, ant, diff])
#
#     print(tabulate(table, headers=['Кол-во дней', 'Альфа', 'P', 'Результат Ant', 'Погрешность'], tablefmt='pretty'))

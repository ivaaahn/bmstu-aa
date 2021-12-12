from benchmarks import run_benchmark
from brute_force import brute_force
from colony import Colony

if __name__ == '__main__':
    run_benchmark()
    #
    # matrix = [
    #     [0, 10, 5, 9, 11],
    #     [10, 0, 11, 8, 12],
    #     [5, 11, 0, 3, 9],
    #     [9, 8, 3, 0, 12],
    #     [11, 12, 9, 12, 0],
    # ]
    #
    # print(Colony(path_map=matrix, days=100).find_path())
    # print(brute_force(matrix))

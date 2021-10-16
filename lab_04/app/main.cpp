//
// Created by ivaaahn on 14.10.2021.
//

#include "point.hpp"
#include "points.hpp"

#include <string>
#include <iostream>
#include <chrono>

#include <thread>

#define REPEATS 100
#define PATH_TO_DATA "../app/data/"


#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */
#define RESET   "\033[0m"


void print_points(std::vector<double3>& points) {
    for (auto& p: points)
        printf("(%lf, %lf, %lf)\n", p.x, p.y, p.z);
}

void handle(std::vector<double3>& points, double3& center, const double3& rotate_data, int num_of_threads = 1) {
    using std::move, std::thread, std::ref;

    int points_per_thread = int(points.size()) / num_of_threads;
    int remaining_data = int(points.size()) - points_per_thread * num_of_threads;

    std::vector<std::thread> threads;
    threads.reserve(num_of_threads);

    int last = -1, from, to;
    for (int i = 0; i < num_of_threads; ++i)
    {
        from = last + 1;
        if (i < remaining_data)
        {
            to = last + points_per_thread + 1;
            last += points_per_thread + 1;
        }
        else
        {
            to = last + points_per_thread;
            last += points_per_thread;
        }

        threads.push_back(move(thread(rotate_points, ref(points), ref(center), rotate_data, from, to)));
    }

    for (auto& t: threads)
        t.join();
}

int write(std::vector<double3>& points, FILE *fd) {
    return write_points(points, fd);
}


using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;


int main(int argc, char *argv[]) {
    std::cout << BOLDYELLOW << "Введите желаемое количество потоков: " << RESET;

    int num_of_threads = 1;
    std::cin >> num_of_threads;

    if (num_of_threads < 1)
    {
        std::cout << BOLDRED << "Некорректное количество потоков." << RESET << std::endl;
        return -1;
    }

    std::vector<double3> points;
    double3 center{};

    std::string file_name;

    std::cout << BOLDYELLOW << "Введите имя входного файла (из директории data/): " << RESET;
    std::cin >> file_name;

    file_name = PATH_TO_DATA + file_name;
    std::cout << file_name << std::endl;
    FILE *fin = fopen(file_name.c_str(), "r");
    if (!fin)
    {
        std::cout << BOLDRED << "Не удалось открыть файл с названием " + file_name << RESET << std::endl;
        return ERR_FOPEN;
    }

    err_t rc = load_points(points, center, fin);
    fclose(fin);

    if (rc != SUCCESS)
    {
        if (rc == ERR_FREAD)
            std::cout << BOLDRED << "Не удалось загрузить точки из файла" << RESET << std::endl;
        else
            std::cout << BOLDRED << "Неизвестная ошибка" << RESET << std::endl;

        return rc;
    }

    double ax, ay, az;
    std::cout << BOLDYELLOW << "Введите три числа - углы повотора по ox/oy/oz: " << RESET;
    std::cin >> ax >> ay >> az;

//    double3 rotate_data {ax, ay, ax};

    auto t1 = high_resolution_clock::now();

    for (int i = 0; i < REPEATS; i++)
        handle(points, center, {ax, ay, az}, num_of_threads);
    auto t2 = high_resolution_clock::now();

    duration<double, std::milli> ms_double = t2 - t1;

    std::cout << BOLDBLUE << ms_double.count() / REPEATS << "ms" << RESET << std::endl;


//    std::cout << BOLDYELLOW << "Введите имя выходного файла (из директории data/): " << RESET;
//    std::cin >> file_name;

    const std::string default_fout = std::string(PATH_TO_DATA) + "default_out.txt";

//    file_name = PATH_TO_DATA + file_name;
    FILE *fout = fopen(default_fout.c_str(), "w");
//    if (!fout)
//    {
//        std::cout << BOLDRED << "Не удалось открыть файл с названием " + file_name << RESET << std::endl;
//        std::cout << BOLDRED << "Результаты будут сохранены в файле " + default_fout << RESET << std::endl;
//        fout = fopen(default_fout.c_str(), "w");
//        write(points, fout);
//        fclose(fout);
//
//        return ERR_FOPEN;
//    }

    write(points, fout);
    fclose(fout);

    return 0;
}
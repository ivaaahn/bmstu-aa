//
// Created by ivaaahn on 14.10.2021.
//

#include "point.hpp"
#include "points.hpp"

#include <string>
#include <iostream>
#include <chrono>

#include <thread>

#define FIN "../app/data/points.txt"
#define FOUT "../app/data/points_res.txt"

void print_points(std::vector<double3>& points) {
    for (auto& p: points)
        printf("(%lf, %lf, %lf)\n", p.x, p.y, p.z);
}

int load(std::vector<double3>& points, double3& center, const std::string& filename) {
    FILE *f = fopen(filename.c_str(), "r");
    auto err = load_points(points, center, f);

//    printf("%d\n", err);
//
//    printf("(%lf, %lf, %lf)\n", center.x, center.y, center.z);
//    print_points(points);
    std::cout << "\n\n\n";
    return SUCCESS;
}

#define NUM_OF_THREADS 128


void handle(std::vector<double3>& points, double3& center, int num_of_threads = 1) {
    int points_per_thread = int(points.size()) / num_of_threads;
    int remaining_data = int(points.size()) - points_per_thread * num_of_threads;
//    std::cout << points_per_thread << ' ' << remaining_data << std::endl;

//    std::vector<std::pair<int, int>> q;

    std::vector<std::thread> threads;
    threads.reserve(num_of_threads);

    int last = -1;
    for (int i = 0; i < num_of_threads; ++i)
    {
        if (i < remaining_data)
        {
            threads.push_back(std::move(
                    std::thread(rotate_points, std::ref(points), std::ref(center), double3{123, 321, -569}, last + 1,
                                last + points_per_thread + 1)));
//            q.push_back({last + 1, last + points_per_thread + 1});
//            std::cout <<  last + 1 << ":" << last + points_per_thread + 1 << " (" << 1 + points_per_thread << ")" << std::endl;
            last += points_per_thread + 1;
        }
        else
        {
            threads.push_back(std::move(
                    std::thread(rotate_points, std::ref(points), std::ref(center), double3{-10325, 10345, -98441}, last + 1,
                                last + points_per_thread)));
//            std::cout <<  last + 1 << ":" << last + points_per_thread << " (" << points_per_thread << ")" << std::endl;

//            q.push_back({last + 1, last + points_per_thread});
//            last += points_per_thread;
        }
    }

//    for (auto& p: q)
//        std::cout << p.first << ":" << p.second << " (" << p.second - p.first + 1 << ")" << std::endl;
//
//
//    for (auto& p: q)
//    {
//        threads.push_back(std::move(
//                std::thread(rotate_points, std::ref(points), std::ref(center), double3{123, 321, -569}, p.first-1,
//                            p.second-1)));
//
//    }

    for (auto& t: threads)
        t.join();
//
//    std::thread x(rotate_points, std::ref(points), std::ref(center), {123, 321, -569}, 0,1);

//    std::thread a(rotate_points, points, center, {123, 321, -569}, 0, 1);
//        rotate_points(points, center, {123, 321, -569}, NUM_OF_THREADS);
//    print_points(points);
}

int write(std::vector<double3>& points, const std::string& filename) {
    FILE *f = fopen(filename.c_str(), "w");
    write_points(points, f);

    return SUCCESS;
}

int main(int argc, char *argv[]) {
    std::vector<double3> points;
    std::vector<double3> points_res;
    double3 center{};

    load(points, center, FIN);

    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;

    const int count = 100;

    auto t1 = high_resolution_clock::now();
    for (int i = 0; i < count; i++)
        handle(points, center, NUM_OF_THREADS);
    auto t2 = high_resolution_clock::now();

    duration<double, std::milli> ms_double = t2 - t1;
    std::cout << ms_double.count() / count << "ms";
    write(points, FOUT);
//
//
//
//    if (argc >= 2)
//        go(argv[1]);
//    else
//    {
//        err_handler(ERR_ARGV);
//        return EXIT_FAILURE;
//    }

    return 0;
}
//
// Created by ivaaahn on 14.10.2021.
//

#ifndef __LAB_04_POINTS_HPP__
#define __LAB_04_POINTS_HPP__

#include <cstdlib>
#include <cstdio>

#include "point.hpp"
#include "errors.hpp"
#include <vector>


struct points_set {
    std::vector <double3> points;
    double3 center;
};


err_t load_points(std::vector <double3>& points, double3& center, FILE *fd);
err_t write_points(std::vector<double3>& points, FILE *datafile);
err_t rotate_points(std::vector<double3>& points, double3& center, const double3& rot_data, int idx0, int idx1);


#endif //__LAB_04_POINTS_HPP__

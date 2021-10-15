//
// Created by ivaaahn on 14.10.2021.
//

#ifndef __LAB_04_POINT_HPP__
#define __LAB_04_POINT_HPP__

#include <cstdio>
#include "errors.hpp"

struct double3 {
    double x;
    double y;
    double z;
};

err_t write_point(double3& p, FILE *datafile);

err_t read_point(double3& point, FILE *datafile);

err_t translate_point(double3& point, const double3& translate_data);
//
//err_t scale_point(double3& point, const double3& scale_data);

err_t rotate_point(double3& point, const double3& rotate_data);


#endif //__LAB_04_POINT_HPP__

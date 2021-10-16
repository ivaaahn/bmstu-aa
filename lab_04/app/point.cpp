//
// Created by ivaaahn on 14.10.2021.
//

#include <cmath>
#include <iostream>

#include "point.hpp"
#include "errors.hpp"


double to_rad(const double angle) {
    return angle * M_PI / 180.0;
}

using std::cout, std::endl;

err_t read_point(double3& p, FILE *datafile) {
    int cnt;
    if ((cnt = fscanf(datafile, "%lf %lf %lf", &p.x, &p.y, &p.z)) != 3)
    {
        std::cout << cnt << std::endl;
        return ERR_FREAD;
    }

    return SUCCESS;
}

err_t write_point(double3& p, FILE *datafile) {
    fprintf(datafile, "%lf %lf %lf\n", p.x, p.y, p.z);
    return SUCCESS;
}

static void rotate_x_axis(double3& p, const double angle) {
    double cos_theta = cos(to_rad(angle));
    double sin_theta = sin(to_rad(angle));

    double temp_y = p.y;
    p.y = p.y * cos_theta - p.z * sin_theta;
    p.z = temp_y * sin_theta + p.z * cos_theta;
}

static void rotate_y_axis(double3& p, const double angle) {
    double cos_theta = cos(to_rad(angle));
    double sin_theta = sin(to_rad(angle));

    double temp_x = p.x;
    p.x = p.x * cos_theta - p.z * sin_theta;
    p.z = temp_x * sin_theta + p.z * cos_theta;
}

static void rotate_z_axis(double3& p, const double angle) {
    double cos_theta = cos(to_rad(angle));
    double sin_theta = sin(to_rad(angle));

    double temp_x = p.x;
    p.x = p.x * cos_theta - p.y * sin_theta;
    p.y = temp_x * sin_theta + p.y * cos_theta;
}

err_t translate_point(double3& p, const double3& tr_data) {
    p.x += tr_data.x;
    p.y += tr_data.y;
    p.z += tr_data.z;

    return SUCCESS;
}

//err_t scale_point(double3& p, const double3& sc_data) {
//    p.x *= sc_data.x;
//    p.y *= sc_data.y;
//    p.z *= sc_data.z;
//
//    return SUCCESS;
//}

err_t rotate_point(double3& point, const double3& rot_data) {
    rotate_x_axis(point, rot_data.x);
    rotate_y_axis(point, rot_data.y);
    rotate_z_axis(point, rot_data.z);

    return SUCCESS;
}
//
// Created by ivaaahn on 14.10.2021.
//

#include <iostream>
#include "points.hpp"

static err_t read_points_count(std::vector<double3>& points, FILE *datafile) {
    size_t tmp_count = 0;

    if ((fscanf(datafile, "%zu", &tmp_count)) != 1)
        return ERR_FREAD;

    if (tmp_count < 2)
        return ERR_POINTS_QTY;

    points.resize(tmp_count);

    return SUCCESS;
}

static err_t read_points(std::vector<double3>& points, double3& center, FILE *datafile) {
    err_t rc = SUCCESS;
    for (size_t i = 0; rc == SUCCESS && i < points.size(); i++)
        rc = read_point(points[i], datafile);

    rc = read_point(center, datafile);  // read center of all points

    return rc;
}

err_t translate_points(std::vector<double3>& points, double3& center, const double3& tr_data) {
    for (size_t i = 0; i < points.size(); i++)
        translate_point(points[i], tr_data);

//    translate_point(center, tr_data);

    return SUCCESS;
}
//
//err_t scale_points(std::vector <double3>& points, double3& center, const double3& sc_data) {
//    for (size_t i = 0; i < points.points.size(); i++)
//        scale_point(points[i], sc_data);
//
//    return SUCCESS;
//}


err_t write_points(std::vector<double3>& points, FILE *datafile) {
    for (auto& p: points)
        write_point(p, datafile);

    return SUCCESS;
}

#include <thread>

err_t rotate_points(std::vector<double3>& points, double3& center, const double3& rot_data, int idx0, int idx1) {
//    std::cout << (std::this_thread::get_id()) << std::endl;
    for (int i = idx0; i <= idx1; ++i)
    {
        translate_point(points[i], {-center.x, -center.y, -center.z});
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        rotate_point(points[i], rot_data);
        translate_point(points[i], {center.x, center.y, center.z});
    }

    return SUCCESS;
}

err_t load_points(std::vector<double3>& points, double3& center, FILE *datafile) {
    err_t rc = SUCCESS;

    if ((rc = read_points_count(points, datafile)) != SUCCESS)
        return rc;

    if ((rc = read_points(points, center, datafile)) != SUCCESS)
        return rc;

    return rc;
}

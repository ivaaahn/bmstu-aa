//
// Created by ivaaahn on 14.10.2021.
//

#ifndef __LAB_04_ERRORS_HPP__
#define __LAB_04_ERRORS_HPP__

#include <string>

#define SUCCESS         0

#define ERR_FOPEN       1   // file open
#define ERR_FREAD       2   // file read

#define ERR_ALLOC       3
#define ERR_POINTS_QTY  4   // num of points
#define ERR_MEM         6

#define ERR_ARGV        7


typedef int err_t;

std::string err_handler(err_t code);

#endif //__LAB_04_ERRORS_HPP__
